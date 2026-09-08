import os.path

import allure
import pytest
from common.readYaml import ReadYaml
from base.apiUtils import BaseRequestUtil


@allure.feature('商品管理')
class TestProduct(object):
    product_list_case_info = ReadYaml().get_testcase_from_yaml('./testcase/ProductManage/getProductListTestcase.yml')
    product_detail_case_info = ReadYaml().get_testcase_from_yaml('./testcase/ProductManage/getProductDetailTestcase.yml')

    @pytest.mark.parametrize('params', product_list_case_info)
    @allure.story('获取商品列表')
    def test_product_list(self, params):
        BaseRequestUtil().specification_yaml(params)

    @pytest.mark.parametrize('params', product_detail_case_info)
    @allure.story('获取商品详情')
    def test_product_detail(self, params):
        BaseRequestUtil().specification_yaml(params)
