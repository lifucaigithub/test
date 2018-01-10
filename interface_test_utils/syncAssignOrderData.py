__author__ = 'Elvis'
#coding:utf-8
import datetime
import httplib
import time
import requests
class SyncAssignOrderData():

    baseUrl='http://172.16.1.143:8080/router/rest?'

    def get_respon(self,method,sign,app_key,format):
        data={"sysId":"GSP","startId":"180","page":"2","limit":"9"}
        timestamp = self.get_yesterday_date()
        m = 'method=' + method + '&'+'sign=' + sign + '&'+'app_key=' + app_key + '&'+ 'format=' + format + '&'+ 'timestamp=' + timestamp+'&'+'data='+str(data).replace(' ','')
        url = self.baseUrl + m
        print url
        return  url
    def get_yesterday_date(self):
        now_time = datetime.datetime.now()
        current_time = str(now_time)[0:19]
        #print current_time
        return current_time
    def get(self, url):
        t1 = time.time()
        print t1
        respon = requests.get(url)
        t2 = time.time()
        print t2
        #print respon.headers
        print respon.content
        print 'Duration is %.3f' % (t2 - t1)

if __name__ == '__main__':
    ss = SyncAssignOrderData()
    ss.get(ss.get_respon('syncAssignOrderData','123','1088','json'))