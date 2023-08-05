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


import os
import statistics
import time

from okera import context
from okera import _thrift_api
from okera.tests import pycerebro_test_common as common
from prettytable import PrettyTable

def read_sql_file(path, **kwargs):
    sql = open(path, 'r').read()
    return sql.format(**kwargs)

class XilinxTest(common.TestBase):

    def test_xilinx_tbl1(self):
        db = 'xilinx_test_db'
        tbl1 = 'flash_view_wtd'
        role = 'xilinx_test_role'
        testuser = 'xilinxuser'

        flash_view_wtd_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'assets', 'xilinx_flash_view_wtd.sql')

        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            ddls = [
                "DROP DATABASE IF EXISTS %s CASCADE" % (db),
                "CREATE DATABASE %s" % (db),
                read_sql_file(flash_view_wtd_path, db=db, tbl=tbl1),

                "create attribute if not exists flash.cogs_bklg_cra",
                "create attribute if not exists flash.cogs_bklg_si",
                "create attribute if not exists flash.cogs_bklg_st",
                "create attribute if not exists flash.cogs_hist_cra",
                "create attribute if not exists flash.cogs_hist_si",
                "create attribute if not exists flash.cogs_hist_st",
                "create attribute if not exists flash.dimension",
                "create attribute if not exists flash.measure",
                "create attribute if not exists flash.qty_bklg_cra",
                "create attribute if not exists flash.qty_bklg_si",
                "create attribute if not exists flash.qty_bklg_st",
                "create attribute if not exists flash.qty_hist_cra",
                "create attribute if not exists flash.qty_hist_si",
                "create attribute if not exists flash.qty_hist_st",
                "create attribute if not exists flash.resale_bklg_st",
                "create attribute if not exists flash.resale_hist_st",
                "create attribute if not exists flash.revenue_bklg_cra",
                "create attribute if not exists flash.revenue_bklg_si",
                "create attribute if not exists flash.revenue_bklg_st",
                "create attribute if not exists flash.revenue_hist_cra",
                "create attribute if not exists flash.revenue_hist_si",
                "create attribute if not exists flash.revenue_hist_st",
                "create attribute if not exists flash.revenue_cover_st",
                "create attribute if not exists flash.asp_hist_st",
                "create attribute if not exists flash.asp_hist_si",
                "create attribute if not exists flash.prod_margin_bklg_st",
                "create attribute if not exists pii.person",

                "DROP ROLE IF EXISTS %s" % (role),
                "CREATE ROLE %s WITH GROUPS %s" % (role, testuser),

                """GRANT SELECT ON DATABASE `%s`
                HAVING ATTRIBUTE IN (`flash`.`cogs_bklg_cra`, `flash`.`cogs_bklg_si`, `flash`.`cogs_bklg_st`, `flash`.`cogs_hist_cra`,  `flash`.`cogs_hist_si`, `flash`.`cogs_hist_st`, `flash`.`qty_bklg_cra`, `flash`.`qty_bklg_si`, `flash`.`qty_bklg_st`, `flash`.`qty_hist_cra`, `flash`.`qty_hist_si`, `flash`.`qty_hist_st`, `flash`.`revenue_bklg_cra`, `flash`.`revenue_bklg_si`, `flash`.`revenue_bklg_st`,`flash`.`resale_bklg_st`, `flash`.`revenue_hist_cra`, `flash`.`revenue_hist_si`, `flash`.`revenue_hist_st`, `flash`.`resale_hist_st`, `flash`.`prod_margin_bklg_st`, `flash`.`asp_hist_st`, `flash`.`asp_hist_si`, `flash`.`revenue_cover_st`)
                WHERE ((in_set('ALL', user_attribute('customer_tier')) OR in_set(customer_tier, user_attribute('customer_tier')))
                AND (in_set('ALL', user_attribute('external_markets')) OR in_set(external_markets, user_attribute('external_markets')))
                AND (in_set('ALL', user_attribute('external_markets_alias')) OR in_set(external_markets_alias, user_attribute('external_markets_alias')))
                AND (in_set('ALL', user_attribute('internal_reporting_markets')) OR in_set(internal_reporting_markets, user_attribute('internal_reporting_markets')))
                AND (in_set('ALL', user_attribute('primary_end_markets')) OR in_set(primary_end_markets, user_attribute('primary_end_markets')))
                -- AND (in_set('ALL', user_attribute('prim_sec_end_markets')) OR in_set(primary_secondary_combo, user_attribute('prim_sec_end_markets')))
                AND (in_set('ALL', user_attribute('sub_seg_level1')) OR in_set(sub_seg_level1, user_attribute('sub_seg_level1')))
                AND (in_set('ALL', user_attribute('channel_geography')) OR in_set(channel_geography, user_attribute('channel_geography')))
                AND (in_set('ALL', user_attribute('channel_hier3')) OR in_set(channel_hier3, user_attribute('channel_hier3')))
                AND (in_set('ALL', user_attribute('customer_xu')) OR in_set(customer_xu, user_attribute('customer_xu')))
                AND (in_set('ALL', user_attribute('rep_name')) OR in_set(rep_name, user_attribute('rep_name')))
                AND (in_set('ALL', user_attribute('territory')) OR in_set(territory, user_attribute('territory')))
                -- AND (in_set('ALL', user_attribute('sector')) OR in_set(sector, user_attribute('sector')))
                -- AND (in_set('ALL', user_attribute('area')) OR in_set(area, user_attribute('area')))
                -- AND (in_set('ALL', user_attribute('internal_product_line')) OR in_set(internal_product_line, user_attribute('internal_product_line')))
                )
                TO ROLE `%s`""" % (db, role),

                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE fiscal_quarter  flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE fiscal_quarter_org  flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE fiscal_qtr_std  flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE year_quarter    flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE year_quarter_week   flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE qtr_alias   flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE week_alias  flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE year_alias  flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE fiscal_year flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE channel_distribution_type   flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE channel_direct_type flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE channel_hier3   flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE channel_geography   flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE channel_geo_hier2   flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE channel_distributor_name    flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE part    flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE extnd_product_dppg  flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE extnd_product_device    flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE extnd_product_family    flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE extnd_product_sub_group flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE extnd_product_sub_group_alias   flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE extnd_product_group flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE extnd_product_group_alias   flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE extended_product_header flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE geometry    flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE internal_product_dppg   flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE internal_product_group  flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE internal_product_family flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE internal_product_line   flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE internal_product_division   flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE internal_product_roll_up    flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE part_external   flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE part_pkg_pin    flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE part_grade  flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE part_speed  flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE part_logic_cells    flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE part_node   flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE primary_end_markets flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE primary_secondary_combo flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE secondary_end_markets   flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE external_markets    flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE external_markets_alias  flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE ext_mkt_level1  flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE primary_end_market_alias    flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE internal_reporting_markets  flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE int_mkt_level1  flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE sub_seg_level1  flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE sub_segments    flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE territory   flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE sector  flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE area    flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE region  flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE rep_name    flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE rep_alias   flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE default_territory   flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE default_sector  flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE default_area    flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE default_region  flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE default_rep_name    flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE default_rep_alias   flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE customer_tier   flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE customer_tier_detail    flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE customer_xu flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE customer_gu flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE hub_party   flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE ship_customer_tier  flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE ship_customer_tier_detail   flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE ship_customer_xu    flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE ship_customer_gu    flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE ship_hub_party  flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE scenario    flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE record_type flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE demand_creation_category    flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE demand_creation_category_alias  flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE demand_creation_type    flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE business_type   flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_actual_curr_qtr_backlog flash.measure flash.revenue_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_actual_curr_qtr_backlog flash.measure flash.revenue_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_actual_curr_qtr_backlog flash.measure flash.revenue_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE curr_qtr_actual_delinquency flash.measure flash.revenue_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_allocated_curr_qtr_backlog  flash.measure flash.revenue_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_allocated_curr_qtr_backlog  flash.measure flash.revenue_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_allocated_curr_qtr_backlog  flash.measure flash.revenue_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE curr_qtr_allocated_delinquency  flash.measure flash.revenue_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_1_curr_qtr_backlog  flash.measure flash.revenue_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_2_curr_qtr_backlog  flash.measure flash.revenue_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_3_curr_qtr_backlog  flash.measure flash.revenue_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE curr_qtr_backlog_csd    flash.measure flash.revenue_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_curr_qtr_delinquency  flash.measure flash.revenue_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE curr_qtr_backlog_cfd    flash.measure flash.revenue_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE qtr_plus2_bklg_rev  flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_actual_revenue  flash.measure flash.revenue_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_actual_revenue  flash.measure flash.revenue_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_actual_revenue  flash.measure flash.revenue_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_revenue_adjustments flash.measure flash.revenue_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_revenue_adjustments flash.measure flash.revenue_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_revenue_adjustments flash.measure flash.revenue_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_allocated_revenue   flash.measure flash.revenue_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_allocated_revenue   flash.measure flash.revenue_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_allocated_revenue   flash.measure flash.revenue_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_1_revenue   flash.measure flash.revenue_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_2_revenue   flash.measure flash.revenue_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_3_revenue   flash.measure flash.revenue_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE qtd_revenue flash.measure flash.revenue_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE flash_total_revenue flash.measure flash.revenue_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_actual_curr_qtr_backlog_qty flash.measure flash.qty_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_allocated_curr_qtr_backlog_qty  flash.measure flash.qty_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_actual_curr_qtr_backlog_qty flash.measure flash.qty_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_allocated_curr_qtr_backlog_qty  flash.measure flash.qty_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_actual_curr_qtr_backlog_qty flash.measure flash.qty_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_allocated_curr_qtr_backlog_qty  flash.measure flash.qty_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE curr_qtr_actual_delinquency_qty flash.measure flash.qty_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE curr_qtr_allocated_delinquency_qty  flash.measure flash.qty_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_1_curr_qtr_backlog_qty  flash.measure flash.qty_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_2_curr_qtr_backlog_qty  flash.measure flash.qty_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_3_curr_qtr_backlog_qty  flash.measure flash.qty_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE curr_qtr_backlog_csd_qty    flash.measure flash.qty_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_curr_qtr_delinquency_qty  flash.measure flash.qty_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE curr_qtr_backlog_qty    flash.measure flash.qty_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_actual_curr_qtr_backlog_cogs    flash.cogs_bklg_st flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_allocated_curr_qtr_backlog_cogs flash.cogs_bklg_st flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_actual_curr_qtr_backlog_cogs    flash.cogs_bklg_st flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_allocated_curr_qtr_backlog_cogs flash.cogs_bklg_st flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_actual_curr_qtr_backlog_cogs    flash.cogs_bklg_st flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_allocated_curr_qtr_backlog_cogs flash.cogs_bklg_st flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE curr_qtr_actual_delinquency_cogs    flash.cogs_bklg_st flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE curr_qtr_allocated_delinquency_cogs flash.cogs_bklg_st flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_1_curr_qtr_backlog_cogs flash.cogs_bklg_st flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_2_curr_qtr_backlog_cogs flash.cogs_bklg_st flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_3_curr_qtr_backlog_cogs flash.cogs_bklg_st flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE curr_qtr_backlog_csd_cogs   flash.cogs_bklg_st flash.measure pii.person" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_curr_qtr_delinquency_cogs flash.cogs_bklg_st flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE curr_qtr_backlog_cogs   flash.cogs_bklg_st flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_actual_qty  flash.measure flash.qty_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_allocated_qty   flash.measure flash.qty_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_adjustments_qty flash.measure flash.qty_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_actual_qty  flash.measure flash.qty_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_allocated_qty   flash.measure flash.qty_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_adjustments_qty flash.measure flash.qty_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_actual_qty  flash.measure flash.qty_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_allocated_qty   flash.measure flash.qty_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_adjustments_qty flash.measure flash.qty_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_1_qty   flash.measure flash.qty_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_2_qty   flash.measure flash.qty_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_3_qty   flash.measure flash.qty_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE qtd_qty flash.measure flash.qty_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE flash_total_qty flash.measure flash.qty_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_actual_cogs flash.cogs_hist_st flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_allocated_cogs  flash.cogs_hist_st flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_adjustments_cogs    flash.cogs_hist_st flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_actual_cogs flash.cogs_hist_st flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_allocated_cogs  flash.cogs_hist_st flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_adjustments_cogs    flash.cogs_hist_st flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_actual_cogs flash.cogs_hist_st flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_allocated_cogs  flash.cogs_hist_st flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_adjustments_cogs    flash.cogs_hist_st flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_1_cogs  flash.cogs_hist_st flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_2_cogs  flash.cogs_hist_st flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_3_cogs  flash.cogs_hist_st flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE qtd_cogs    flash.cogs_hist_st flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE flash_total_cogs    flash.cogs_hist_st flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE qtr_plus2_bklg_qty  flash.measure flash.qty_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE qtr_plus2_bklg_cogs flash.cogs_bklg_st flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_actual_curr_qtr_backlog_cra flash.measure flash.revenue_bklg_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_actual_curr_qtr_backlog_cra flash.measure flash.revenue_bklg_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_actual_curr_qtr_backlog_cra flash.measure flash.revenue_bklg_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE qtr_plus2_bklg_rev_cra  flash.measure flash.revenue_bklg_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_allocated_curr_qtr_backlog_cra  flash.measure flash.revenue_bklg_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_allocated_curr_qtr_backlog_cra  flash.measure flash.revenue_bklg_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_allocated_curr_qtr_backlog_cra  flash.measure flash.revenue_bklg_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_1_curr_qtr_backlog_cra  flash.measure flash.revenue_bklg_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_2_curr_qtr_backlog_cra  flash.measure flash.revenue_bklg_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_3_curr_qtr_backlog_cra  flash.measure flash.revenue_bklg_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE curr_qtr_backlog_csd_cra    flash.measure flash.revenue_bklg_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE curr_qtr_backlog_cra    flash.measure flash.revenue_bklg_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_actual_revenue_cra  flash.measure flash.revenue_hist_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_actual_revenue_cra  flash.measure flash.revenue_hist_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_actual_revenue_cra  flash.measure flash.revenue_hist_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_revenue_adjustments_cra flash.measure flash.revenue_hist_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_revenue_adjustments_cra flash.measure flash.revenue_hist_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_revenue_adjustments_cra flash.measure flash.revenue_hist_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_1_revenue_cra   flash.measure flash.revenue_hist_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_2_revenue_cra   flash.measure flash.revenue_hist_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_3_revenue_cra   flash.measure flash.revenue_hist_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE qtd_revenue_cra flash.measure flash.revenue_hist_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE flash_total_revenue_cra flash.measure flash.revenue_hist_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE curr_qtr_backlog_sell_in    flash.measure flash.revenue_bklg_si" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE qtd_revenue_sell_in flash.measure flash.revenue_hist_si" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE flash_total_sell_in flash.measure flash.revenue_hist_si" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE actual_curr_qtr_backlog flash.measure flash.revenue_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE allocated_curr_qtr_backlog  flash.measure flash.revenue_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE curr_qtr_backlog_actual_and_allocation  flash.measure flash.revenue_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE adjustment  flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_actual_curr_qtr_backlog_qty_cra flash.measure flash.qty_bklg_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_actual_curr_qtr_backlog_qty_cra flash.measure flash.qty_bklg_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_actual_curr_qtr_backlog_qty_cra flash.measure flash.qty_bklg_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE qtr_plus2_bklg_qty_cra  flash.measure flash.qty_bklg_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_allocated_curr_qtr_backlog_qty_cra  flash.measure flash.qty_bklg_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_allocated_curr_qtr_backlog_qty_cra  flash.measure flash.qty_bklg_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_allocated_curr_qtr_backlog_qty_cra  flash.measure flash.qty_bklg_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_1_curr_qtr_backlog_qty_cra  flash.measure flash.qty_bklg_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_2_curr_qtr_backlog_qty_cra  flash.measure flash.qty_bklg_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_3_curr_qtr_backlog_qty_cra  flash.measure flash.qty_bklg_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE curr_qtr_backlog_csd_qty_cra    flash.measure flash.qty_bklg_cra pii.person" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE curr_qtr_backlog_qty_cra    flash.measure flash.qty_bklg_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_actual_qty_cra  flash.measure flash.qty_hist_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_actual_qty_cra  flash.measure flash.qty_hist_cra pii.person" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_actual_qty_cra  flash.measure flash.qty_hist_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_adjustments_qty_cra flash.measure flash.qty_hist_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_adjustments_qty_cra flash.measure flash.qty_hist_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_adjustments_qty_cra flash.measure flash.qty_hist_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_1_qty_cra   flash.measure flash.qty_hist_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_2_qty_cra   flash.measure flash.qty_hist_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_3_qty_cra   flash.measure flash.qty_hist_cra pii.person" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE qtd_qty_cra flash.measure flash.qty_hist_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE flash_total_qty_cra flash.measure flash.qty_hist_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE curr_qtr_backlog_qty_sell_in    flash.measure flash.qty_bklg_si" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE qtd_qty_sell_in flash.measure flash.qty_hist_si" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE flash_total_qty_sell_in flash.measure flash.qty_hist_si" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_actual_curr_qtr_backlog_cogs_cra    flash.cogs_bklg_cra flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_actual_curr_qtr_backlog_cogs_cra    flash.cogs_bklg_cra flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_actual_curr_qtr_backlog_cogs_cra    flash.cogs_bklg_cra flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE qtr_plus2_bklg_cogs_cra flash.cogs_bklg_cra flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_allocated_curr_qtr_backlog_cogs_cra flash.cogs_bklg_cra flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_allocated_curr_qtr_backlog_cogs_cra flash.cogs_bklg_cra flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_allocated_curr_qtr_backlog_cogs_cra flash.cogs_bklg_cra flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_1_curr_qtr_backlog_cogs_cra flash.cogs_bklg_cra flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_2_curr_qtr_backlog_cogs_cra flash.cogs_bklg_cra flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_3_curr_qtr_backlog_cogs_cra flash.cogs_bklg_cra flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE curr_qtr_backlog_csd_cogs_cra   flash.cogs_bklg_cra flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE curr_qtr_backlog_cogs_cra   flash.cogs_bklg_cra flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_actual_cogs_cra flash.cogs_hist_cra flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_actual_cogs_cra flash.cogs_hist_cra flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_actual_cogs_cra flash.cogs_hist_cra flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_adjustments_cogs_cra    flash.cogs_hist_cra flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_adjustments_cogs_cra    flash.cogs_hist_cra flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_adjustments_cogs_cra    flash.cogs_hist_cra flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_1_cogs_cra  flash.cogs_hist_cra flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_2_cogs_cra  flash.cogs_hist_cra flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_3_cogs_cra  flash.cogs_hist_cra flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE qtd_cogs_cra    flash.cogs_hist_cra flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE flash_total_cogs_cra    flash.cogs_hist_cra flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE curr_qtr_backlog_cogs_sell_in   flash.cogs_bklg_si flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE qtd_cogs_sell_in    flash.cogs_hist_si flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE flash_total_cogs_sell_in    flash.cogs_hist_si flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_actual_curr_qtr_backlog_resale  flash.measure flash.resale_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_actual_curr_qtr_backlog_resale  flash.measure flash.resale_bklg_st pii.person" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_actual_curr_qtr_backlog_resale  flash.measure flash.resale_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE curr_qtr_actual_delinquency_resale  flash.measure flash.resale_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_allocated_curr_qtr_backlog_resale   flash.measure flash.resale_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_allocated_curr_qtr_backlog_resale   flash.measure flash.resale_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_allocated_curr_qtr_backlog_resale   flash.measure flash.resale_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE curr_qtr_allocated_delinquency_resale   flash.measure flash.resale_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_1_curr_qtr_backlog_resale   flash.measure flash.resale_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_2_curr_qtr_backlog_resale   flash.measure flash.resale_bklg_st pii.person" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_3_curr_qtr_backlog_resale   flash.measure flash.resale_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE curr_qtr_backlog_resale_csd flash.measure flash.resale_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_curr_qtr_delinquency_resale   flash.measure flash.resale_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE curr_qtr_backlog_resale flash.measure flash.resale_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE qtr_plus2_bklg_res  flash.measure" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_actual_resale   flash.measure flash.resale_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_actual_resale   flash.measure flash.resale_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_actual_resale   flash.measure flash.resale_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_resale_adjustments  flash.measure flash.revenue_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_resale_adjustments  flash.measure flash.revenue_hist_st pii.person" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_resale_adjustments  flash.measure flash.revenue_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_1_allocated_resale    flash.measure flash.resale_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_2_allocated_resale    flash.measure flash.resale_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE month_3_allocated_resale    flash.measure flash.resale_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_1_resale    flash.measure flash.resale_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_2_resale    flash.measure flash.resale_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE total_month_3_resale    flash.measure flash.resale_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE qtd_resale  flash.measure flash.resale_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE flash_total_resale  flash.measure flash.resale_hist_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE flash_total_revenue_qtr_ago flash.measure flash.revenue_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE flash_total_revenue_cra_qtr_ago flash.measure flash.revenue_bklg_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE flash_total_sell_in_qtr_ago flash.measure flash.revenue_bklg_si" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE flash_total_revenue_qtr_ago_turns   flash.measure flash.revenue_bklg_st" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE flash_total_revenue_cra_qtr_ago_turns   flash.measure flash.revenue_bklg_cra" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE flash_total_sell_in_qtr_ago_turns   flash.measure flash.revenue_bklg_si" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE dm_time_key flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE dm_part_key flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE dm_geography_key    flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE dm_channel_key  flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE dm_cust_key_disti   flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE dm_cust_key_end flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE dm_city_key flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE dm_cust_key_end_xcm flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE dm_city_key_xcm flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE dm_sales_hierarchy_key  flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE dm_mkt_seg_key  flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE dm_default_sales_hierarchy_key  flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE dm_cust_key_ship_xcm    flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE dm_business_type_key    flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE dm_demand_creation_key  flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE flag_14_week    flash.dimension" % (db, tbl1),
                "ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE week_no flash.dimension" % (db, tbl1),
            ]

            print("Creating environment with DDLs")
            start = time.time()
            for ddl in ddls:
                conn.execute_ddl(ddl)
            end = time.time()
            print("Done creating environment with DDLs: %s seconds" % (end-start))

        # We put the query on a separate connection as it makes debugging the logs
        # a bit easier.
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            ctx.enable_token_auth(token_str=testuser)

            print("Executing query")
            start = time.time()
            conn.scan_as_json('select * from %s.%s' % (db, tbl1))
            end = time.time()
            print("Done query: %s seconds" % (end-start))