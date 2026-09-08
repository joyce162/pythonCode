import pytest
import os
import  shutil

if __name__ == '__main__':
    # pytest.main(['-vs','./testcase','-m','smoke'])

    pytest.main(['-vs', './testcase/Login/test_login.py'])

    # pytest.main(['-vs', './testcase/ProductManage/test_productManage.py'])
    # pytest.main([''])
    #因每次/report/temp文件夹的所有文件都会被清除，所以必须copy环境文件
    shutil.copy('./enviroment.xml','./report/temp')
    # 生成静态html报告
    os.system("allure generate ./report/temp -c -o ./report/allure-report")
    # 打开浏览器
    os.system("allure open ./report/allure-report")
