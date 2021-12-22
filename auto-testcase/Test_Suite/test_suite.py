#coding=utf-8
import sys
sys.path.append('E:\\Program Files\\web自动化测试用例\\auto-testcase')

from TestCase.login import TestRun
import unittest
from selenium import webdriver
import os
import HTMLTestRunner


if __name__ == "__main":
    suite = unittest.TestSuite()
    suite.addTest(TestRun("test_login"))
    runner = unittest.TextTestRunner()
    runner.run(suite)



# def get_suite():
#     suite = unittest.TestSuite()
#     tests = []
#     loader = unittest.TestLoader()
#     suite.addTests(loader.loadTestsFromTestCase())
#
#     return suite


