#coding:utf-8
import unittest
import os
import datetime
from Public import HTMLTestRunner
from Public import HTMLTestReportCN

def discover_case(case_dir):
    # 扫描用例目录
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,pattern="*.py",top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testcase.addTests(test_case)
    return(testcase)

if __name__ == "__main__":
    path = os.path.join(os.getcwd(), "Cases")
    cases = discover_case(case_dir=path)
    #运行并生成报告
    daf = HTMLTestReportCN.DirAndFiles()
    daf.create_dir(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
    #HTMLFile = "Report/"+datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+"_testResult.html"
    report_path = HTMLTestReportCN.GlobalMsg.get_value("report_path")
    fp = file(report_path,'wb')
    runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,title=u'UI测试',description=u'result')
    runner.run(cases)
    fp.close()