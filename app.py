"""
核心:api+case+data
api:封装请求相关业务(使用requests向服务器发送请求)

case:封 装unittest相关实现(调用api的请求的业务,参数化调用data中的测试数据,自身还需要实现断言业务)

data:封装测试数据(一般使用json文件)

测试报告:report+tools+run_suite.py
report:保存生成的测试报告
tools:存储第三方工具
run_suite.py:组织测试套件

全局文件:app.py
app.py 封装程序中常量/全局变量/工具方法...




"""
#封装不同接口中URL相同的前缀(协议+域名)
import os

BASE_URL = "http://localhost/"
# wenjian = os.getcwd()
# print(wenjian)
file_path = os.path.abspath(__file__)
pro_path = os.path.dirname(file_path)
print(file_path)
print(pro_path)