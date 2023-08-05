# Copyright 2021 Okera Inc. All Rights Reserved.
#
# Some scenario tests for steward delegation
#
# pylint: disable=broad-except
# pylint: disable=global-statement
# pylint: disable=no-self-use
# pylint: disable=too-many-lines
# pylint: disable=too-many-public-methods
# pylint: disable=too-many-locals
# pylint: disable=bad-continuation
# pylint: disable=broad-except

"""
+---------------+--------------------------+----------+---------+---------+---------+---------+-------+
|      rpc      |           name           |   user   |   mean  |   50%   |   90%   |   99%   | iters |
+---------------+--------------------------+----------+---------+---------+---------+---------+-------+
| list_datasets | Wide table w/ attributes |  admin   |  57.408 |  56.484 |  57.609 |  93.027 |   50  |
| list_datasets | Wide table w/ attributes | testuser | 334.477 | 312.530 | 373.459 | 577.000 |   50  |
+---------------+--------------------------+----------+---------+---------+---------+---------+-------+
"""

import statistics

from okera import context
from okera import _thrift_api
from okera.tests import pycerebro_test_common as common
from prettytable import PrettyTable

ATTR = "perf_test.attr1"
DB = "python_perf_test_db"
TBL1 = "tbl1"
TBL2 = "tbl2"
ROLE = "python_perf_test_role"
TEST_USER = "pythonperfuser"

def _create_wide_view(db, tbl, multiple, source_db, source_tbl):
    cols = []
    for idx in range(multiple):
        cols.extend([
            "uid AS uid%04d" % (idx),
            "dob AS dob%04d" % (idx),
            "gender AS gender%04d" % (idx),
            "ccn AS ccn%04d" % (idx),
        ])
    stmt = "CREATE VIEW %s.%s AS SELECT %s FROM %s.%s" % (
        db, tbl, ', '.join(cols), source_db, source_tbl)

    return stmt

OUTPUT_TABLE = PrettyTable(
  ['rpc', 'name', 'user', 'mean', '50%', '90%', '99%', 'iters']
)

class PerfTest(common.TestBase):
    @classmethod
    def setUpClass(cls):
        print("\n\nSetting up perf test.")
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            ddls = [
                "DROP ATTRIBUTE IF EXISTS %s" % (ATTR),
                "CREATE ATTRIBUTE %s" % (ATTR),

                "DROP DATABASE IF EXISTS %s CASCADE" % (DB),
                "CREATE DATABASE %s" % (DB),

                """CREATE TABLE {db}.users (
                  uid STRING ATTRIBUTE {attr},
                  dob STRING ATTRIBUTE {attr},
                  gender STRING ATTRIBUTE {attr},
                  ccn STRING ATTRIBUTE {attr}
                )""".format(db=DB, attr=ATTR),

                _create_wide_view(DB, TBL1, 100, DB, 'users'),

                "DROP ROLE IF EXISTS %s" % (ROLE),
                "CREATE ROLE %s WITH GROUPS %s" % (ROLE, TEST_USER),
                "GRANT SELECT ON DATABASE %s HAVING ATTRIBUTE IN (%s) TO ROLE %s" % \
                    (DB, ATTR, ROLE),
            ]

            for ddl in ddls:
                conn.execute_ddl(ddl)
        print("...Done setting up perf test")

    @classmethod
    def tearDownClass(cls):
        print("\nPerf tests done:")
        print(str(OUTPUT_TABLE))

    def measure(self, fn, msg, user, rpc, iters=50):
      latencies = common.measure_latency(iters, fn, msg=msg)
      mean = "{:.3f}".format(statistics.mean(latencies))
      p50 = "{:.3f}".format(latencies[int(len(latencies) * .5)])
      p90 = "{:.3f}".format(latencies[int(len(latencies) * .9)])
      p99 = "{:.3f}".format(latencies[int(len(latencies) * .99)])
      row = [rpc, msg, user, mean, p50, p90, p99, iters]
      OUTPUT_TABLE.add_row(row)

    def test_wide_table_with_attributes(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            def list(tbl):
                def get():
                    datasets = conn.list_datasets(DB, name=tbl)
                    assert len(datasets) == 1
                return get

            """
            ---------------------------- admin --------------------------
            Iterations 50
            Mean 57.408270835876465 ms
            50%: 56.48446083068848 ms
            90%: 57.608842849731445 ms
            95%: 58.23540687561035 ms
            99%: 93.02711486816406 ms
            99.5%: 93.02711486816406 ms
            99.9%: 93.02711486816406 ms
            """
            self.measure(list(TBL1), "Wide table w/ attributes",
                         "admin", "list_datasets")

            """
            ---------------------------- test user --------------------------
            Iterations 50
            Mean 334.47683811187744 ms
            50%: 312.5302791595459 ms
            90%: 373.4593391418457 ms
            95%: 374.4511604309082 ms
            99%: 576.9996643066406 ms
            99.5%: 576.9996643066406 ms
            99.9%: 576.9996643066406 ms
            """
            ctx.enable_token_auth(token_str=TEST_USER)
            self.measure(list(TBL1), "Wide table w/ attributes",
                         "testuser", "list_datasets")

