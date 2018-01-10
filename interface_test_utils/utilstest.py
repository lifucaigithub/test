#coding:utf-8
import base64
import hashlib
import json
import os
import random
import ssl
import sys
import time
import types
import thread
from Crypto.Cipher import AES
import httplib2
import requests
from interface_test_utils.get_token import GetToken
import datetime
from interface_test_utils.changeOrderStatus import ChangeOrderStatus
from urllib import urlencode, quote
import random
reload(sys)
sys.setdefaultencoding('utf-8')


class utils():
    APPSECRET = '20c079d77bd0c11c60c8f1d603f7f1db'
    APPKEY = '47a7ccefe0'
    BASEURL = 'http://test.truckmanager.g7s.chinawayltd.com/app.php?'
    BASEURL1 = 'https://line2.truckmanager.g7s.huoyunren.com/app.php?'
    MALLBASEURL='http://test.mall.g7s.chinawayltd.com/g7api/'
    arr=[0,0,0,0,0]
    flag = False
    #原始参数拼接为字典
    def string(self, data):
        d = {}
        # process = unquote(data.replace(' ', ''))
        if data.startswith('[{\"longitude\"') or data.startswith('settings={') or data.startswith('message') or data.startswith('gpsnos') or data.startswith('uid'):
            original = data.replace(' ', '').split('*')
        else:
            original = data.replace(' ', '').split(';')
            # print original
        map(lambda x: d.setdefault(x.split('=')[0], x.split('=')[1]), original)
        # print '######',d
        return d

    def string1(self, data):
        d = {}
        # process = unquote(data.replace(' ', ''))
        if data.startswith('[{\"longitude\"') or data.startswith('settings={') or data.startswith('message') or data.startswith('gpsnos') or data.startswith('uid'):
            original = data.replace(' ', '').split('*')
        else:
            original = data.replace(' ', '').split(',')
            # print original
        map(lambda x: d.setdefault(x.split('=')[0], x.split('=')[1]), original)
        # print '######',d
        return d

    #计算校验码
    def code(self, dict):
        value = ''
        key = dict.keys()
        for k in sorted(key):
            value += dict[k]
        key = value + self.APPSECRET
        print 'key is', key
        m = hashlib.md5()
        m.update(key)
        psw = m.hexdigest()
        #print psw
        return psw

    #第三方接口调用的校验码
    def third_code(self, d):

        d['signTime'] = int(d['signTime'])
        m = hashlib.md5()
        j = json.dumps(d, sort_keys=True).decode('unicode_escape').replace(' ', '')
        print 'j is ', j
        m.update(j)
        psw = m.hexdigest()
        #print psw
        return psw

    #没有参数的时候的校验码计算
    def no_data_code(self):
        m = hashlib.md5()
        m.update(self.APPSECRET)
        psw = m.hexdigest()
        #print psw
        return psw
        #拼接测试参数
    def get_token(self, ENV, username):
        getToken = GetToken()

        if 'demo' in ENV:
            url = self.MALLBASEURL.replace('test', 'demo')
        else:
            url = self.MALLBASEURL
        if url.startswith('http://demo'):
            token = getToken.get_demo_token(username)
        else:
            token =  getToken.get_test_token(username)
            #print url
        return token
        #拼接测试参数
    def create_parameter(self, ENV, method, data, username):
        getToken = GetToken()

        if 'demo' in ENV:
            url = self.MALLBASEURL + method
        else:
            url = self.MALLBASEURL.replace('demo', 'test') + method
        if url.startswith('http://demo'):
            token = '&token=' + getToken.get_demo_token(username)
        else:
            token = '&token=' + getToken.get_test_token(username)
        if len(data) == 0:
            cc = '&code=' + self.no_data_code()
            post = url + 'appkey=' + self.APPKEY + cc + token
            print post
        else:
            cc = '&code=' + self.code(self.string(data))
            p = self.string(data)
            para = ''
            for k in p.keys():
                para += k + '=' + p[k] + '&'
            if method.find('login') == '0':
                post = url + para + 'appkey=' + self.APPKEY + cc
                print post
            else:
                post = url + para + 'appkey=' + self.APPKEY + cc + token
                print post
        return post

    def create_parameter1(self, ENV, method,data,username):
        getToken = GetToken()

        if 'demo' in ENV:
            url = self.MALLBASEURL
        else:
            url = self.MALLBASEURL.replace('demo', 'test')
        if url.startswith('http://demo'):
            token = '&token=' + getToken.get_demo_token(username)
        else:
            token = '&token=' + getToken.get_test_token(username)
        if len(data) == 0:
            cc = '&code=' + self.no_data_code()
            post = url + 'appkey=' + self.APPKEY + cc + token
            print post
        else:
            cc = '&code=' + self.code(self.string(data))
            p = self.string(data)
            para = ''
            for k in p.keys():
                para += k + '=' + p[k] + '&'
            if method.find('login') == '0':
                post = url + para + 'appkey=' + self.APPKEY + cc
                print post
            else:
                post = url + para + 'appkey=' + self.APPKEY + cc + token
                print post
        return post

    #第三方接口调用
    def third_create_parameter(self, ENV, method, data):
        #ETC 83c3d502f183b4dd 02d4ea925213210c3e1f8a6013bce6b7
        #OILCARD 8ef39525e7d126c7 ca79770ee66317b3eaa872b48d0147f7
        #管车 47a7ccefe0 20c079d77bd0c11c60c8f1d603f7f1db
        #招采 844937e502bec18e  bc4b6a10bf6ee6e6ffbf66f3a0813fa4
        base_url = 'http://test.mall.g7s.chinawayltd.com/g7api/'
        signTime = int(time.time())
        m = 'method=' + method + '&'
        if 'demo' in ENV:
            url = base_url + m
        else:
            url = base_url.replace('demo', 'test') + m
        print 'url is', url
        appkey = '279d66290140f16a1899a6f416387ccf'
        appSecret = '71b80faca8c0d8daf1fdccbd390cd111'
        print 'data is', data

        orin = self.string(data + ';signTime=%d' % signTime + ';appkey=%s' % appkey + ';appSecret=%s' % appSecret + ';method=%s' % method)
        print 'orin is', orin
        cc = 'sign=' + self.third_code(orin)
        # print cc
        p = self.string(data)
        p['signTime'] = str(signTime)
        p['appkey'] = appkey
        para = ''
        for k in p.keys():
            para += k + '=' + p[k] + '&'
        post = url + para + cc
        post = post.replace('\\', '')
        print post
        return post

    def gsp2_create_url(self, ENV, method):
        base_url = 'http://demo.mall.g7s.chinawayltd.com/g7api/'
        signTime = int(time.time())
        if 'demo' in ENV:
            url = base_url + method
        else:
            url = base_url.replace('demo', 'test') + method
        print 'url is', url
        return url
        #第三方接口调用
    def gsp2_create_parameter(self, ENV, data):
        signTime = int(time.time())
        appkey = '279d66290140f16a1899a6f416387ccf'
        appSecret = '71b80faca8c0d8daf1fdccbd390cd111'
        print 'data is', data

        orin = self.string(data + ';signTime=%d' % signTime + ';appKey=%s' % appkey + ';appSecret=%s' % appSecret)
        print 'orin is', orin
        cc = self.third_code(orin)
        # print cc
        p = self.string(data)
        print  'p is', p
        ds = str(p).replace('\\','')
        print  'ds is', ds
        ps =eval(ds)

        #orderStatusList='[{"orderStatus" : "1", "modifyTime":"1494928450", "remark":"","codPayStatus" : "1","expressCompany" : "", "logisticsNo" : "","workOrderStatus" : "1","engineerName":"","engineerMobile" : "","installTime" : "1494928452","installAddress" : ""}]'
        ps['signTime'] = str(signTime)
        ps['appKey'] = appkey
        ps['sign'] = cc
        print 'ps is', ps
        return ps

    def post_order(self, method, payload):
        session = requests.Session()
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/' + method
        print url
        data = self.string(payload)
        print  data
        r = session.post(url, data=data)
        print r.text.decode('unicode_escape')
        ecsid =  r.cookies['ecsid']
        cookies = {'ecsid':ecsid}
        url1 = 'http://test.mall.g7s.chinawayltd.com/g7api/flow/consignee'
        data1 = self.string('name=四道口黄河,mobile=18888888888,provinceCode=21344,cityCode=234677,address=天府四街199号')
        r1 = session.post(url1, data=data1)
        print r1.text.decode('unicode_escape')
        url2 = 'http://test.mall.g7s.chinawayltd.com/g7api/flow/checkout?'
        content = session.get(url2, cookies = cookies)
        print content.text.decode('unicode_escape')
        ##########续费接口
    def renew_info(self, method,username):
        token = self.get_token('test',username)
        #session = requests.Session()
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method+'?token='+token
        print url
        r = requests.get(url)
        print r.text.decode('unicode_escape')

    def banner_list(self, method,positionCode ,username):
        session = requests.Session()
        token = self.get_token('test',username)
        url1 = 'http://test.mall.g7s.chinawayltd.com/g7api/category'+'?token='+token
        print url1
        resp1 = session.get(url1)
        ecsid =  resp1.cookies['ecsid']
        cookies = {'ecsid':ecsid}
        print resp1.text.decode('unicode_escape')
        url2='http://test.mall.g7s.chinawayltd.com/g7api/goods/200?token='+ token
        print url2
        resp2 = session.get(url2,cookies=cookies)
        print resp2.text.decode('unicode_escape')
        url3 = 'http://test.mall.g7s.chinawayltd.com/g7api/flow/add?token='+token
        data1 = 'goodsId=200,number=1'
        data = self.string1(data1)
        print url3
        resp3 = session.post(url3,data=data,cookies=cookies)
        print resp3.text.decode('unicode_escape')
        url4 = 'http://test.mall.g7s.chinawayltd.com/g7api/flow/consignee?token='+token
        print url4
        resp4 = session.get(url4,cookies=cookies)
        print resp4.text.decode('unicode_escape')
        url5 = 'http://test.mall.g7s.chinawayltd.com/g7api/flow/consignee?token='+token
        print url5
        data2 = 'name=lfc123,mobile=13730645598,provinceCode=310000000000,cityCode=310000000000,districtCode=310101000000,address=上海路22号'
        dataaddress= self.string1(data2)
        resp5 = session.post(url5,data=dataaddress,cookies=cookies)
        print resp5.text.decode('unicode_escape')
        url6= 'http://test.mall.g7s.chinawayltd.com/g7api/flow/checkout?token='+token
        print url6
        resp6 = session.get(url6,cookies=cookies)
        print resp6.text.decode('unicode_escape')
        url7 = 'http://test.mall.g7s.chinawayltd.com/g7api/flow/submit?token='+token
        datapay='payId=6'
        payId= self.string1(datapay)
        print url7
        resp7 = session.post(url7,cookies=cookies,data=payId)
        print resp7.text.decode('unicode_escape')
        d = json.loads(resp7.text)
        orderSn = d['data']['orderSn']
        print orderSn
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method+'?positionCode='+positionCode+'&token='+token
        print url
        r = session.get(url,cookies=cookies)
        print r.text.decode('unicode_escape')

    def draw_count(self, method,username):
        session = requests.Session()
        token = self.get_token('test',username)
        url1 = 'http://test.mall.g7s.chinawayltd.com/g7api/category'+'?token='+token
        #print url1
        resp1 = session.get(url1)
        ecsid =  resp1.cookies['ecsid']
        cookies = {'ecsid':ecsid}
        #print resp1.text.decode('unicode_escape')
        url2='http://test.mall.g7s.chinawayltd.com/g7api/goods/200?token='+ token
        #print url2
        resp2 = session.get(url2,cookies=cookies)
        #print resp2.text.decode('unicode_escape')
        url3 = 'http://test.mall.g7s.chinawayltd.com/g7api/flow/add?token='+token
        data1 = 'goodsId=200,number=3'
        data = self.string1(data1)
        # print url3
        resp3 = session.post(url3,data=data,cookies=cookies)
        #print resp3.text.decode('unicode_escape')
        url4 = 'http://test.mall.g7s.chinawayltd.com/g7api/flow/consignee?token='+token
        #print url4
        resp4 = session.get(url4,cookies=cookies)
        #print resp4.text.decode('unicode_escape')
        url5 = 'http://test.mall.g7s.chinawayltd.com/g7api/flow/consignee?token='+token
        #print url5
        data2 = 'name=lfc123,mobile=13730645598,provinceCode=310000000000,cityCode=310000000000,districtCode=310101000000,address=上海路22号'
        dataaddress= self.string1(data2)
        resp5 = session.post(url5,data=dataaddress,cookies=cookies)
        #print resp5.text.decode('unicode_escape')
        url6= 'http://test.mall.g7s.chinawayltd.com/g7api/flow/checkout?token='+token
        #print url6
        resp6 = session.get(url6,cookies=cookies)
        #print resp6.text.decode('unicode_escape')
        url7 = 'http://test.mall.g7s.chinawayltd.com/g7api/flow/submit?token='+token
        datapay='payId=6'
        payId= self.string1(datapay)
        #print url7
        resp7 = session.post(url7,cookies=cookies,data=payId)
        print resp7.text.decode('unicode_escape')
        d = json.loads(resp7.text)
        orderSn = d['data']['orderSn']
        cos = ChangeOrderStatus()
        cos.change_order_status(orderSn)
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method+'?token='+token
        #print url
        r = session.post(url,cookies=cookies)
        print r.text.decode('unicode_escape')
        d = json.loads(r.text)
        co =d['code']
        #print '----',co,type(co)
        if co==0:
            level = d['data']['level']
            if level=='0':
                print '谢谢参与'
                self.arr[0]+=1
            if level=='1':
                print '一等奖'
                self.arr[1]+=1
                self.flag=True
            if level=='2':
                print '二等奖'
                self.arr[2]+=1
            if level=='3':
                print '三等奖'
                self.arr[3]+=1
            if level=='4':
                print '四等奖'
                self.arr[4]+=1

        print self.arr
        self.write_file(level)
        time.sleep(1)
        return level

        print ' '

    def write_file(self,content):
        filename = 'E:/PythonWorkSpace/level.txt'
        file_object = open(filename, 'a')
        file_object.write(content+'\n')
        file_object.close()

    def draw(self, method,username):
        session = requests.Session()
        token = self.get_token('test',username)
        url1 = 'http://test.mall.g7s.chinawayltd.com/g7api/category'+'?token='+token
        print url1
        resp1 = session.get(url1)
        ecsid =  resp1.cookies['ecsid']
        cookies = {'ecsid':ecsid}
        print resp1.text.decode('unicode_escape')
        url2='http://test.mall.g7s.chinawayltd.com/g7api/goods/200?token='+ token
        print url2
        resp2 = session.get(url2,cookies=cookies)
        print resp2.text.decode('unicode_escape')
        url3 = 'http://test.mall.g7s.chinawayltd.com/g7api/flow/add?token='+token
        data1 = 'goodsId=200,number=1'
        data = self.string1(data1)
        print url3
        resp3 = session.post(url3,data=data,cookies=cookies)
        print resp3.text.decode('unicode_escape')
        url4 = 'http://test.mall.g7s.chinawayltd.com/g7api/flow/consignee?token='+token
        print url4
        resp4 = session.get(url4,cookies=cookies)
        print resp4.text.decode('unicode_escape')
        url5 = 'http://test.mall.g7s.chinawayltd.com/g7api/flow/consignee?token='+token
        print url5
        data2 = 'name=lfc123,mobile=13730645598,provinceCode=310000000000,cityCode=310000000000,districtCode=310101000000,address=上海路22号'
        dataaddress= self.string1(data2)
        resp5 = session.post(url5,data=dataaddress,cookies=cookies)
        print resp5.text.decode('unicode_escape')
        url6= 'http://test.mall.g7s.chinawayltd.com/g7api/flow/checkout?token='+token
        print url6
        resp6 = session.get(url6,cookies=cookies)
        print resp6.text.decode('unicode_escape')
        url7 = 'http://test.mall.g7s.chinawayltd.com/g7api/flow/submit?token='+token
        datapay='payId=6'
        payId= self.string1(datapay)
        print url7
        resp7 = session.post(url7,cookies=cookies,data=payId)
        print resp7.text.decode('unicode_escape')
        d = json.loads(resp7.text)
        orderSn = d['data']['orderSn']
        cos = ChangeOrderStatus()
        cos.change_order_status(orderSn)
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method+'?token='+token
        print url
        r = session.post(url,cookies=cookies)
        print r.text.decode('unicode_escape')

    def draw_times(self, method,username):
        session = requests.Session()
        token = self.get_token('test',username)
        url1 = 'http://test.mall.g7s.chinawayltd.com/g7api/category'+'?token='+token
        print url1
        resp1 = session.get(url1)
        ecsid =  resp1.cookies['ecsid']
        cookies = {'ecsid':ecsid}
        print resp1.text.decode('unicode_escape')
        url2='http://test.mall.g7s.chinawayltd.com/g7api/goods/200?token='+ token
        print url2
        resp2 = session.get(url2,cookies=cookies)
        print resp2.text.decode('unicode_escape')
        url3 = 'http://test.mall.g7s.chinawayltd.com/g7api/flow/add?token='+token
        data1 = 'goodsId=200,number=3'
        data = self.string1(data1)
        print url3
        resp3 = session.post(url3,data=data,cookies=cookies)
        print resp3.text.decode('unicode_escape')
        url4 = 'http://test.mall.g7s.chinawayltd.com/g7api/flow/consignee?token='+token
        print url4
        resp4 = session.get(url4,cookies=cookies)
        print resp4.text.decode('unicode_escape')
        url5 = 'http://test.mall.g7s.chinawayltd.com/g7api/flow/consignee?token='+token
        print url5
        data2 = 'name=lfc123,mobile=13730645598,provinceCode=310000000000,cityCode=310000000000,districtCode=310101000000,address=上海路22号'
        dataaddress= self.string1(data2)
        resp5 = session.post(url5,data=dataaddress,cookies=cookies)
        print resp5.text.decode('unicode_escape')
        url6= 'http://test.mall.g7s.chinawayltd.com/g7api/flow/checkout?token='+token
        print url6
        resp6 = session.get(url6,cookies=cookies)
        print resp6.text.decode('unicode_escape')
        url7 = 'http://test.mall.g7s.chinawayltd.com/g7api/flow/submit?token='+token
        datapay='payId=6'
        payId= self.string1(datapay)
        print url7
        resp7 = session.post(url7,cookies=cookies,data=payId)
        print resp7.text.decode('unicode_escape')
        d = json.loads(resp7.text)
        orderSn = d['data']['orderSn']
        cos = ChangeOrderStatus()
        cos.change_order_status(orderSn)
        urldrawtimes = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method+'?token='+token
        print urldrawtimes
        urldrawtimes1 = session.get(urldrawtimes,cookies=cookies)
        print urldrawtimes1.text.decode('unicode_escape')

        urldraw = 'http://test.mall.g7s.chinawayltd.com/g7api/draw'+'?token='+token
        print urldraw
        urldraw1 = session.post(urldraw,cookies=cookies)
        print urldraw1.text.decode('unicode_escape')

        urldrawtimes2 = session.get(urldrawtimes,cookies=cookies)
        print urldrawtimes2.text.decode('unicode_escape')

        useOutOfTimes = 'http://test.mall.g7s.chinawayltd.com/g7api/draw/useOutOfTimes'+'?token='+token
        print useOutOfTimes
        useOutOfTimes1 = session.get(useOutOfTimes,cookies=cookies)
        print useOutOfTimes1.text.decode('unicode_escape')

        winList = 'http://test.mall.g7s.chinawayltd.com/g7api/draw/winList'+'?token='+token
        print winList
        winList1 = session.get(winList,cookies=cookies)
        print winList1.text.decode('unicode_escape')

    def draw_winList(self, method,username):
        session = requests.Session()
        token = self.get_token('test',username)
        url1 = 'http://test.mall.g7s.chinawayltd.com/g7api/category'+'?token='+token
        print url1
        resp1 = session.get(url1)
        ecsid =  resp1.cookies['ecsid']
        cookies = {'ecsid':ecsid}
        print resp1.text.decode('unicode_escape')
        url2='http://test.mall.g7s.chinawayltd.com/g7api/goods/200?token='+ token
        print url2
        resp2 = session.get(url2,cookies=cookies)
        print resp2.text.decode('unicode_escape')
        url3 = 'http://test.mall.g7s.chinawayltd.com/g7api/flow/add?token='+token
        data1 = 'goodsId=200,number=1'
        data = self.string1(data1)
        print url3
        resp3 = session.post(url3,data=data,cookies=cookies)
        print resp3.text.decode('unicode_escape')
        url4 = 'http://test.mall.g7s.chinawayltd.com/g7api/flow/consignee?token='+token
        print url4
        resp4 = session.get(url4,cookies=cookies)
        print resp4.text.decode('unicode_escape')
        url5 = 'http://test.mall.g7s.chinawayltd.com/g7api/flow/consignee?token='+token
        print url5
        data2 = 'name=lfc123,mobile=13730645598,provinceCode=310000000000,cityCode=310000000000,districtCode=310101000000,address=上海路22号'
        dataaddress= self.string1(data2)
        resp5 = session.post(url5,data=dataaddress,cookies=cookies)
        print resp5.text.decode('unicode_escape')
        url6= 'http://test.mall.g7s.chinawayltd.com/g7api/flow/checkout?token='+token
        print url6
        resp6 = session.get(url6,cookies=cookies)
        print resp6.text.decode('unicode_escape')
        url7 = 'http://test.mall.g7s.chinawayltd.com/g7api/flow/submit?token='+token
        datapay='payId=6'
        payId= self.string1(datapay)
        print url7
        resp7 = session.post(url7,cookies=cookies,data=payId)
        print resp7.text.decode('unicode_escape')
        d = json.loads(resp7.text)
        orderSn = d['data']['orderSn']
        cos = ChangeOrderStatus()
        cos.change_order_status(orderSn)
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method+'?token='+token
        print url
        r = session.get(url,cookies=cookies)
        print r.text.decode('unicode_escape')

    def draw_useOutOfTimes(self, method,username):
        session = requests.Session()
        token = self.get_token('test',username)
        url1 = 'http://test.mall.g7s.chinawayltd.com/g7api/category'+'?token='+token
        print url1
        resp1 = session.get(url1)
        ecsid =  resp1.cookies['ecsid']
        cookies = {'ecsid':ecsid}
        print resp1.text.decode('unicode_escape')
        url2='http://test.mall.g7s.chinawayltd.com/g7api/goods/200?token='+ token
        print url2
        resp2 = session.get(url2,cookies=cookies)
        print resp2.text.decode('unicode_escape')
        url3 = 'http://test.mall.g7s.chinawayltd.com/g7api/flow/add?token='+token
        data1 = 'goodsId=200,number=1'
        data = self.string1(data1)
        print url3
        resp3 = session.post(url3,data=data,cookies=cookies)
        print resp3.text.decode('unicode_escape')
        url4 = 'http://test.mall.g7s.chinawayltd.com/g7api/flow/consignee?token='+token
        print url4
        resp4 = session.get(url4,cookies=cookies)
        print resp4.text.decode('unicode_escape')
        url5 = 'http://test.mall.g7s.chinawayltd.com/g7api/flow/consignee?token='+token
        print url5
        data2 = 'name=lfc123,mobile=13730645598,provinceCode=310000000000,cityCode=310000000000,districtCode=310101000000,address=上海路22号'
        dataaddress= self.string1(data2)
        resp5 = session.post(url5,data=dataaddress,cookies=cookies)
        print resp5.text.decode('unicode_escape')
        url6= 'http://test.mall.g7s.chinawayltd.com/g7api/flow/checkout?token='+token
        print url6
        resp6 = session.get(url6,cookies=cookies)
        print resp6.text.decode('unicode_escape')
        url7 = 'http://test.mall.g7s.chinawayltd.com/g7api/flow/submit?token='+token
        datapay='payId=6'
        payId= self.string1(datapay)
        print url7
        resp7 = session.post(url7,cookies=cookies,data=payId)
        print resp7.text.decode('unicode_escape')
        d = json.loads(resp7.text)
        orderSn = d['data']['orderSn']
        cos = ChangeOrderStatus()
        cos.change_order_status(orderSn)
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method+'?token='+token
        print url
        r = session.get(url,cookies=cookies)
        print r.text.decode('unicode_escape')

    def renew_trucks(self, method,username):
        token = self.get_token('test',username)
        #session = requests.Session()
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method+'?token='+token
        print url
        r = requests.get(url)
        print r.text.decode('unicode_escape')

    def renew_price(self, method,data,username):
        token = self.get_token('test',username)
        #session = requests.Session()
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method+ data + '?token='+token
        print url
        r = requests.get(url)
        print r.text.decode('unicode_escape')

    def renew_add(self, method,data,username):
        token = self.get_token('test',username)
        session = requests.Session()
        data = self.string(data)
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method + '?token='+token
        print url
        r = session.post(url, data=data)
        print r.text.decode('unicode_escape')
        return r

    def renew_list(self, method,username):
        session = requests.Session()
        token = self.get_token('test',username)
        method1 = 'renew/add'
        data = 'truckid=08D1A5968DFDD6C52906D9B58CC58ADD,goodsAttrId=55'
        resp=self.renew_add(method1,data,username)
        ecsid =  resp.cookies['ecsid']
        cookies = {'ecsid':ecsid}
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method + '?token='+token
        print url
        content = session.get(url, cookies = cookies)
        print content.text.decode('unicode_escape')

    def renew_getconsignee(self, method,username):
        token = self.get_token('test',username)
        #session = requests.Session()
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method+'?token='+token
        print url
        r = requests.get(url)
        print r.text.decode('unicode_escape')

    def renew_postdemoconsignee(self, method,data,username):
        token = self.get_token('demo',username)
        session = requests.Session()
        data = self.string(data)
        url = 'http://demo.mall.g7s.chinawayltd.com/g7api/'+method + '?token='+token
        print url
        r = session.post(url, data=data)
        print r.text.decode('unicode_escape')

    def renew_posttestconsignee(self, method,data,username):
        token = self.get_token('test',username)
        session = requests.Session()
        data = self.string(data)
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method + '?token='+token
        print url
        r = session.post(url, data=data)
        print r.text.decode('unicode_escape')

    def renew_checkout(self, method,username):
        session = requests.Session()
        token = self.get_token('test',username)
        method1 = 'renew/add'
        data = 'truckid=08D1A5968DFDD6C52906D9B58CC58ADD,goodsAttrId=55'
        resp=self.renew_add(method1,data,username)
        ecsid =  resp.cookies['ecsid']
        cookies = {'ecsid':ecsid}
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method + '?token='+token
        print url
        content = session.get(url, cookies = cookies)
        print content.text.decode('unicode_escape')

    def renew_deleteRecId(self, method,username):
        session = requests.Session()
        token = self.get_token('test',username)
        method1 = 'renew/add'
        data = 'truckid=5488FA6336C7FC21BBEEFC619FB20E08,goodsAttrId=55'
        resp=self.renew_add(method1,data,username)
        ecsid =  resp.cookies['ecsid']
        cookies = {'ecsid':ecsid}
        method2 = 'renew/checkout'
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method2 + '?token='+token
        content = session.get(url, cookies = cookies)
        print content.text.decode('unicode_escape')
        d = json.loads(content.text)
        recId = d['data']['goods'][0]['recId']
        print recId
        url1 = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method+recId+'?token='+token
        print url1
        content = session.delete(url1, cookies = cookies)
        print content.text.decode('unicode_escape')
        content = session.get(url, cookies = cookies)
        print content.text.decode('unicode_escape')

    def renew_submit(self, method,username):
        session = requests.Session()
        token = self.get_token('test',username)
        method1 = 'renew/add'
        data = 'truckid=08D1A5968DFDD6C52906D9B58CC58ADD,goodsAttrId=55'
        resp=self.renew_add(method1,data,username)
        ecsid =  resp.cookies['ecsid']
        cookies = {'ecsid':ecsid}
        method2 = 'renew/checkout'
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method2 + '?token='+token
        print url
        content = session.get(url, cookies = cookies)
        print content.text.decode('unicode_escape')
        d = json.loads(content.text)
        payId = d['data']['payments'][0]['payId']
        print payId
        payData = {'payId':str(payId)}
        print payData
        payurl = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method+'?token='+token
        print payurl
        content = session.post(payurl,data=payData,cookies = cookies)
        print content.text.decode('unicode_escape')

    def renew_deleteAll(self, method,username):
        session = requests.Session()
        token = self.get_token('test',username)
        method1 = 'renew/add'
        data = 'truckid=5488FA6336C7FC21BBEEFC619FB20E08,goodsAttrId=55'
        resp=self.renew_add(method1,data,username)
        ecsid =  resp.cookies['ecsid']
        cookies = {'ecsid':ecsid}
        method2 = 'renew/checkout'
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method2 + '?token='+token
        content = session.get(url, cookies = cookies)
        print content.text.decode('unicode_escape')
        url1 = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method+'?token='+token
        print url1
        content = session.delete(url1, cookies = cookies)
        print content.text.decode('unicode_escape')
        content = session.get(url, cookies = cookies)
        print content.text.decode('unicode_escape')
        ##########升级接口
    def upgrade_trucks(self, method,data,username):
        token = self.get_token('test',username)
        session = requests.Session()
        data = self.string(data)
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method + '?token='+token
        print url
        r = session.get(url, data=data)
        print r.text.decode('unicode_escape')

    def upgrade_add(self, method,data,username):
        token = self.get_token('test',username)
        session = requests.Session()
        data = self.string(data)
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method + '?token='+token
        print url
        r = session.post(url, data=data)
        print r.text.decode('unicode_escape')
        return r

    def upgrade_list(self, method,data,username):
        session = requests.Session()
        token = self.get_token('test',username)
        method1 = 'upgrade/add'
        data1 = 'truckid=5488FA6336C7FC21BBEEFC619FB20E08,25EE731D4CF22DB1F33CA7D0CE043D1E;goodsId=132'
        resp=self.upgrade_add(method1,data1,username)
        ecsid =  resp.cookies['ecsid']
        cookies = {'ecsid':ecsid}
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method + '?goodsId='+data+'&token='+token
        print url
        r = session.get(url,cookies=cookies)
        print r.text.decode('unicode_escape')

    def upgrade_list1(self, method,username):
        session = requests.Session()
        token = self.get_token('test',username)
        method1 = 'upgrade/add'
        data1 = 'truckid=5488FA6336C7FC21BBEEFC619FB20E08,25EE731D4CF22DB1F33CA7D0CE043D1E;goodsId=144'
        resp=self.upgrade_add(method1,data1,username)
        ecsid =  resp.cookies['ecsid']
        cookies = {'ecsid':ecsid}
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method + '?token='+token
        print url
        r = session.get(url,cookies=cookies)
        print r.text.decode('unicode_escape')

    def upgrade_getconsignee(self, method,username):
        token = self.get_token('test',username)
        #session = requests.Session()
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method+'?token='+token
        print url
        r = requests.get(url)
        print r.text.decode('unicode_escape')

    def upgrade_postconsignee(self, method,data,username):
        session = requests.Session()
        token = self.get_token('test',username)
        method1 = 'upgrade/add'
        data1 = 'truckid=5488FA6336C7FC21BBEEFC619FB20E08,25EE731D4CF22DB1F33CA7D0CE043D1E;goodsId=144'
        resp=self.upgrade_add(method1,data1,username)
        ecsid =  resp.cookies['ecsid']
        cookies = {'ecsid':ecsid}
        data = self.string1(data)
        print data

        url = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method + '?token='+token
        print url
        r = session.post(url, data=data,cookies=cookies)
        print r.text.decode('unicode_escape')

    def upgrade_checkout(self, method,username):
        session = requests.Session()
        token = self.get_token('test',username)
        method1 = 'upgrade/add'
        data1 = 'truckid=5488FA6336C7FC21BBEEFC619FB20E08,25EE731D4CF22DB1F33CA7D0CE043D1E;goodsId=144'
        resp=self.upgrade_add(method1,data1,username)

        ecsid =  resp.cookies['ecsid']
        cookies = {'ecsid':ecsid}
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method + '?token='+token
        print url
        content = session.get(url, cookies = cookies)
        print content.text.decode('unicode_escape')

    def upgrade_deleteRecId(self, method,username):
        session = requests.Session()
        token = self.get_token('test',username)
        method1 = 'upgrade/add'
        data1 = 'truckid=5488FA6336C7FC21BBEEFC619FB20E08,25EE731D4CF22DB1F33CA7D0CE043D1E;goodsId=144'
        resp=self.upgrade_add(method1,data1,username)
        ecsid =  resp.cookies['ecsid']
        cookies = {'ecsid':ecsid}
        method2 = 'upgrade/checkout'
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method2 + '?token='+token
        content = session.get(url, cookies = cookies)
        print content.text.decode('unicode_escape')
        d = json.loads(content.text)
        recId = d['data']['goods'][0]['recId']
        print recId
        url1 = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method+recId+'?token='+token
        print url1
        content = session.delete(url1, cookies = cookies)
        print content.text.decode('unicode_escape')
        content = session.get(url, cookies = cookies)
        print content.text.decode('unicode_escape')

    def upgrade_submit(self, method,username):
        session = requests.Session()
        token = self.get_token('test',username)
        method1 = 'upgrade/add'
        data1 = 'truckid=5488FA6336C7FC21BBEEFC619FB20E08,25EE731D4CF22DB1F33CA7D0CE043D1E;goodsId=144'
        resp=self.upgrade_add(method1,data1,username)
        ecsid =  resp.cookies['ecsid']
        cookies = {'ecsid':ecsid}
        method2 = 'upgrade/checkout'
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method2 + '?token='+token
        print url
        content = session.get(url, cookies = cookies)
        print content.text.decode('unicode_escape')
        d = json.loads(content.text)
        payId = d['data']['payments'][0]['payId']
        print payId
        payData = {'payId':str(payId)}
        print payData
        payurl = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method+'?token='+token
        print payurl
        content = session.post(payurl,data=payData,cookies = cookies)
        print content.text.decode('unicode_escape')

    def upgrade_deleteAll(self, method,username):
        session = requests.Session()
        token = self.get_token('test',username)
        method1 = 'upgrade/add'
        data1 = 'truckid=5488FA6336C7FC21BBEEFC619FB20E08,25EE731D4CF22DB1F33CA7D0CE043D1E;goodsId=144'
        resp=self.upgrade_add(method1,data1,username)
        ecsid =  resp.cookies['ecsid']
        cookies = {'ecsid':ecsid}
        method2 = 'upgrade/checkout'
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method2 + '?token='+token
        content = session.get(url, cookies = cookies)
        print content.text.decode('unicode_escape')
        url1 = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method+'?token='+token
        print url1
        content = session.delete(url1, cookies = cookies)
        print content.text.decode('unicode_escape')
        content = session.get(url, cookies = cookies)
        print content.text.decode('unicode_escape')

    def jumpURL(self, method,data,username):
        token = self.get_token('test',username)
        session = requests.Session()
        data = self.string(data)
        print data
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method+'?token='+token
        print url
        r = session.get(url,data=data)
        print r.text.decode('unicode_escape')

    def allJumpURL(self, method,username):
        token = self.get_token('test',username)
        session = requests.Session()
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method+'?token='+token
        print url
        r = session.get(url)
        print r.text.decode('unicode_escape')

    def synchronizeStatus(self, env,method,data):
        session = requests.Session()
        url = self.gsp2_create_url(env,method)
        param = self.gsp2_create_parameter(env,data)

        r = session.post(url,data=param)
        print r.text.decode('unicode_escape')

    def order_orderlist(self, method,data,username):
        token = self.get_token('test',username)
        session = requests.Session()
        data = self.string(data)
        print data
        type= data['type']
        page= data['page']
        print type, page
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method + '?page='+page+'&type='+type+'&token='+token
        print url
        r = session.get(url)
        print r.text.decode('unicode_escape')

    def order_orderOrderId(self, method,username):
        token = self.get_token('test',username)
        session = requests.Session()
        method1 = 'order'
        url1 = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method1 + '?token='+token
        print url1
        resp = session.get(url1)
        print resp.text.decode('unicode_escape')
        ecsid =  resp.cookies['ecsid']
        cookies = {'ecsid':ecsid}
        d = json.loads(resp.text)
        orderId= d['data']['orderList'][0]['orderId']
        print orderId
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/'+method+orderId+'?token='+token
        print url
        content = session.get(url,cookies=cookies)
        print content.text.decode('unicode_escape')
        #get方式提交数据
    def camera(self, url):
        h = httplib2.Http()
        t1 = time.time()
        print t1
        resp, content = h.request(url)
        t2 = time.time()
        print t2
        # print resp
        print content.decode('unicode_escape')
        a = json.loads(content.decode('unicode_escape')).get('data')[0].get('channel')[0].get('msgId')
        print a
        print 'Duration is %.3f' % (t2 - t1)
        return a
        # self.write_result('Duration is %.3f' % (t2 - t1))

    #get方式提交数据
    def get(self, url):
        ssl._create_default_https_context = ssl._create_unverified_context
        h = httplib2.Http()
        t1 = time.time()
        # u =  quote(url)
        resp, content = h.request(url,)
        t2 = time.time()
        print t2
        # print resp
        result = content.decode('unicode_escape')
        print 'Duration is %.3f' % (t2 - t1)
        return result
        # self.write_result('Duration is %.3f' % (t2 - t1))

    def get2(self,url):
        r = requests.get(url)
        content = r.text
        print content
        return content

    def rm(self):
        file = 'C:/Users/wuke/PycharmProjects/sjgc_interface_test/sjgc_interface_test/test1.txt'
        if os.path.exists(file):
            os.remove(file)

    def write1(self,content):
        fp = open("test1.txt","a")
        j = json.loads(content)
        li = j['data']
        space = ' '
        for i in li:
            type = str(i.get('type'))
            starttime = i.get('starttime')
            starttime1 = self.timestamp2string1(starttime)
            c = i.get('content')
            # print str(i).decode('unicode_escape')
            if len(type) == 1:
                s = space * 2
            else:
                s = space
            fp.write(type + s + str(starttime) + space + starttime1 + space + c)
            fp.write('\n')
        fp.close()

    def write(self,content):
        fp = open("test.txt","w+")
        j = json.loads(content)
        li = j['data']['notices']
        space = ' '
        for i in li:
            type = str(i.get('type'))
            starttime = i.get('starttime')
            starttime1 = self.timestamp2string(starttime/1000)
            c = i.get('content')
            # print str(i).decode('unicode_escape')
            if len(type) == 1:
                s = space * 2
            else:
                s = space
            fp.write(type + s + str(starttime) + space + starttime1 + space + c)
            fp.write('\n')
        fp.close()

    def timestamp2string1(self,timeStamp):
        timeArray = time.localtime(timeStamp)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        return otherStyleTime

    def timestamp2string(self, timeStamp):
        try:
            d = datetime.datetime.fromtimestamp(timeStamp)
            str1 = d.strftime("%Y-%m-%d %H:%M:%S.%f")
            # 2015-08-28 16:43:37.283000'
            return str1
        except Exception as e:
            print e
            return ''



    def get1(self, url):
        h = httplib2.Http()
        t1 = time.time()
        print t1
        resp, content = h.request(url)
        t2 = time.time()
        print t2
        # print resp
        print content.decode('unicode_escape')
        a = json.loads(content.decode('unicode_escape')).get('data').get('imageData')
        b = json.loads(content.decode('unicode_escape')).get('data').get('codeId')
        c = a,b
        print 'Duration is %.3f' % (t2 - t1)
        print c
        return c
        # self.write_result('Duration is %.3f' % (t2 - t1))

    # #写文件
    # def write_result(self, content):
    #     file_path = 'e://demo_test_result.txt'
    #     f = open(file_path, 'a')
    #     for line in content:
    #         f.write(line)
    #     f.write('\n')
    #     f.write('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    #     f.write('\n')
    #     f.flush()
    #     f.close()

    #格式化时间日期
    #获取昨天的日期
    def get_yesterday_date(self):
        now_time = datetime.datetime.now()
        yes_time = now_time + datetime.timedelta(days=-1)
        yes_date = str(yes_time)[0:10]
        return yes_date

    #获取当前时间戳
    def get_timestamp(self):
        signTime = str(int(time.time()))
        return signTime

    #生成随机浮点数
    def get_random_num(self):
        num = str(random.uniform(1000, 99999))
        return num

    #生成32位字符串
    def get_32_string(self):
        key = str(random.uniform)
        m = hashlib.md5()
        m.update(key)
        psw = m.hexdigest()
        #print psw
        return psw

        #AES对称加密
    def encryption(self, text):
        PADDING = ' '
        key = '9c11801e78582dacf047e7554e6cf9ba'
        iv = '09148e49cff0f732'
        length = 16
        count = len(text)  # .count('')
        padcount = (count % length)
        if padcount == 0:
            return text
        add = length - padcount
        text += PADDING * add
        generator = AES.new(key, AES.MODE_CBC, iv)
        crypt = generator.encrypt(text)
        cryptedStr = base64.b64encode(crypt)
        # print cryptedStr
        return cryptedStr

    def mall_test(self, method, data,username):
        getToken = GetToken()
        if len(username)>0:
            token = '&token=' + getToken.get_test_token(username)
        else:
            token = ''
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/'
        if len(token)>10:
            full_url = url + method + '?' + data + token
        else:
            full_url = url + method + '?' + data
        print full_url
        return full_url

    def create(self, data):
        if len(data) == 0:
            d = {}
            d['code'] = self.no_data_code()
            d['appkey'] = self.APPKEY()
            # print d
        else:
            p = self.string(data)
            # print 'p is',p
            p['code'] = self.code(p)
            p ['appkey'] = self.APPKEY
            # print p
        return p


    def post_sms(self, method, payload):
        session = requests.Session()
        url = 'http://test.truckmanager.g7s.chinawayltd.com/app.php?mehtod=' + method
        print url
        data = self.create(payload)
        print 'sddd',data
        r = session.post(url, data=data)
        print r.text.decode('unicode_escape')
        # print r.co

    def post_sms1(self, method, payload):
        # session = requests.Session()
        url = 'http://test.truckmanager.g7s.chinawayltd.com/app.php?mehtod=' + method
        print url
        print 'sddd',payload
        r = requests.post(url, data=payload)
        print r.text.decode('unicode_escape')


    def put_sms(self, method, payload):
        session = requests.session()
        # url = 'http://test.mall.g7s.chinawayltd.com/g7api/' + method
        # data = self.string(payload)
        # r = requests.put(url, data)
        # # ecsid =  r.cookies['path=/, g7_anonymous_phone']
        # print r.text.decode('unicode_escape')
        # print r.headers
        # g7_anonymous_phone = r.cookies['g7_anonymous_phone']
        # ecsid = r.cookies['ecsid']
        # g7_anonymous = r.cookies['g7_anonymous']
        # g7_anonymous_key = r.cookies['g7_anonymous_key']
        # cookies = {'g7_anonymous_phone':g7_anonymous_phone,'ecsid':ecsid, 'g7_anonymous':g7_anonymous,'g7_anonymous_key':g7_anonymous_key}
        cookies1 = {'g7_anonymous_phone':'13340962986','ecsid':'0fa93704a96b5d43969356b29d0d0d59b137337a', 'g7_anonymous':'1','g7_anonymous_key':'a1add9366bdaeb1010a313d0928d3aa9'}
        print cookies1
        url1 = 'http://test.mall.g7s.chinawayltd.com/g7api/order?page=1&type=ALL&token=7d9e11f78e5428e553af9efe0e8f29e0'
        content = session.get(url1, cookies = cookies1)
        print content.text.decode('unicode_escape')


    def agreements(self, method, payload):
        session = requests.Session()
        url = 'http://test.mall.g7s.chinawayltd.com/g7api/' + method
        data = self.string(payload)
        r = session.post(url, data=data)
        print r.text.decode('unicode_escape')
        ecsid =  r.cookies['ecsid']
        cookies = {'ecsid':ecsid}
        url1 = 'http://test.mall.g7s.chinawayltd.com/g7api/agreements'
        content = session.get(url1, cookies = cookies)
        print content.text.decode('unicode_escape')