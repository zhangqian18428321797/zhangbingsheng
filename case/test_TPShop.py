# 1.导包
import json
import unittest
import requests

# 2.创建测试类
from parameterized import parameterized
from api.user_api import UserLogin
def read_json():
    data = []

    with open("D:\张倩\软件测试的代码和Python的代码\jiekou_06\data\login_data.json",'r',encoding="utf-8") as f:
        w_data = json.load(f)
        for value in w_data.values():
            data.append((
                value.get("username"),
                value.get("password"),
                value.get("verify_code"),
                value.get("status"),
                value.get("msg")
            ))


    return data


class TestTPShop(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()
        self.user_obj = UserLogin()

    def tearDown(self):
        self.session.close()

    def test_get_verify_code(self):
        resopnes = self.user_obj.get_verify_code(self.session)
        self.assertIn("png", resopnes.headers.get("Content-Type"))
        self.assertEqual(200, resopnes.status_code)

    @parameterized.expand(read_json())
    def test_login(self, username, password, verify_code, status, msg):
        print(username, password, verify_code, status, msg)
        resopnes1 = self.user_obj.get_verify_code(self.session)
        resopnes2 = self.user_obj.go_login(self.session, username, password, verify_code)
        print(resopnes2.json())
        self.assertIn(msg,resopnes2.json().get("msg"))
        self.assertEqual(status, resopnes2.json().get("status"))

