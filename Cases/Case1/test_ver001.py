#coding:utf-8
import subprocess
import time
import unittest
import uiautomator2 as ut2
import uiautomator2.ext.htmlreport as htmlreport
import sys
sys.path.append('../../')
from Public.HTMLTestReportCN import DirAndFiles

class ver001():
    def __init__(self,apkname,device):
        self.apkname = apkname
        self.d = device
    
    def __del__(self):
        self.apkname = None
        self.d = None

    def installAPK(self):
        installdict = ['adb','install',self.apkname]
        recode = subprocess.call(installdict)
        if recode == 0:
            return True
        else:
            return False

class case001(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.device = ut2.connect()
        self.hrp = htmlreport.HTMLReport(self.device,'Report/'+self.__name__)
        self.hrp.patch_click()
        self.testVer = ver001("Apk/test.apk",self.device)
        self.daf = DirAndFiles()

    @classmethod
    def tearDownClass(self):
        self.device = None
        self.testVer = None
        self.hrp.unpatch_click()
        self.hrp = None
    
    def test_01_xxx(self):
        try:
            self.testVer.installAPK()
        except:
            self.daf.get_screenshot(self.device)
            raise

    def test_02_siminfo(self):
        pass


if __name__ == "__main__":
    print "Test"