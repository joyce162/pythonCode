import pytest
import allure
from common.readYaml import ReadYaml
from common.recordLog import log
from base.apiUtils import BaseRequestUtil

@allure.feature('物流')
class TestLogistic(object):
   get_material_case_info = ReadYaml().get_testcase_from_yaml('./testcase/Logistic/getMaterial.yml')
   shipper_create_oder_case_info = ReadYaml().get_testcase_from_yaml('./testcase/Logistic/shipperCreateOrder.yml')
   corp_receive_order_case_info = ReadYaml().get_testcase_from_yaml('./testcase/Logistic/corpReceiveOrder.yml')
   corp_assign_order_case_info = ReadYaml().get_testcase_from_yaml('./testcase/Logistic/corpAssignOrder.yml')
   carrier_receive_order_case_info = ReadYaml().get_testcase_from_yaml('./testcase/Logistic/carrierReceiveOrder.yml')

   @pytest.mark.parametrize('baseInfo,testcase', get_material_case_info)
   @allure.story('获取下单物料信息')
   def test_get_material(self, baseInfo,testcase):
       allure.dynamic.title(testcase['case_name'])
       BaseRequestUtil().specification_yaml(baseInfo,testcase)

   @pytest.mark.parametrize('baseInfo,testcase', shipper_create_oder_case_info)
   @allure.story('货主（托运人）下订单')
   def test_shipper_create_order(self, baseInfo, testcase):
       allure.dynamic.title(testcase['case_name'])
       BaseRequestUtil().specification_yaml(baseInfo, testcase)

   @pytest.mark.parametrize('baseInfo,testcase', corp_receive_order_case_info)
   @allure.story('集团接收货主订单')
   def test_corp_receive_order(self, baseInfo, testcase):
       allure.dynamic.title(testcase['case_name'])
       BaseRequestUtil().specification_yaml(baseInfo, testcase)

   @pytest.mark.parametrize('baseInfo,testcase', corp_assign_order_case_info)
   @allure.story('集团分配订单给物流公司')
   def test_corp_assign_order(self, baseInfo, testcase):
       allure.dynamic.title(testcase['case_name'])
       BaseRequestUtil().specification_yaml(baseInfo, testcase)

   @pytest.mark.parametrize('baseInfo,testcase', carrier_receive_order_case_info)
   @allure.story('物流公司接单')
   def test_carrier_receive_order(self, baseInfo, testcase):
       allure.dynamic.title(testcase['case_name'])
       BaseRequestUtil().specification_yaml(baseInfo, testcase)