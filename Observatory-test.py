# -*- coding:utf-8 -*-
"""
@Description :     9-day forecast test
@version:          V1.0
@Date:             2020/0/29
@Author:           huxuebing
@Desc: python version: 3.6+
       need install uiautomator2 
       github: https://github.com/openatx/uiautomator2
       execute in cmd interface : pip install --upgrade --pre uiautomator2
       Connect the phone to execute in cmd interface : python -m uiautomator2 init
       device: meizu pro6 android 7.1.1
       ATX is adopted because the framework is relatively easy to deploy, has fast operation efficiency, low learning cost, and less debugging and writing time.
"""

import time
import datetime  
import unittest

import uiautomator2 as u2

class DayForecastTest(unittest.TestCase):
        #Run before whole testcase set execution, decorator classmethod is essential
    def __init__(self,*args,**kwargs):
        unittest.TestCase.__init__(self,*args,**kwargs)
        #device id or device ip
        self.d = u2.connect('192.168.0.106')

    def setUp(self):
        self.d.app_stop("hko.MyObservatory_v1_0") 
        time.sleep(1)
        self.d.app_start("hko.MyObservatory_v1_0")
        time.sleep(8)

    def tearDown(self):
        self.d.app_stop("hko.MyObservatory_v1_0") 

    def test_all(self):
        #check date/temperature/humidity/wind power
        self.d(description="转到上一层级").click()
        time.sleep(1)
        self.d.swipe(201,1592,201,537)
        time.sleep(1)
        self.d(resourceId="hko.MyObservatory_v1_0:id/text", text="9-Day Forecast").click()
        time.sleep(5)
        print(self.d(resourceId="hko.MyObservatory_v1_0:id/mainAppSevenDayGenSit").info['text'])
        today = datetime.date.today() 
        for i in range(8):
            tomorrow = today + datetime.timedelta(days = 1) 
            today = tomorrow
            print(tomorrow.strftime("%d %b %a"))
            print(self.d(resourceId="hko.MyObservatory_v1_0:id/sevenday_forecast_date").info['text'])
            #check date
            self.assertIn(self.d(resourceId="hko.MyObservatory_v1_0:id/sevenday_forecast_date").info['text'],tomorrow.strftime("%d %b"))
            self.assertIn(tomorrow.strftime("%a"),self.d(resourceId="hko.MyObservatory_v1_0:id/sevenday_forecast_day_of_week").info['text'])
            #check temperature
            self.assertIn("°C",self.d(resourceId="hko.MyObservatory_v1_0:id/sevenday_forecast_temp").info['text'])
            #check humidity
            self.assertIn("%",self.d(resourceId="hko.MyObservatory_v1_0:id/sevenday_forecast_rh").info['text'])
            #check wind power
            self.assertIn("force",self.d(resourceId="hko.MyObservatory_v1_0:id/sevenday_forecast_wind").info['text'])

            self.d.swipe(417,1180,417,805)
            time.sleep(1)
        # check other day
        tomorrow = today + datetime.timedelta(days = 1) 
        print(tomorrow.strftime("%d %b %a"))
        print(self.d(resourceId="hko.MyObservatory_v1_0:id/sevenday_forecast_date",instance=1).info['text'])
        #check date
        self.assertIn(self.d(resourceId="hko.MyObservatory_v1_0:id/sevenday_forecast_date",instance=1).info['text'],tomorrow.strftime("%d %b"))
        self.assertIn(tomorrow.strftime("%a"),self.d(resourceId="hko.MyObservatory_v1_0:id/sevenday_forecast_day_of_week",instance=1).info['text'])
        #check temperature
        self.assertIn("°C",self.d(resourceId="hko.MyObservatory_v1_0:id/sevenday_forecast_temp",instance=1).info['text'])
        #check humidity
        self.assertIn("%",self.d(resourceId="hko.MyObservatory_v1_0:id/sevenday_forecast_rh",instance=1).info['text'])
        #check wind power
        self.assertIn("force",self.d(resourceId="hko.MyObservatory_v1_0:id/sevenday_forecast_wind",instance=1).info['text'])
        #check text is not null
        self.assertIsNotNone(self.d(resourceId="hko.MyObservatory_v1_0:id/mainAppSevenDayGenSit").info['text'])


if __name__=='__main__':
    unittest.main()