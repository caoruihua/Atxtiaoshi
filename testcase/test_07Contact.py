# coding: utf-8
import unittest
import uiautomator2 as u2
import time
import uiautomator2.ext.htmlreport as htmlreport
import loger



class TestXiaobaiban(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.u = u2.connect_usb()
        cls.u.healthcheck()  # 解锁屏幕并启动uiautomator服务
        hrp = htmlreport.HTMLReport(cls.u, 'report')
        hrp.patch_click()
        cls.u.make_toast("测试开始")
        # cls.u.disable_popups(True)  # 允许自动处理弹出框

    @classmethod
    def tearDownClass(cls):
        cls.u.make_toast("测试结束", 3)
        cls.u.app_stop_all()
        cls.u.service(
            "uiautomator").stop()  # 停止uiautomator守护程序，允许其他测试框架如 appium 运行

    def setUp(self):
        self.log=loger.log_message()
        self.d = self.u.session("com.esenyun.workline")  # restart app
        time.sleep(5)  # 等待首页广告结束

    def tearDown(self):
        pass




    def test02RizhiAndShenpi(self):
        self.log.info_log("查看小白板日志测试")
        time.sleep(3)
        self.d(text=u"我的小白板").click()
        time.sleep(1)
        self.d(text=u"冷藏库开辟市场参考").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/title_iv_right02").click()
        time.sleep(1)
        self.d.swipe(0.729, 0.751,0.645, 0.326,0.5)
        time.sleep(1)
        self.d(text=u"查看日志").click() #进入查看小白板日志界面
        time.sleep(1)
        self.d.swipe(0.729, 0.751, 0.645, 0.326, 0.5)
        time.sleep(1)
        self.d.press("back")
        time.sleep(1)
        self.log.info_log("查看小白板日志测试完成")
        time.sleep(1)
        self.log.info_log("审批测试开始")
        self.d(resourceId="com.esenyun.workline:id/title_iv_right02").click()
        time.sleep(1)
        self.d(text=u"发起审批").click()
        time.sleep(3)
        self.d.click(0.505, 0.847)
        time.sleep(1)
        self.d.click(0.513, 0.205)
        time.sleep(3)
        self.d(text=u"adsaf").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/tv_confirm").click()
        time.sleep(1)
        self.d.click(0.561, 0.836)
        time.sleep(1)
        self.assertTrue(self.d(text=u"点赞").exists,"审批失败")
        time.sleep(1)
        self.log.info_log("审批测试通过")











if __name__ == '__main__':
        unittest.main()
