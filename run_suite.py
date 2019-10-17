import unittest

import time
from HTMLTestRunner import HTMLTestRunner

from case.test_TPShop import TestTPShop

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestTPShop))
file_to = "./report/{}_report.html".format(time.strftime("%Y%m%d%H%M%S"))
with open(file_to,"wb") as f:
    runner = HTMLTestRunner(f,title="张倩的",description="v1.0")
    runner.run(suite)