#coding:utf-8
'''
@author: we
'''


import time
import json
import random
from  gearman import GearmanClient

class notification():
    server1 = '120.26.214.57:4730'
    server2 = '121.41.14.170:4730'
    server = [server1, server2]
    servertest = '172.16.1.14:4730'
    serverstress = '172.16.1.102:4730'
    serverdemo = '172.16.1.132:4730'
    method = 'notification.save'
    serverC = '121.41.6.246:4730' #时间类型
    type = [1,2,3,4,5,11,15,28,32,38,45,46,47,53,54,60,61,62,63,64,65,66,72,76,298,299,1003,1032,1038,1045,1072,1076,1299,1028,58,59,1035,35,62,9901,9902]
    type1 = [1111,'abcd']
    type2 = [1,2,3,4,5]
    marker_name = ['成都高新南天府四','sdjfkjoeirui eirjejr','920384903284098','跟着我左手右手一个慢动作，IWUEUWEHRHHJDSFKH  oieiueiwjkj 9238497384978231_+-=','四川省|成都市']
    marker_name1='888'
    probename = ['生鲜','疫苗','渣渣']
    compressor = ['0','1']
    door = ['0','1']
    alarmlevel = [2, 3]
    #未打卡类型
    nosigntype = [0, 1, 2]


    #随机经纬度
    def get_lat(self, lng, lat):
        f3 = random.randrange(100000, 999999)
        f1 = random.randrange(100000, 999999) / 1000000.00
        f2 = random.randrange(100000, 999999) / 1000000.00
        lng = float(lng) + f1
        lat = float(lat) + f2
        return lng, lat

    def testTwo(self, lng, lat,sleep):
        type = 1299
        lng, lat = self.get_lat(lng, lat)
        milaege = random.uniform(1000, 9999)
        max_speed = random.uniform(80, 150)
        id = str(int(time.time()))[4:]
        new_client = GearmanClient([self.serverdemo])

        data = json.dumps({"event_id":id,"truckid":"5FBC042A907BC269525E7B8897A65667","carnum":u"川L88999","driverid":"01DB402C78950EF4727103B0464301D8","drivername":u"lfc测试","starttime":int(time.time()),"endtime":int(time.time()),"stoptime":random.randint(1,10000),"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":lng,"lat":lat,"endlng":lng,"endlat":lat,"client_createtime":int(time.time()),
                           "next_id":0,"noticetype":type, "marker_name":random.choice(self.marker_name),'oilvolumn':random.uniform(1,1000),
                           "probename":random.choice(self.probename),"compressor":random.choice(self.compressor),"door":random.choice(self.door),"hightemp":random.uniform(20,100),"lowtemp":random.uniform(-50,20),
                           "avgtemp":random.uniform(20,60),"temperature":random.uniform(0,60),"alarmlevel":random.choice(self.alarmlevel),"nosigntype":random.choice(self.nosigntype)})
        print type(data)
        current_request = new_client.submit_job(self.method,data)
        new_result = current_request.result
        time.sleep(sleep)
        #test环境
    #车 - 浙D929AB - CF2F75A8C9AE17620043515CD2F7879B
    #lng-经度整数部分，lat-纬度整数部分,sleep-两次不同事件之间的发送间隔
    def testOne(self, lng, lat):
        types =1299
        lng, lat = self.get_lat(lng, lat)
        print lng, lat ,int(time.time()*1000)
        milaege = random.uniform(1000, 9999)
        max_speed = random.uniform(80, 150)
        id = str(int(time.time()))[4:]
        new_client = GearmanClient([self.serverC])
        data = json.dumps({"event_id":id,"truckid":"AE4B658CA4822C3041AA3861E2929254","carnum":u"测A12345","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"ServerC小可可","starttime":int(time.time()*1000),"endtime":int(time.time()*1000),"stoptime":random.randint(1,10000),"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":lng,"lat":lat,"endlng":lng,"endlat":lat,"client_createtime":int(time.time()*1000),
                               "next_id":0,"noticetype":types, "marker_name":random.choice(self.marker_name),'oilvolumn':random.uniform(1,1000),
                               "probename":random.choice(self.probename),"compressor":random.choice(self.compressor),"door":random.choice(self.door),"hightemp":random.uniform(20,100),"lowtemp":random.uniform(-50,20),
                               "avgtemp":random.uniform(20,60),"temperature":random.uniform(0,60),"alarmlevel":random.choice(self.alarmlevel),"nosigntype":random.choice(self.nosigntype)})

        current_request = new_client.submit_job(self.method,data,background=True)
        new_result = current_request.result



    #test环境
    #车 - 浙D929AB - CF2F75A8C9AE17620043515CD2F7879B
    #lng-经度整数部分，lat-纬度整数部分,sleep-两次不同事件之间的发送间隔
    def test(self, lng, lat,sleep):
        types =1
        lng, lat = self.get_lat(lng, lat)
        milaege = random.uniform(1000, 9999)
        max_speed = random.uniform(80, 150)
        id = str(int(time.time()))[4:]
        new_client = GearmanClient([self.servertest])
        for t in self.type:
            print t
            data = json.dumps({"event_id":id,"truckid":"993D29C278046063B8FC08BF6E8475C2","carnum":u"川C773HE","driverid":"","drivername":u"autotest11","starttime":int(time.time())*1000,"endtime":int(time.time())*1000,"stoptime":random.randint(1,10000),"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":lng,"lat":lat,"endlng":lng,"endlat":lat,"client_createtime":int(time.time()),"next_id":0,"noticetype":t,"marker_name":'testdemolfc',
                               "probename":random.choice(self.probename),"compressor":random.choice(self.compressor),"door":random.choice(self.door),"hightemp":random.uniform(20,100),"lowtemp":random.uniform(-50,20),
                               "avgtemp":random.uniform(20,60),"temperature":random.uniform(0,60),"alarmlevel":random.choice(self.alarmlevel),'oilvolumn':random.uniform(1,1000), "nosigntype":random.choice(self.nosigntype)})
            current_request = new_client.submit_job(self.method,data)
            new_result = current_request.result
            print new_result
            time.sleep(sleep)


    def test1(self, lng, lat,sleep):
        milaege = random.uniform(1000, 9999)
        max_speed = random.uniform(80, 150)
        id = str(int(time.time()))[4:]
        new_client = GearmanClient([self.servertest])
        for t in self.type:
            print t
            data = json.dumps({"event_id":id,"truckid":"5FBC042A907BC269525E7B8897A65667","carnum":u"川L88999","driverid":"01DB402C78950EF4727103B0464301D8","drivername":u"渣渣无效","starttime":int(time.time()),"endtime":int(time.time()),"stoptime":random.randint(1,10000),"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":lng,"lat":lat,"endlng":lng,"endlat":lat,"client_createtime":int(time.time()),
                               "next_id":0,"noticetype":t, "marker_name":random.choice(self.marker_name),'oilvolumn':random.uniform(1,1000),
                               "probename":random.choice(self.probename),"compressor":random.choice(self.compressor),"door":random.choice(self.door),"hightemp":random.uniform(20,100),"lowtemp":random.uniform(-50,20),
                               "avgtemp":random.uniform(20,60),"temperature":random.uniform(0,60),"alarmlevel":random.choice(self.alarmlevel),"nosigntype":random.choice(self.nosigntype)})
            current_request = new_client.submit_job(self.method,data)
            new_result = current_request.result
            time.sleep(sleep)

    def test2(self, lng, lat,sleep):
        lng, lat = self.get_lat(lng, lat)
        milaege = random.uniform(1000, 9999)
        max_speed = random.uniform(80, 150)
        id = str(int(time.time()))[4:]
        new_client = GearmanClient([self.servertest])
        for t in self.type:
            print t
            data = json.dumps({"event_id":id,"truckid":"0E88F512AD4FD7700EB19BA1F94C1A99","carnum":u"川A88888","driverid":"01DB402C78950EF4727103B0464301D8","drivername":u"渣渣非订阅","starttime":int(time.time()),"endtime":int(time.time()),"stoptime":random.randint(1,10000),"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":lng,"lat":lat,"endlng":lng,"endlat":lat,"client_createtime":int(time.time()),
                               "next_id":0,"noticetype":t, "marker_name":random.choice(self.marker_name),'oilvolumn':random.uniform(1,1000),
                               "probename":random.choice(self.probename),"compressor":random.choice(self.compressor),"door":random.choice(self.door),"hightemp":random.uniform(20,100),"lowtemp":random.uniform(-50,20),
                               "avgtemp":random.uniform(20,60),"temperature":random.uniform(0,60),"alarmlevel":random.choice(self.alarmlevel),"nosigntype":random.choice(self.nosigntype)})
            current_request = new_client.submit_job(self.method,data)
            new_result = current_request.result
            time.sleep(sleep)

    def testUnknow(self, lng, lat,sleep):
        lng, lat = self.get_lat(lng, lat)
        milaege = random.uniform(1000, 9999)
        max_speed = random.uniform(80, 150)
        id = str(int(time.time()))[4:]
        new_client = GearmanClient([self.servertest])
        for t in self.type1:
            print t
            data = json.dumps({"event_id":id,"truckid":"5FBC042A907BC269525E7B8897A65667","carnum":u"川L88999","driverid":"01DB402C78950EF4727103B0464301D8","drivername":u"渣渣非订阅","starttime":int(time.time()),"endtime":int(time.time()),"stoptime":random.randint(1,10000),"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":lng,"lat":lat,"endlng":lng,"endlat":lat,"client_createtime":int(time.time()),
                               "next_id":0,"noticetype":t, "marker_name":random.choice(self.marker_name),'oilvolumn':random.uniform(1,1000),
                               "probename":random.choice(self.probename),"compressor":random.choice(self.compressor),"door":random.choice(self.door),"hightemp":random.uniform(20,100),"lowtemp":random.uniform(-50,20),
                               "avgtemp":random.uniform(20,60),"temperature":random.uniform(0,60),"alarmlevel":random.choice(self.alarmlevel),"nosigntype":random.choice(self.nosigntype)})
            current_request = new_client.submit_job(self.method,data)
            new_result = current_request.result
            time.sleep(sleep)

    def testUnknow2(self, lng, lat,sleep):
        lng, lat = self.get_lat(lng, lat)
        milaege = random.uniform(1000, 9999)
        max_speed = random.uniform(80, 150)
        id = str(int(time.time()))[4:]
        new_client = GearmanClient([self.servertest])
        for t in self.type1:
            print t
            data = json.dumps({"event_id":id,"truckid":"0E88F512AD4FD7700EB19BA1F94C1A99","carnum":u"川A88888","driverid":"01DB402C78950EF4727103B0464301D8","drivername":u"渣渣非订阅","starttime":int(time.time()),"endtime":int(time.time()),"stoptime":random.randint(1,10000),"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":lng,"lat":lat,"endlng":lng,"endlat":lat,"client_createtime":int(time.time()),
                               "next_id":0,"noticetype":t, "marker_name":random.choice(self.marker_name),'oilvolumn':random.uniform(1,1000),
                               "probename":random.choice(self.probename),"compressor":random.choice(self.compressor),"door":random.choice(self.door),"hightemp":random.uniform(20,100),"lowtemp":random.uniform(-50,20),
                               "avgtemp":random.uniform(20,60),"temperature":random.uniform(0,60),"alarmlevel":random.choice(self.alarmlevel),"nosigntype":random.choice(self.nosigntype)})
            current_request = new_client.submit_job(self.method,data)
            new_result = current_request.result
            time.sleep(sleep)


    #demo环境
    #车 - 吴A12345 - C6C918E8F9DD09146DAAA024340BC9FB
    #lng-经度整数部分，lat-纬度整数部分,sleep-两次不同事件之间的发送间隔
    def demo(self, lng, lat,sleep):
        lng, lat = self.get_lat(lng, lat)
        milaege = random.uniform(1000, 9999)
        max_speed = random.uniform(80, 150)
        id = str(int(time.time()))[4:]
        new_client = GearmanClient([self.serverdemo])
        print self.type
        for t in self.type:
            print t
            data = json.dumps({"event_id":id,"truckid":"993D29C278046063B8FC08BF6E8475C2","carnum":u"川C773HE","driverid":"","drivername":u"autotest11","starttime":int(time.time())*1000,"endtime":int(time.time())*1000,"stoptime":random.randint(1,10000),"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":lng,"lat":lat,"endlng":lng,"endlat":lat,"client_createtime":int(time.time()),"next_id":0,"noticetype":t,"marker_name":'testdemolfc',
                               "probename":random.choice(self.probename),"compressor":random.choice(self.compressor),"door":random.choice(self.door),"hightemp":random.uniform(20,100),"lowtemp":random.uniform(-50,20),
                               "avgtemp":random.uniform(20,60),"temperature":random.uniform(0,60),"alarmlevel":random.choice(self.alarmlevel),'oilvolumn':random.uniform(1,1000), "nosigntype":random.choice(self.nosigntype)})
            current_request = new_client.submit_job(self.method,data)
            new_result = current_request.result
            print new_result
            time.sleep(sleep)



    #线上环境
    #车 - 粤A3JJ06 - C6C918E8F9DD09146DAAA024340BC9FB
    #lng-经度整数部分，lat-纬度整数部分,sleep-两次不同事件之间的发送间隔
    def product(self, lng, lat,sleep):
        lng, lat = self.get_lat(lng, lat)
        milaege = random.uniform(1000, 9999)
        max_speed = random.uniform(80, 150)
        id = str(int(time.time()))[4:]
        new_client = GearmanClient([random.choice(self.server)])
        for t in self.type:
            print t
            data = json.dumps({"event_id":id,"truckid":"C86CDE9A6B135CDFA0121B1CF5B9E915","carnum":u"粤A3JJ06","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(time.time()),"endtime":int(time.time()),"stoptime":random.randint(1,10000),"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":lng,"lat":lat,"endlng":lng,"endlat":lat,"client_createtime":int(time.time()),"next_id":0,"noticetype":t,"marker_name":random.choice(self.marker_name),
                               "probename":random.choice(self.probename),"compressor":random.choice(self.compressor),"door":random.choice(self.door),"hightemp":random.uniform(20,100),"lowtemp":random.uniform(-50,20),
                               "avgtemp":random.uniform(20,60),"temperature":random.uniform(0,60),"alarmlevel":random.choice(self.alarmlevel),'oilvolumn':random.uniform(1,1000), "nosigntype":random.choice(self.nosigntype)})
            current_request = new_client.submit_job(self.method,data)
            new_result = current_request.result
            time.sleep(sleep)


if __name__=='__main__':
    notification = notification()
    #for i in range(21):
       #notification.testOne(140,30)
    #notification.test(104,30,0.7)
    notification.demo(104,30,0.7)
    #notification.test(104,30,0.7)

'''
    count = 0
    while True:
        notification.testTwo(140,30,0.7)
        count+=1
        print '+++++++%d' % count
        #notification.test1(0,0,0.7)
        #notification.test2(104,30,0.7)
        #notification.testUnknow(104,30,0.7)
        #notification.testUnknow2(104,30,0.7)

    start = 1481512260
    end = 1481512320
    count = 0
    now = int(time.time())
    while now >= start:
        notification.testOne(104,30,0.7)
        count+=1
        now = int(time.time())
        print now
        if now == end:
            break
    print '+++++++%d' % count
'''
