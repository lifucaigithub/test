#coding:utf-8
import base64
import hashlib
import json
import random
import sys
import time
from Crypto.Cipher import AES
import httplib2
from interface_test_utils.get_token import GetToken

import datetime
__author__ = 'we'


reload(sys)
sys.setdefaultencoding('utf-8')


class utils():
    APPSECRET = '20c079d77bd0c11c60c8f1d603f7f1db'
    APPKEY = '47a7ccefe0'
    BASEURL = 'http://demo.truckmanager.g7s.chinawayltd.com/app.php?'
    #TESTBASEURL = 'http://test.truckmanager.g7s.chinawayltd.com/app.php?'
    TESTBASEURL = 'http://172.16.2.114/app.php?'
    externaltesturi = 'http://test.truckmanager.g7s.chinawayltd.com/external.php?'
    method = 'external.message.sendMessage'
    #原始参数拼接为字典
    def string(self, data):
        d = {}
        if data.startswith('[{\"longitude\"') or data.startswith('settings={')or data.startswith('gpsnos='):
            original = data.replace(' ', '').split('*')
        else:
            original = data.replace(' ', '').split(',')
        map(lambda x: d.setdefault(x.split('=')[0], x.split('=')[1]), original)
        return d

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

    #计算校验码
    def code(self, dict):
        value = ''
        key = dict.keys()
        for k in sorted(key):
            value += dict[k]
        key = value + self.APPSECRET
        print key
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
        print j
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
    def create_parameter_login(self, ENV, method, data):
        m = 'method=' + method + '&'
        if 'test' in ENV:
            url = self.TESTBASEURL + m
        elif 'demo' in ENV:
            url = self.BASEURL + m
        else:
            url = self.BASEURL.replace('demo', 'test') + m

        cc = '&code=' + self.code(self.string(data))
        p = self.string(data)
        username = p.get('username')
        password = p.get('password')
        post = url + 'username='+username+'&'+'password=' +password+'&' 'appkey=' + self.APPKEY + cc
        print post
        return post
    def create_parameter_logout(self, ENV, method, data,username):
        getToken = GetToken()
        m = 'method=' + method + '&'
        if 'test' in ENV:
            url = self.TESTBASEURL + m
        elif 'demo' in ENV:
            url = self.BASEURL + m
        else:
            url = self.BASEURL.replace('demo', 'test') + m

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
    #拼接测试参数
    def create_parameter(self, ENV, method, data, username):
        #data1 = '{"oiltime":"2016-05-31 14:21","oilvolume":125}'
        #u.create_parameter('demo', 'truck.driver.saveDriver', 'drivername=阿斯顿马丁1,id=123', 'wuke'))
        getToken = GetToken()
        m = 'method=' + method + '&'
        if 'test' in ENV:
            url = self.TESTBASEURL + m
        elif 'demo' in ENV:
            url = self.BASEURL + m
        else:
            url = self.BASEURL.replace('demo', 'test') + m
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
    def create_parameter_siji5(self, ENV, method, data, username):
        #data1 = '{"oiltime":"2016-05-31 14:21","oilvolume":125}'
        #u.create_parameter('demo', 'truck.driver.saveDriver', 'drivername=阿斯顿马丁1,id=123', 'wuke'))
        getToken = GetToken()
        m = 'method=' + method + '&'
        if 'test' in ENV:
            url = self.TESTBASEURL + m
        elif 'demo' in ENV:
            url = self.BASEURL + m
        else:
            url = self.BASEURL.replace('demo', 'test') + m
        if url.startswith('http://demo'):
            token = '&token=' + getToken.get_demo_token(username)
        else:
            token = '&token=' + getToken.get_testsiji5_token(username)
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
    def create_parameter_syncScore(self, ENV, method, data, username):
        #data1 = '{"oiltime":"2016-05-31 14:21","oilvolume":125}'
        #u.create_parameter('demo', 'truck.driver.saveDriver', 'drivername=阿斯顿马丁1,id=123', 'wuke'))

        getToken = GetToken()
        m = 'method=' + method + '&'
        if 'test' in ENV:
            url = self.externaltesturi + m

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
        base_url = 'http://demo.truckmanager.g7s.chinawayltd.com/external.php?'
        signTime = int(time.time())
        m = 'method=' + method + '&'
        if 'demo' in ENV:
            url = base_url + m
        else:
            url = base_url.replace('demo', 'test') + m
        appkey = '844937e502bec18e'
        appSecret = 'bc4b6a10bf6ee6e6ffbf66f3a0813fa4'
        cc = 'sign=' + self.third_code(self.string(data + ',signTime=%d' % signTime + ',appkey=%s' % appkey + ', appSecret=%s' % appSecret + ',method=%s' % method))
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
    def third_create_parameterdata(self,data):
        signTime = int(time.time())
        appkey = '844937e502bec18e'
        appSecret = 'bc4b6a10bf6ee6e6ffbf66f3a0813fa4'
        cc = 'sign=' + self.third_code(self.string(data + ',signTime=%d' % signTime + ',appkey=%s' % appkey + ', appSecret=%s' % appSecret+ ',method=%s' % self.method))
        print cc
        p = self.string(data)
        p['signTime'] = str(signTime)
        p['appkey'] = appkey
        para = ''
        for k in p.keys():
            para += k + '=' + p[k] + '&'
        post =para + cc
        post = post.replace('\\', '')
        print post
        return post
    def third_create_parameter1(self, ENV):
        #ETC 83c3d502f183b4dd 02d4ea925213210c3e1f8a6013bce6b7
        #OILCARD 8ef39525e7d126c7 ca79770ee66317b3eaa872b48d0147f7
        #管车 47a7ccefe0 20c079d77bd0c11c60c8f1d603f7f1db
        #招采 844937e502bec18e  bc4b6a10bf6ee6e6ffbf66f3a0813fa4
        base_url = 'http://demo.truckmanager.g7s.chinawayltd.com/external.php?'
        signTime = int(time.time())
        m = 'method=' + self.method
        if 'demo' in ENV:
            uri = base_url+m
        else:
            uri = base_url.replace('demo', 'test')+m
        print uri
        return uri
    #get方式提交数据
    def get(self, url):
        h = httplib2.Http()
        t1 = time.time()
        print t1
        resp, content = h.request(url)
        t2 = time.time()
        print t2
        print content.decode('unicode_escape')
        self.write_result(content.decode('unicode_escape'))
        print 'Duration is %.3f' % (t2 - t1)
        self.write_result('Duration is %.3f' % (t2 - t1))

    def post(self,uri):
        h = httplib2.Http('.cache')
        t1 = time.time()
        print t1
        data =  'message=3,title=haha12311,uid=79F4ED6BE54383D3D866B969002DB159,description=lfctestandroid,linktext=阅读全文最多10个字符,linktype=1,linkurl=http://www.baidu.com'
        bodydata = self.third_create_parameterdata(data)
        response,content = h.request(uri, 'POST',body = bodydata, headers={'Content-Type': 'application/x-www-form-urlencoded'})
        t2 = time.time()
        print t2
        print content.decode('unicode_escape')
        self.write_result(content.decode('unicode_escape'))
        print 'Duration is %.3f' % (t2 - t1)
        self.write_result('Duration is %.3f' % (t2 - t1))
    def post1(self,uri):
        h = httplib2.Http('.cache')
        t1 = time.time()
        print t1
        data ='[{"oiltime":"2016-05-31 14:21","oilvolume":125},{"oiltime":"2016-05-30 14:21","oilvolume":122}]'
        bodydata = self.third_create_parameterdata(data)
        response,content = h.request(uri, 'POST',body = bodydata, headers={'Content-Type': 'application/x-www-form-urlencoded'})
        t2 = time.time()
        print t2
        print content.decode('unicode_escape')
        self.write_result(content.decode('unicode_escape'))
        print 'Duration is %.3f' % (t2 - t1)
        self.write_result('Duration is %.3f' % (t2 - t1))
    #写文件
    def write_result(self, content):
        file_path = 'e://demo_test_result.txt'
        f = open(file_path, 'a')
        for line in content:
            f.write(line)
        f.write('\n')
        f.write('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        f.write('\n')
        f.flush()
        f.close()

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
    def md5_pwd(self,password):
        m = hashlib.md5()
        m.update(password)
        psw = m.hexdigest()
        #print psw
        return psw
    def md5_string(self,code):
        m = hashlib.md5()
        m.update(code)
        psw = m.hexdigest()
        return psw

