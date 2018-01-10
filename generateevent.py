#coding:utf-8
'''
@author: we
'''

import time
from  gearman import GearmanClient
import json
import random

server1 = '120.26.214.57:4730'
server2 = '121.41.14.170:4730'
servertest = '172.16.1.14:4730'
serverstress = '172.16.1.102:4730'
serverdemo = '172.16.1.20:4730'

#b5 线上车辆
#超速
def gearmanclient():
    milaege = random.uniform(1000, 9999)  
    max_speed = random.uniform(80, 150) 
    a='notification.save'
    new_client = GearmanClient([serverdemo])
    #new_client = GearmanClient([server1])
    #new_client = GearmanClient([servertest])
    id = str(int(time.time()))[4:]
    start_time = time.time()
    b=json.dumps({"event_id":id,"truckid":"4D3D734E2691E669EFE300E6311D1722","carnum":u"川AB0001","driverid":"7B079508CC9AD08B96A97F00F532F4D3 ","drivername":u"杨柳桦樱qwieuy*(! dj UAY","starttime":int(start_time) - 100,"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.289271","lat":"31.283928","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":28})
    b1=json.dumps({"event_id":id,"truckid":"D3BC6B35B6B1641F77A2A8382A8F6339","carnum":u"川O11111","driverid":"EFC85C0F9306DF8ADD9CD72684688375","drivername":u"朱文亮","starttime":int(start_time) - 100,"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":28})
    b2=json.dumps({"event_id":id,"truckid":"C6C918E8F9DD09146DAAA024340BC9FB","carnum":u"吴A12345","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"troierytyweqhjkhsdjhckhdsfjkho","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":28})
    b3=json.dumps({"event_id":id,"truckid":"5877E51E19519E7A64B5AFCD3BB45B2C","carnum":u"川G987WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":28})
    b4=json.dumps({"event_id":id,"truckid":"15C17462C5F203E5F94B250345D01DFD","carnum":u"川Z123WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":28})
    b5=json.dumps({"event_id":id,"truckid":"C86CDE9A6B135CDFA0121B1CF5B9E915","carnum":u"粤A3JJ06","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":28})
    start_time1  = time.time()
    current_request = new_client.submit_job(a,b2)
    print 28
    end_time = time.time()
    duration = end_time - start_time1
    new_result = current_request.result
    print 'event_id   %s' %id
    print '距离   %s' %milaege
    print '最大  %s' %max_speed
    print 'finish   ' + new_result
    print '运行时间   %s' %duration
    
#出区
def out():
    milaege = int(random.uniform(1000, 9999))
    max_speed = random.uniform(80, 150) 
    a='notification.save'
    new_client = GearmanClient([serverdemo])
    #new_client = GearmanClient([server2])
    #new_client = GearmanClient([servertest])
    id = str(int(time.time()))[4:]
    start_time = time.time()
    b=json.dumps({"event_id":id,"truckid":"CF2F75A8C9AE17620043515CD2F7879B","carnum":u"浙D929AB","driverid":"EFC85C0F9306DF8ADD9CD72684688375","drivername":u"杨柳桦樱qwieuy*(! dj UAY","starttime":int(start_time),"endtime":int(start_time),"stoptime":19223984776,"maxspeed":0,"speed":"28","distance":milaege,"lng":"80.158553","lat":"40.742968","endlng":"0","endlat":"0","client_createtime":int(start_time),"next_id":128762,"noticetype":2,"marker_name":"吴可翠莲佩佩舟舟吴可翠莲佩佩舟舟吴可翠"})
    b1=json.dumps({"event_id":id,"truckid":"D3BC6B35B6B1641F77A2A8382A8F6339","carnum":u"川O11111","driverid":"EFC85C0F9306DF8ADD9CD72684688375","drivername":u"朱文亮","starttime":int(start_time),"endtime":int(start_time),"stoptime":19223984776,"maxspeed":0,"speed":"28","distance":milaege,"lng":"104.0705944","lat":"30.547096","endlng":"0","endlat":"0","client_createtime":int(start_time),"next_id":128762,"noticetype":2,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dhjf 2938是是酷"})
    b2=json.dumps({"event_id":id,"truckid":"C6C918E8F9DD09146DAAA024340BC9FB","carnum":u"吴A12345","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":128762,"noticetype":2,"marker_name":"酷等奖和dhjf 2938是是酷"})
    b3=json.dumps({"event_id":id,"truckid":"5877E51E19519E7A64B5AFCD3BB45B2C","carnum":u"川G987WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":128762,"noticetype":2,"marker_name":"酷等奖和dhjf 2938是是酷"})
    b4=json.dumps({"event_id":id,"truckid":"15C17462C5F203E5F94B250345D01DFD","carnum":u"川Z123WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":128762,"noticetype":2,"marker_name":"酷等奖和dhjf 2938是是酷"})
    b5=json.dumps({"event_id":id,"truckid":"C86CDE9A6B135CDFA0121B1CF5B9E915","carnum":u"粤A3JJ06","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":128762,"noticetype":2,"marker_name":"酷等奖和dhjf 2938是是酷"})
    current_request = new_client.submit_job(a,b2)
    end_time = time.time()
    duration = end_time - start_time
    new_result = current_request.result
    print 'event_id   %s' %id
    print '停留时间   %s' %milaege
    print 'finish   ' + new_result
    print '运行时间   %s' %duration
    
 
#进区
def inarea():
    milaege = int(random.uniform(1000, 9999))
    max_speed = random.uniform(80, 150) 
    a='notification.save'
    new_client = GearmanClient([serverdemo])
    #new_client = GearmanClient([server1])
    #new_client = GearmanClient([servertest])
    id = str(int(time.time()))[4:]
    start_time = time.time()
    b=json.dumps({"event_id":id,"truckid":"4703A08A9FFCB6D53F162E384DDB057E","carnum":u"北O22221","driverid":"EA53742B804EBD89D9D1181C12F21ED9","drivername":u"兰基","starttime":int(start_time),"endtime":int(start_time),"stoptime":0,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","client_createtime":int(start_time),"next_id":0,"noticetype":1,"marker_name":"酷就刷卡费开奖号酷就是是酷"})
    b1=json.dumps({"event_id":id,"truckid":"D3BC6B35B6B1641F77A2A8382A8F6339","carnum":u"川O11111","driverid":"EA53742B804EBD89D9D1181C12F21ED9","drivername":u"兰基","starttime":int(start_time),"endtime":int(start_time),"stoptime":0,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","client_createtime":int(start_time),"next_id":0,"noticetype":1,"marker_name":"酷就刷卡费开奖号酷就是是酷"})
    b2=json.dumps({"event_id":id,"truckid":"C6C918E8F9DD09146DAAA024340BC9FB","carnum":u"吴A12345","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":0,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","client_createtime":int(start_time),"next_id":0,"noticetype":1,"marker_name":"酷就刷卡费开奖号酷就是是酷"})
    b3=json.dumps({"event_id":id,"truckid":"5877E51E19519E7A64B5AFCD3BB45B2C","carnum":u"川G987WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":0,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","client_createtime":int(start_time),"next_id":0,"noticetype":1,"marker_name":"酷就刷卡费开奖号酷就是是酷"})
    b4=json.dumps({"event_id":id,"truckid":"15C17462C5F203E5F94B250345D01DFD","carnum":u"川Z123WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":0,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","client_createtime":int(start_time),"next_id":0,"noticetype":1,"marker_name":"酷就刷卡费开奖号酷就是是酷"})
    b5=json.dumps({"event_id":id,"truckid":"C86CDE9A6B135CDFA0121B1CF5B9E915","carnum":u"粤A3JJ06","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":0,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","client_createtime":int(start_time),"next_id":0,"noticetype":1,"marker_name":"酷就刷卡费开奖号酷就是是酷"})
    current_request = new_client.submit_job(a,b2)
    end_time = time.time()
    duration = end_time - start_time
    new_result = current_request.result
    print 'event_id   %s' %id
    print '停留时间   %s' %milaege
    print 'finish   ' + new_result
    print '运行时间   %s' %duration   
    
    
#点火
def on():
    milaege = int(random.uniform(1000, 9999))
    max_speed = random.uniform(80, 150) 
    a='notification.save'
    new_client = GearmanClient([serverdemo])
    #new_client = GearmanClient([server2])
    #new_client = GearmanClient([servertest])
    id = str(int(time.time()))[4:]
    start_time = time.time()
    b=json.dumps({"event_id":id,"truckid":"4703A08A9FFCB6D53F162E384DDB057E","carnum":u"北O22221","driverid":"EA53742B804EBD89D9D1181C12F21ED9","drivername":u"兰基","starttime":int(start_time),"endtime":int(start_time),"stoptime":0,"maxspeed":max_speed,"speed":"101","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":4})
    b1=json.dumps({"event_id":id,"truckid":"E6C5B0BB7E16C45FB5811D6ADB42E36C","carnum":u"川AS45T6","driverid":"EA53742B804EBD89D9D1181C12F21ED9","drivername":u"兰基","starttime":int(start_time),"endtime":int(start_time),"stoptime":0,"maxspeed":max_speed,"speed":"101","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":4})
    b2=json.dumps({"event_id":id,"truckid":"C6C918E8F9DD09146DAAA024340BC9FB","carnum":u"吴A12345","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":0,"maxspeed":max_speed,"speed":"101","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":4})
    b3=json.dumps({"event_id":id,"truckid":"5877E51E19519E7A64B5AFCD3BB45B2C","carnum":u"川G987WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":0,"maxspeed":max_speed,"speed":"101","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":4})
    b5=json.dumps({"event_id":id,"truckid":"C86CDE9A6B135CDFA0121B1CF5B9E915","carnum":u"粤A3JJ06","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":0,"maxspeed":max_speed,"speed":"101","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":4})
    current_request = new_client.submit_job(a,b2)
    #current_request = new_client.submit_job(a,b1)
    end_time = time.time()
    duration = end_time - start_time
    new_result = current_request.result
    print 'event_id   %s' %id
    print '停留时间   %s' %milaege
    print 'finish   ' + new_result
    print '运行时间   %s' %duration  


#熄火
def off():
    milaege = int(random.uniform(1000, 9999))
    max_speed = random.uniform(80, 150) 
    a='notification.save'
    new_client = GearmanClient([serverdemo])
    #new_client = GearmanClient([server1])
    #new_client = GearmanClient([servertest])
    id = str(int(time.time()))[4:]
    start_time = time.time()
    b=json.dumps({"event_id":id,"truckid":"4703A08A9FFCB6D53F162E384DDB057E","carnum":u"北O22221","driverid":"EA53742B804EBD89D9D1181C12F21ED9","drivername":u"兰基","starttime":int(start_time),"endtime":int(start_time),"stoptime":0,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"31.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":1234,"noticetype":5})
    b1=json.dumps({"event_id":id,"truckid":"E6C5B0BB7E16C45FB5811D6ADB42E36C","carnum":u"川AS45T6","driverid":"EA53742B804EBD89D9D1181C12F21ED9","drivername":u"兰基","starttime":int(start_time),"endtime":int(start_time),"stoptime":0,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"31.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":1234,"noticetype":5})
    b2=json.dumps({"event_id":id,"truckid":"C6C918E8F9DD09146DAAA024340BC9FB","carnum":u"吴A12345","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":0,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"31.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":1234,"noticetype":5})
    b3=json.dumps({"event_id":id,"truckid":"5877E51E19519E7A64B5AFCD3BB45B2C","carnum":u"川G987WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":0,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"31.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":1234,"noticetype":5})
    b5=json.dumps({"event_id":id,"truckid":"C86CDE9A6B135CDFA0121B1CF5B9E915","carnum":u"粤A3JJ06","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":0,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"31.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":1234,"noticetype":5})
    current_request = new_client.submit_job(a,b2)
    #current_request = new_client.submit_job(a,b1)
    end_time = time.time()
    duration = end_time - start_time
    new_result = current_request.result
    print 'event_id   %s' %id
    print '行驶里程   %s' %milaege
    print 'finish   ' + new_result
    print '运行时间   %s' %duration  

def test():
    print int(time.time())
    
    
#进省市
def inCity():

    milaege = int(random.uniform(1000, 9999))
    max_speed = random.uniform(80, 150) 
    a='notification.save'
    new_client = GearmanClient([serverdemo])
    #new_client = GearmanClient([server2])
    #new_client = GearmanClient([servertest])
    id = str(int(time.time()))[4:]
    start_time = time.time()
    b=json.dumps({"event_id":id,"truckid":"4703A08A9FFCB6D53F162E384DDB057E","carnum":u"北O22250","driverid":"EFC85C0F9306DF8ADD9CD72684688375","drivername":u"朱文亮","starttime":int(start_time),"endtime":int(start_time),"stoptime":19223984776,"maxspeed":0,"speed":"28","distance":milaege,"lng":"104.0705944","lat":"30.547096","endlng":"0","endlat":"0","client_createtime":int(start_time),"next_id":128762,"noticetype":11,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dhjf 2938是是酷"})
    b1=json.dumps({"event_id":id,"truckid":"D3BC6B35B6B1641F77A2A8382A8F6339","carnum":u"川O11111","driverid":"EFC85C0F9306DF8ADD9CD72684688375","drivername":u"朱文亮","starttime":int(start_time),"endtime":int(start_time),"stoptime":19223984776,"maxspeed":0,"speed":"28","distance":milaege,"lng":"104.0705944","lat":"30.547096","endlng":"0","endlat":"0","client_createtime":int(start_time),"next_id":128762,"noticetype":2,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dhjf 2938是是酷"})
    b2=json.dumps({"event_id":id,"truckid":"C6C918E8F9DD09146DAAA024340BC9FB","carnum":u"吴A12345","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time) - 100,"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":128762,"noticetype":11,"marker_name":"四川省|成都市"})
    b3=json.dumps({"event_id":id,"truckid":"5877E51E19519E7A64B5AFCD3BB45B2C","carnum":u"川G987WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time) - 100,"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":128762,"noticetype":11,"marker_name":"四川省|成都市"})
    b5=json.dumps({"event_id":id,"truckid":"C86CDE9A6B135CDFA0121B1CF5B9E915","carnum":u"粤A3JJ06","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":128762,"noticetype":11,"marker_name":"四川省|成都市"})
    current_request = new_client.submit_job(a,b2)
    end_time = time.time()
    duration = end_time - start_time
    new_result = current_request.result
    print 'event_id   %s' %id
    print '停留时间   %s' %milaege
    print 'finish   ' + new_result
    print '运行时间   %s' %duration
    
#急减速
def brakes():
    milaege = int(random.uniform(1000, 9999))
    max_speed = random.uniform(80, 150) 
    a='notification.save'
    new_client = GearmanClient([serverdemo])
    #new_client = GearmanClient([server1])
    #new_client = GearmanClient([servertest])
    id = str(int(time.time()))[4:]
    start_time = time.time()
    b=json.dumps({"event_id":id,"truckid":"4703A08A9FFCB6D53F162E384DDB057E","carnum":u"北O22250","driverid":"EFC85C0F9306DF8ADD9CD72684688375","drivername":u"朱文亮","starttime":int(start_time),"endtime":int(start_time),"stoptime":19223984776,"maxspeed":0,"speed":"28","distance":milaege,"lng":"104.0705944","lat":"30.547096","endlng":"0","endlat":"0","client_createtime":int(start_time),"next_id":128762,"noticetype":11,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dhjf 2938是是酷"})
    b1=json.dumps({"event_id":id,"truckid":"D3BC6B35B6B1641F77A2A8382A8F6339","carnum":u"川O11111","driverid":"EFC85C0F9306DF8ADD9CD72684688375","drivername":u"朱文亮","starttime":int(start_time),"endtime":int(start_time),"stoptime":19223984776,"maxspeed":0,"speed":"28","distance":milaege,"lng":"104.0705944","lat":"30.547096","endlng":"0","endlat":"0","client_createtime":int(start_time),"next_id":128762,"noticetype":2,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dhjf 2938是是酷"})
    b2=json.dumps({"event_id":id,"truckid":"C6C918E8F9DD09146DAAA024340BC9FB","carnum":u"吴A12345","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time) - 100,"endtime":int(start_time),"stoptime":int(random.uniform(1000, 999999)),"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":128762,"noticetype":53,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dh是是酷"})
    b3=json.dumps({"event_id":id,"truckid":"5877E51E19519E7A64B5AFCD3BB45B2C","carnum":u"川G987WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time) - 100,"endtime":int(start_time),"stoptime":int(random.uniform(1000, 999999)),"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":128762,"noticetype":53,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dh是是酷"})
    b5=json.dumps({"event_id":id,"truckid":"C86CDE9A6B135CDFA0121B1CF5B9E915","carnum":u"粤A3JJ06","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":int(random.uniform(1000, 999999)),"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":128762,"noticetype":53,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dh是是酷"})
    current_request = new_client.submit_job(a,b2)
    end_time = time.time()
    duration = end_time - start_time
    new_result = current_request.result
    print 'event_id   %s' %id
    print '停留时间   %s' %milaege
    print 'finish   ' + new_result
    print '运行时间   %s' %duration
    
#拆壳
def openbox():
    milaege = int(random.uniform(1000, 9999))
    max_speed = random.uniform(80, 150) 
    a='notification.save'
    new_client = GearmanClient([serverdemo])
    #new_client = GearmanClient([server2])
    #new_client = GearmanClient([servertest])
    id = str(int(time.time()))[4:]
    start_time = time.time()
    b=json.dumps({"event_id":id,"truckid":"4703A08A9FFCB6D53F162E384DDB057E","carnum":u"北O22250","driverid":"EFC85C0F9306DF8ADD9CD72684688375","drivername":u"杨柳桦樱qwieuy*(! dj UAY","starttime":int(start_time),"endtime":int(start_time),"stoptime":19223984776,"maxspeed":0,"speed":"28","distance":milaege,"lng":"104.0705944","lat":"30.547096","endlng":"0","endlat":"0","client_createtime":int(start_time),"next_id":128762,"noticetype":38,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dhjf 2938是是酷"})
    b1=json.dumps({"event_id":id,"truckid":"D3BC6B35B6B1641F77A2A8382A8F6339","carnum":u"川O11111","driverid":"EFC85C0F9306DF8ADD9CD72684688375","drivername":u"朱文亮","starttime":int(start_time),"endtime":int(start_time),"stoptime":19223984776,"maxspeed":0,"speed":"28","distance":milaege,"lng":"104.0705944","lat":"30.547096","endlng":"0","endlat":"0","client_createtime":int(start_time),"next_id":128762,"noticetype":2,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dhjf 2938是是酷"})
    b2=json.dumps({"event_id":id,"truckid":"C6C918E8F9DD09146DAAA024340BC9FB","carnum":u"吴A12345","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time) - 100,"endtime":int(start_time),"stoptime":int(random.uniform(1000, 999999)),"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":128762,"noticetype":38,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dh是是酷"})
    b3=json.dumps({"event_id":id,"truckid":"5877E51E19519E7A64B5AFCD3BB45B2C","carnum":u"川G987WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time) - 100,"endtime":int(start_time),"stoptime":int(random.uniform(1000, 999999)),"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":128762,"noticetype":38,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dh是是酷"})
    b5=json.dumps({"event_id":id,"truckid":"C86CDE9A6B135CDFA0121B1CF5B9E915","carnum":u"粤A3JJ06","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":int(random.uniform(1000, 999999)),"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":128762,"noticetype":38,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dh是是酷"})
    current_request = new_client.submit_job(a,b2)
    end_time = time.time()
    duration = end_time - start_time
    new_result = current_request.result
    print 'event_id   %s' %id
    print '停留时间   %s' %milaege
    print 'finish   ' + new_result
    print '运行时间   %s' %duration
    
#合壳
def closebox():
    milaege = int(random.uniform(1000, 9999))
    max_speed = random.uniform(80, 150) 
    a='notification.save'
    new_client = GearmanClient([serverdemo])
    #new_client = GearmanClient([server1])
    #new_client = GearmanClient([servertest])
    id = str(int(time.time()))[4:]
    start_time = time.time()
    b=json.dumps({"event_id":id,"truckid":"4703A08A9FFCB6D53F162E384DDB057E","carnum":u"北O22250","driverid":"EFC85C0F9306DF8ADD9CD72684688375","drivername":u"朱文亮","starttime":int(start_time),"endtime":int(start_time),"stoptime":19223984776,"maxspeed":0,"speed":"28","distance":milaege,"lng":"104.0705944","lat":"30.547096","endlng":"0","endlat":"0","client_createtime":int(start_time),"next_id":128762,"noticetype":11,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dhjf 2938是是酷"})
    b1=json.dumps({"event_id":id,"truckid":"D3BC6B35B6B1641F77A2A8382A8F6339","carnum":u"川O11111","driverid":"EFC85C0F9306DF8ADD9CD72684688375","drivername":u"朱文亮","starttime":int(start_time),"endtime":int(start_time),"stoptime":19223984776,"maxspeed":0,"speed":"28","distance":milaege,"lng":"104.0705944","lat":"30.547096","endlng":"0","endlat":"0","client_createtime":int(start_time),"next_id":128762,"noticetype":2,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dhjf 2938是是酷"})
    b2=json.dumps({"event_id":id,"truckid":"C6C918E8F9DD09146DAAA024340BC9FB","carnum":u"吴A12345","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time) - 100,"endtime":int(start_time),"stoptime":int(random.uniform(1000, 999999)),"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":128762,"noticetype":1038,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dh是是酷"})
    b3=json.dumps({"event_id":id,"truckid":"5877E51E19519E7A64B5AFCD3BB45B2C","carnum":u"川G987WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time) - 100,"endtime":int(start_time),"stoptime":int(random.uniform(1000, 999999)),"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":128762,"noticetype":1038,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dh是是酷"})
    b5=json.dumps({"event_id":id,"truckid":"C86CDE9A6B135CDFA0121B1CF5B9E915","carnum":u"粤A3JJ06","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":int(random.uniform(1000, 999999)),"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":128762,"noticetype":1038,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dh是是酷"})
    current_request = new_client.submit_job(a,b2)
    end_time = time.time()
    duration = end_time - start_time
    new_result = current_request.result
    print 'event_id   %s' %id
    print '停留时间   %s' %milaege
    print 'finish   ' + new_result
    print '运行时间   %s' %duration
    
#移除天线
def removeGPS():
    milaege = int(random.uniform(1000, 9999))
    max_speed = random.uniform(80, 150) 
    a='notification.save'
    new_client = GearmanClient([serverdemo])
    #new_client = GearmanClient([server2])
    #new_client = GearmanClient([servertest])
    id = str(int(time.time()))[4:]
    start_time = time.time()
    b=json.dumps({"event_id":id,"truckid":"4703A08A9FFCB6D53F162E384DDB057E","carnum":u"北O22250","driverid":"EFC85C0F9306DF8ADD9CD72684688375","drivername":u"朱文亮","starttime":int(start_time),"endtime":int(start_time),"stoptime":19223984776,"maxspeed":0,"speed":"28","distance":milaege,"lng":"104.0705944","lat":"30.547096","endlng":"0","endlat":"0","client_createtime":int(start_time),"next_id":128762,"noticetype":11,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dhjf 2938是是酷"})
    b1=json.dumps({"event_id":id,"truckid":"D3BC6B35B6B1641F77A2A8382A8F6339","carnum":u"川O11111","driverid":"EFC85C0F9306DF8ADD9CD72684688375","drivername":u"朱文亮","starttime":int(start_time),"endtime":int(start_time),"stoptime":19223984776,"maxspeed":0,"speed":"28","distance":milaege,"lng":"104.0705944","lat":"30.547096","endlng":"0","endlat":"0","client_createtime":int(start_time),"next_id":128762,"noticetype":2,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dhjf 2938是是酷"})
    b2=json.dumps({"event_id":id,"truckid":"C6C918E8F9DD09146DAAA024340BC9FB","carnum":u"吴A12345","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time) - 100,"endtime":int(start_time),"stoptime":int(random.uniform(1000, 999999)),"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":128762,"noticetype":3,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dh是是酷"})
    b3=json.dumps({"event_id":id,"truckid":"5877E51E19519E7A64B5AFCD3BB45B2C","carnum":u"川G987WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time) - 100,"endtime":int(start_time),"stoptime":int(random.uniform(1000, 999999)),"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":128762,"noticetype":3,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dh是是酷"})
    b5=json.dumps({"event_id":id,"truckid":"C86CDE9A6B135CDFA0121B1CF5B9E915","carnum":u"粤A3JJ06","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":int(random.uniform(1000, 999999)),"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":128762,"noticetype":3,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dh是是酷"})
    current_request = new_client.submit_job(a,b2)
    end_time = time.time()
    duration = end_time - start_time
    new_result = current_request.result
    print 'event_id   %s' %id
    print '停留时间   %s' %milaege
    print 'finish   ' + new_result
    print '运行时间   %s' %duration
    
#恢复天线
def fixGPS():
    milaege = int(random.uniform(1000, 9999))
    max_speed = random.uniform(80, 150) 
    a='notification.save'
    new_client = GearmanClient([serverdemo])
    #new_client = GearmanClient([server1])
    #new_client = GearmanClient([servertest])
    id = str(int(time.time()))[4:]
    start_time = time.time()
    b=json.dumps({"event_id":id,"truckid":"4703A08A9FFCB6D53F162E384DDB057E","carnum":u"北O22250","driverid":"EFC85C0F9306DF8ADD9CD72684688375","drivername":u"朱文亮","starttime":int(start_time),"endtime":int(start_time),"stoptime":19223984776,"maxspeed":0,"speed":"28","distance":milaege,"lng":"104.0705944","lat":"30.547096","endlng":"0","endlat":"0","client_createtime":int(start_time),"next_id":128762,"noticetype":11,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dhjf 2938是是酷"})
    b1=json.dumps({"event_id":id,"truckid":"CF2F75A8C9AE17620043515CD2F7879B","carnum":u"浙D929AB","driverid":"EFC85C0F9306DF8ADD9CD72684688375","drivername":u"朱文亮","starttime":int(start_time),"endtime":int(start_time),"stoptime":19223984776,"maxspeed":0,"speed":"28","distance":milaege,"lng":"134.0705944","lat":"30.547096","endlng":"0","endlat":"0","client_createtime":int(start_time),"next_id":128762,"noticetype":1003,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dhjf 2938是是酷"})
    b2=json.dumps({"event_id":id,"truckid":"C6C918E8F9DD09146DAAA024340BC9FB","carnum":u"吴A12345","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":1003})
    b3=json.dumps({"event_id":id,"truckid":"5877E51E19519E7A64B5AFCD3BB45B2C","carnum":u"川G987WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time) - 100,"endtime":int(start_time),"stoptime":int(random.uniform(1000, 999999)),"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":128762,"noticetype":1003,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dh是是酷"})
    b5=json.dumps({"event_id":id,"truckid":"C86CDE9A6B135CDFA0121B1CF5B9E915","carnum":u"粤A3JJ06","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":int(random.uniform(1000, 999999)),"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":128762,"noticetype":1003,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dh是是酷"})
    current_request = new_client.submit_job(a,b2)
    end_time = time.time()
    duration = end_time - start_time
    new_result = current_request.result
    print 'event_id   %s' %id
    print '停留时间   %s' %milaege
    print 'finish   ' + new_result
    print '运行时间   %s' %duration    
    
#温度超标开始
def HighT():
    milaege = int(random.uniform(1000, 9999))
    max_speed = random.uniform(80, 150) 
    a='notification.save'
    new_client = GearmanClient([serverdemo])
    #new_client = GearmanClient([server2])
    #new_client = GearmanClient([servertest])
    id = str(int(time.time()))[4:]
    start_time = time.time()
    b=json.dumps({"event_id":id,"truckid":"C56E8B166DC04CAE8E088A37C3462E1D","carnum":u"天B99993","driverid":"EFC85C0F9306DF8ADD9CD72684688375","drivername":u"朱文亮","starttime":int(start_time),"endtime":int(start_time),"stoptime":19223984776,"maxspeed":0,"speed":"28","distance":milaege,"lng":"104.0705944","lat":"30.547096","endlng":"0","endlat":"0","client_createtime":int(start_time),"next_id":128762,"noticetype":11,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dhjf 2938是是酷"})
    b1=json.dumps({"event_id":id,"truckid":"D3BC6B35B6B1641F77A2A8382A8F6339","carnum":u"川O11111","driverid":"EFC85C0F9306DF8ADD9CD72684688375","drivername":u"朱文亮","starttime":int(start_time),"endtime":int(start_time),"stoptime":19223984776,"maxspeed":0,"speed":"28","distance":milaege,"lng":"104.0705944","lat":"30.547096","endlng":"0","endlat":"0","client_createtime":int(start_time),"next_id":128762,"noticetype":2,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dhjf 2938是是酷"})
    b2=json.dumps({"event_id":id,"truckid":"5877E51E19519E7A64B5AFCD3BB45B2C","carnum":u"川G987WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time) - 100,"endtime":int(start_time),"stoptime":int(random.uniform(1000, 999999)),"maxspeed":max_speed,
                   "speed":"46","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995",
                   "client_createtime":int(start_time),"next_id":128762,"noticetype":46,
                   "probename":'熊佩',"compressor":'1',"door":'0',"hightemp":'22.3',"lowtemp":'1.2',
                       "avgtemp":'18.9',"temperature":'22.1',"alarmlevel":2})
    b3=json.dumps({"event_id":id,"truckid":"C6C918E8F9DD09146DAAA024340BC9FB","carnum":u"吴A12345","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":int(random.uniform(1000, 999999)),"maxspeed":max_speed,
                   "speed":"46","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995",
                   "client_createtime":int(start_time),"next_id":128762,"noticetype":46,
                   "probename":'熊佩',"compressor":'1',"door":'0',"hightemp":'22.3',"lowtemp":'1.2',
                       "avgtemp":'18.9',"temperature":'22.1',"alarmlevel":2})
    b5=json.dumps({"event_id":id,"truckid":"C86CDE9A6B135CDFA0121B1CF5B9E915","carnum":u"粤A3JJ06","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":int(random.uniform(1000, 999999)),"maxspeed":max_speed,
                   "speed":"46","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995",
                   "client_createtime":int(start_time),"next_id":128762,"noticetype":46,
                   "probename":'熊佩',"compressor":'1',"door":'0',"hightemp":'22.3',"lowtemp":'1.2',
                       "avgtemp":'18.9',"temperature":'22.1',"alarmlevel":2})
    current_request = new_client.submit_job(a,b3)
    end_time = time.time()
    duration = end_time - start_time
    new_result = current_request.result
    print 'event_id   %s' %id
    print '停留时间   %s' %milaege
    print 'finish   ' + new_result
    print '运行时间   %s' %duration 
    
#温度超标结束
def HighTE():
    milaege = int(random.uniform(1000, 9999))
    max_speed = random.uniform(80, 150) 
    a='notification.save'
    new_client = GearmanClient([serverdemo])
    #new_client = GearmanClient([server1])
    #new_client = GearmanClient([servertest])
    id = str(int(time.time()))[4:]
    start_time = time.time()
    b=json.dumps({"event_id":id,"truckid":"C56E8B166DC04CAE8E088A37C3462E1D","carnum":u"天B99993","driverid":"EFC85C0F9306DF8ADD9CD72684688375","drivername":u"朱文亮","starttime":int(start_time),"endtime":int(start_time),"stoptime":19223984776,"maxspeed":0,"speed":"28","distance":milaege,"lng":"104.0705944","lat":"30.547096","endlng":"0","endlat":"0","client_createtime":int(start_time),"next_id":128762,"noticetype":11,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dhjf 2938是是酷"})
    b1=json.dumps({"event_id":id,"truckid":"D3BC6B35B6B1641F77A2A8382A8F6339","carnum":u"川O11111","driverid":"EFC85C0F9306DF8ADD9CD72684688375","drivername":u"朱文亮","starttime":int(start_time),"endtime":int(start_time),"stoptime":19223984776,"maxspeed":0,"speed":"28","distance":milaege,"lng":"104.0705944","lat":"30.547096","endlng":"0","endlat":"0","client_createtime":int(start_time),"next_id":128762,"noticetype":2,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dhjf 2938是是酷"})
    b2=json.dumps({"event_id":id,"truckid":"5877E51E19519E7A64B5AFCD3BB45B2C","carnum":u"川G987WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time) - 100,"endtime":int(start_time),"stoptime":int(random.uniform(1000, 999999)),"maxspeed":max_speed,
                   "speed":"46","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995",
                   "client_createtime":int(start_time),"next_id":128762,"noticetype":47,
                   "probename":'熊佩',"compressor":'1',"door":'0',"hightemp":'22.3',"lowtemp":'1.2',
                       "avgtemp":'18.9',"temperature":'22.1',"alarmlevel":2})
    b3=json.dumps({"event_id":id,"truckid":"C6C918E8F9DD09146DAAA024340BC9FB","carnum":u"吴A12345","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":int(random.uniform(1000, 999999)),"maxspeed":max_speed,
                   "speed":"46","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995",
                   "client_createtime":int(start_time),"next_id":128762,"noticetype":47,
                   "probename":'熊佩',"compressor":'1',"door":'0',"hightemp":'22.3',"lowtemp":'1.2',
                       "avgtemp":'18.9',"temperature":'22.1',"alarmlevel":2})
    
    b5=json.dumps({"event_id":id,"truckid":"C86CDE9A6B135CDFA0121B1CF5B9E915","carnum":u"粤A3JJ06","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":int(random.uniform(1000, 999999)),"maxspeed":max_speed,
                   "speed":"46","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995",
                   "client_createtime":int(start_time),"next_id":128762,"noticetype":47,
                   "probename":'熊佩',"compressor":'1',"door":'0',"hightemp":'22.3',"lowtemp":'1.2',
                       "avgtemp":'18.9',"temperature":'22.1',"alarmlevel":2})
    current_request = new_client.submit_job(a,b3)
    end_time = time.time()
    duration = end_time - start_time
    new_result = current_request.result
    print 'event_id   %s' %id
    print '停留时间   %s' %milaege
    print 'finish   ' + new_result
    print '运行时间   %s' %duration 
    
#加油
def Oil():
    milaege = int(random.uniform(1000, 9999))
    max_speed = random.uniform(80, 150) 
    a='notification.save'
    new_client = GearmanClient([serverdemo])
    #new_client = GearmanClient([server2])
    #new_client = GearmanClient([servertest])
    id = str(int(time.time()))[4:]
    start_time = time.time()
    b=json.dumps({"event_id":id,"truckid":"C56E8B166DC04CAE8E088A37C3462E1D","carnum":u"天B99993","driverid":"EFC85C0F9306DF8ADD9CD72684688375","drivername":u"朱文亮","starttime":int(start_time),"endtime":int(start_time),"stoptime":19223984776,"maxspeed":0,"speed":"28","distance":milaege,"lng":"104.0705944","lat":"30.547096","endlng":"0","endlat":"0","client_createtime":int(start_time),"next_id":128762,"noticetype":11,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dhjf 2938是是酷"})
    b1=json.dumps({"event_id":id,"truckid":"D3BC6B35B6B1641F77A2A8382A8F6339","carnum":u"川O11111","driverid":"EFC85C0F9306DF8ADD9CD72684688375","drivername":u"朱文亮","starttime":int(start_time),"endtime":int(start_time),"stoptime":19223984776,"maxspeed":0,"speed":"28","distance":milaege,"lng":"104.0705944","lat":"30.547096","endlng":"0","endlat":"0","client_createtime":int(start_time),"next_id":128762,"noticetype":2,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dhjf 2938是是酷"})
    b2=json.dumps({"event_id":id,"truckid":"5877E51E19519E7A64B5AFCD3BB45B2C","carnum":u"川G987WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time) - 100,"endtime":int(start_time),"stoptime":int(random.uniform(1000, 999999)),"maxspeed":max_speed,
                   "speed":"46","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995",
                   "client_createtime":int(start_time),"next_id":128762,"noticetype":60,"oilvolumn":max_speed,
                   "probename":'熊佩',"compressor":'1',"door":'0',"hightemp":'22.3',"lowtemp":'1.2',
                       "avgtemp":'18.9',"temperature":'22.1',"alarmlevel":2})
    b3=json.dumps({"event_id":id,"truckid":"C6C918E8F9DD09146DAAA024340BC9FB","carnum":u"吴A12345","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":60})
    b5=json.dumps({"event_id":id,"truckid":"C86CDE9A6B135CDFA0121B1CF5B9E915","carnum":u"粤A3JJ06","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":int(random.uniform(1000, 999999)),"maxspeed":max_speed,
                   "speed":"46","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995",
                   "client_createtime":int(start_time),"next_id":128762,"noticetype":60,"oilvolumn":max_speed,
                   "probename":'熊佩',"compressor":'1',"door":'0',"hightemp":'22.3',"lowtemp":'1.2',
                       "avgtemp":'18.9',"temperature":'22.1',"alarmlevel":2})
    current_request = new_client.submit_job(a,b5)
    end_time = time.time()
    duration = end_time - start_time
    new_result = current_request.result
    print 'event_id   %s' %id
    print '停留时间   %s' %milaege
    print 'finish   ' + new_result
    print '运行时间   %s' %duration

#油耗异常
def exception():
    milaege = int(random.uniform(1000, 9999))
    max_speed = random.uniform(80, 150) 
    a='notification.save'
    new_client = GearmanClient([serverdemo])
    #new_client = GearmanClient([server2])
    #new_client = GearmanClient([servertest])
    id = str(int(time.time()))[4:]
    start_time = time.time()
    b=json.dumps({"event_id":id,"truckid":"C56E8B166DC04CAE8E088A37C3462E1D","carnum":u"天B99993","driverid":"EFC85C0F9306DF8ADD9CD72684688375","drivername":u"朱文亮","starttime":int(start_time),"endtime":int(start_time),"stoptime":19223984776,"maxspeed":0,"speed":"28","distance":milaege,"lng":"104.0705944","lat":"30.547096","endlng":"0","endlat":"0","client_createtime":int(start_time),"next_id":128762,"noticetype":11,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dhjf 2938是是酷"})
    b1=json.dumps({"event_id":id,"truckid":"D3BC6B35B6B1641F77A2A8382A8F6339","carnum":u"川O11111","driverid":"EFC85C0F9306DF8ADD9CD72684688375","drivername":u"朱文亮","starttime":int(start_time),"endtime":int(start_time),"stoptime":19223984776,"maxspeed":0,"speed":"28","distance":milaege,"lng":"104.0705944","lat":"30.547096","endlng":"0","endlat":"0","client_createtime":int(start_time),"next_id":128762,"noticetype":2,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dhjf 2938是是酷"})
    b2=json.dumps({"event_id":id,"truckid":"5877E51E19519E7A64B5AFCD3BB45B2C","carnum":u"川G987WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time) - 100,"endtime":int(start_time),"stoptime":int(random.uniform(1000, 999999)),"maxspeed":max_speed,
                   "speed":"46","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995",
                   "client_createtime":int(start_time),"next_id":128762,"noticetype":61,"oilvolumn":max_speed,
                   "probename":'熊佩',"compressor":'1',"door":'0',"hightemp":'22.3',"lowtemp":'1.2',
                       "avgtemp":'18.9',"temperature":'22.1',"alarmlevel":2})
    b3=json.dumps({"event_id":id,"truckid":"C6C918E8F9DD09146DAAA024340BC9FB","carnum":u"吴A12345","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":61})
    b5=json.dumps({"event_id":id,"truckid":"C86CDE9A6B135CDFA0121B1CF5B9E915","carnum":u"粤A3JJ06","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":int(random.uniform(1000, 999999)),"maxspeed":max_speed,
                   "speed":"46","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995",
                   "client_createtime":int(start_time),"next_id":128762,"noticetype":61,"oilvolumn":max_speed,
                   "probename":'熊佩',"compressor":'1',"door":'0',"hightemp":'22.3',"lowtemp":'1.2',
                       "avgtemp":'18.9',"temperature":'22.1',"alarmlevel":2})
    current_request = new_client.submit_job(a,b3)
    end_time = time.time()
    duration = end_time - start_time
    new_result = current_request.result
    print 'event_id   %s' %id
    print '停留时间   %s' %milaege
    print 'finish   ' + new_result
    print '运行时间   %s' %duration  

#熄火少油
def reduce():
    milaege = int(random.uniform(1000, 9999))
    max_speed = random.uniform(80, 150) 
    a='notification.save'
    new_client = GearmanClient([serverdemo])
    #new_client = GearmanClient([server1])
    #new_client = GearmanClient([servertest])
    id = str(int(time.time()))[4:]
    start_time = time.time()
    b=json.dumps({"event_id":id,"truckid":"C56E8B166DC04CAE8E088A37C3462E1D","carnum":u"天B99993","driverid":"EFC85C0F9306DF8ADD9CD72684688375","drivername":u"朱文亮","starttime":int(start_time),"endtime":int(start_time),"stoptime":19223984776,"maxspeed":0,"speed":"28","distance":milaege,"lng":"104.0705944","lat":"30.547096","endlng":"0","endlat":"0","client_createtime":int(start_time),"next_id":128762,"noticetype":11,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dhjf 2938是是酷"})
    b1=json.dumps({"event_id":id,"truckid":"D3BC6B35B6B1641F77A2A8382A8F6339","carnum":u"川O11111","driverid":"EFC85C0F9306DF8ADD9CD72684688375","drivername":u"朱文亮","starttime":int(start_time),"endtime":int(start_time),"stoptime":19223984776,"maxspeed":0,"speed":"28","distance":milaege,"lng":"104.0705944","lat":"30.547096","endlng":"0","endlat":"0","client_createtime":int(start_time),"next_id":128762,"noticetype":2,"marker_name":"酷就刷卡费开奖号酷就卡三等奖和dhjf 2938是是酷"})
    b2=json.dumps({"event_id":id,"truckid":"5877E51E19519E7A64B5AFCD3BB45B2C","carnum":u"川G987WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time) - 100,"endtime":int(start_time),"stoptime":int(random.uniform(1000, 999999)),"maxspeed":max_speed,
                   "speed":"46","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995",
                   "client_createtime":int(start_time),"next_id":128762,"noticetype":62,"oilvolumn":max_speed,
                   "probename":'熊佩',"compressor":'1',"door":'0',"hightemp":'22.3',"lowtemp":'1.2',
                       "avgtemp":'18.9',"temperature":'22.1',"alarmlevel":2})
    b3=json.dumps({"event_id":id,"truckid":"C6C918E8F9DD09146DAAA024340BC9FB","carnum":u"吴A12345","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":62})
    b5=json.dumps({"event_id":id,"truckid":"C86CDE9A6B135CDFA0121B1CF5B9E915","carnum":u"粤A3JJ06","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":int(random.uniform(1000, 999999)),"maxspeed":max_speed,
                   "speed":"46","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995",
                   "client_createtime":int(start_time),"next_id":128762,"noticetype":62,"oilvolumn":max_speed,
                   "probename":'熊佩',"compressor":'1',"door":'0',"hightemp":'22.3',"lowtemp":'1.2',
                       "avgtemp":'18.9',"temperature":'22.1',"alarmlevel":2})
    current_request = new_client.submit_job(a,b3)
    end_time = time.time()
    duration = end_time - start_time
    new_result = current_request.result
    print 'event_id   %s' %id
    print '停留时间   %s' %milaege
    print 'finish   ' + new_result
    print '运行时间   %s' %duration
    
#停车未熄火
def stalled():
    milaege = random.uniform(1000, 9999)  
    max_speed = random.uniform(80, 150) 
    a='notification.save'
    new_client = GearmanClient([serverdemo])
    #new_client = GearmanClient([servertest])
    id = str(int(time.time()))[4:]
    start_time = time.time()
    b=json.dumps({"event_id":id,"truckid":"4D3D734E2691E669EFE300E6311D1722","carnum":u"川AB0001","driverid":"7B079508CC9AD08B96A97F00F532F4D3 ","drivername":u"杨柳桦樱qwieuy*(! dj UAY","starttime":int(start_time) - 100,"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.289271","lat":"31.283928","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":28})
    b1=json.dumps({"event_id":id,"truckid":"4703A08A9FFCB6D53F162E384DDB057E","carnum":u"北O22221","driverid":"EFC85C0F9306DF8ADD9CD72684688375","drivername":u"朱文亮","starttime":int(start_time) - 100,"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":76})
    b2=json.dumps({"event_id":id,"truckid":"4703A08A9FFCB6D53F162E384DDB057E","carnum":u"北O22221","driverid":"EFC85C0F9306DF8ADD9CD72684688375","drivername":u"朱文亮","starttime":int(start_time) - 100,"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":76})
    b3=json.dumps({"event_id":id,"truckid":"C6C918E8F9DD09146DAAA024340BC9FB","carnum":u"吴A12345","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":76})
    start_time1  = time.time()
    current_request = new_client.submit_job(a,b3)
    print 28
    end_time = time.time()
    duration = end_time - start_time1
    new_result = current_request.result
    print 'event_id   %s' %id
    print '距离   %s' %milaege
    print '最大  %s' %max_speed
    print 'finish   ' + new_result
    print '运行时间   %s' %duration
    
#车辆碰撞
def collision():
    milaege = random.uniform(1000, 9999)  
    max_speed = random.uniform(80, 150) 
    a='notification.save'
    new_client = GearmanClient([serverdemo])
    #new_client = GearmanClient([server2])
    #new_client = GearmanClient([servertest])
    id = str(int(time.time()))[4:]
    start_time = time.time()
    b=json.dumps({"event_id":id,"truckid":"4D3D734E2691E669EFE300E6311D1722","carnum":u"川AB0001","driverid":"7B079508CC9AD08B96A97F00F532F4D3 ","drivername":u"杨柳桦樱qwieuy*(! dj UAY","starttime":int(start_time) - 100,"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.289271","lat":"31.283928","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":28})
    b1=json.dumps({"event_id":id,"truckid":"CF2F75A8C9AE17620043515CD2F7879B","carnum":u"浙D929AB","driverid":"-1","drivername":u"后方可会飞的  1238907!@*&^#0 KJ","starttime":int(start_time) - 100,"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"999.8","distance":milaege,"lng":"104.2582015","lat":"31.0099174","endlng":"130.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":298})
    b2=json.dumps({"event_id":id,"truckid":"C6C918E8F9DD09146DAAA024340BC9FB","carnum":u"吴A12345","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":298})
    b3=json.dumps({"event_id":id,"truckid":"5877E51E19519E7A64B5AFCD3BB45B2C","carnum":u"川G987WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":298})
    b4=json.dumps({"event_id":id,"truckid":"15C17462C5F203E5F94B250345D01DFD","carnum":u"川Z123WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":28})
    b5=json.dumps({"event_id":id,"truckid":"C86CDE9A6B135CDFA0121B1CF5B9E915","carnum":u"粤A3JJ06","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":298})
    start_time1  = time.time()
    current_request = new_client.submit_job(a,b2)
    print 28
    end_time = time.time()
    duration = end_time - start_time1
    new_result = current_request.result
    print 'event_id   %s' %id
    print '距离   %s' %milaege
    print '最大  %s' %max_speed
    print 'finish   ' + new_result
    print '运行时间   %s' %duration
    
#疲劳驾驶
def tired():
    milaege = random.uniform(1000, 9999)  
    max_speed = random.uniform(80, 150) 
    a='notification.save'
    new_client = GearmanClient([serverdemo])
    #new_client = GearmanClient([server2])
    #new_client = GearmanClient([servertest])
    id = str(int(time.time()))[4:]
    start_time = time.time()
    b=json.dumps({"event_id":id,"truckid":"4D3D734E2691E669EFE300E6311D1722","carnum":u"川AB0001","driverid":"7B079508CC9AD08B96A97F00F532F4D3 ","drivername":u"杨柳桦樱qwieuy*(! dj UAY","starttime":int(start_time) - 100,"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.289271","lat":"31.283928","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":28})
    b1=json.dumps({"event_id":id,"truckid":"CF2F75A8C9AE17620043515CD2F7879B","carnum":u"浙D929AB","driverid":"-1","drivername":u"荆棘里的花","starttime":int(start_time),"endtime":int(start_time),"stoptime":18061,"maxspeed":max_speed,"speed":"999.8","distance":milaege,"lng":"104.2582015","lat":"31.0099174","endlng":"130.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":15})
    b2=json.dumps({"event_id":id,"truckid":"C6C918E8F9DD09146DAAA024340BC9FB","carnum":u"吴A12345","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":15})
    b3=json.dumps({"event_id":id,"truckid":"5877E51E19519E7A64B5AFCD3BB45B2C","carnum":u"川G987WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":15})
    b4=json.dumps({"event_id":id,"truckid":"15C17462C5F203E5F94B250345D01DFD","carnum":u"川Z123WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":28})
    b5=json.dumps({"event_id":id,"truckid":"C86CDE9A6B135CDFA0121B1CF5B9E915","carnum":u"粤A3JJ06","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":15})
    start_time1  = time.time()
    current_request = new_client.submit_job(a,b2)
    end_time = time.time()
    duration = end_time - start_time1
    new_result = current_request.result
    print 'event_id   %s' %id
    print '距离   %s' %milaege
    print '最大  %s' %max_speed
    print 'finish   ' + new_result
    print '运行时间   %s' %duration
    
#急加速
def speedup():
    milaege = random.uniform(1000, 9999)  
    max_speed = random.uniform(80, 150) 
    a='notification.save'
    new_client = GearmanClient([serverdemo])
    #new_client = GearmanClient([server1])
    #new_client = GearmanClient([servertest])
    id = str(int(time.time()))[4:]
    start_time = time.time()
    b=json.dumps({"event_id":id,"truckid":"4D3D734E2691E669EFE300E6311D1722","carnum":u"川AB0001","driverid":"7B079508CC9AD08B96A97F00F532F4D3 ","drivername":u"杨柳桦樱qwieuy*(! dj UAY","starttime":int(start_time) - 100,"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.289271","lat":"31.283928","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":28})
    b1=json.dumps({"event_id":id,"truckid":"CF2F75A8C9AE17620043515CD2F7879B","carnum":u"浙D929AB","driverid":"-1","drivername":u"荆棘里的花","starttime":int(start_time),"endtime":int(start_time),"stoptime":23746896,"maxspeed":max_speed,"speed":"999.8","distance":milaege,"lng":"134.2582015","lat":"31.0099174","endlng":"130.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":54})
    b2=json.dumps({"event_id":id,"truckid":"C6C918E8F9DD09146DAAA024340BC9FB","carnum":u"吴A12345","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":54})
    b3=json.dumps({"event_id":id,"truckid":"5877E51E19519E7A64B5AFCD3BB45B2C","carnum":u"川G987WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":54})
    b4=json.dumps({"event_id":id,"truckid":"15C17462C5F203E5F94B250345D01DFD","carnum":u"川Z123WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":28})
    b5=json.dumps({"event_id":id,"truckid":"C86CDE9A6B135CDFA0121B1CF5B9E915","carnum":u"粤A3JJ06","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":54})
    start_time1  = time.time()
    current_request = new_client.submit_job(a,b2)
    print 28
    end_time = time.time()
    duration = end_time - start_time1
    new_result = current_request.result
    print 'event_id   %s' %id
    print '距离   %s' %milaege
    print '最大  %s' %max_speed
    print 'finish   ' + new_result
    print '运行时间   %s' %duration
    
#上班打卡
def clockin():
    milaege = random.uniform(1000, 9999)  
    max_speed = random.uniform(80, 150) 
    a='notification.save'
    new_client = GearmanClient([serverdemo])
    #new_client = GearmanClient([server1])
    #new_client = GearmanClient([servertest])
    id = str(int(time.time()))[4:]
    start_time = time.time()
    b=json.dumps({"event_id":id,"truckid":"4D3D734E2691E669EFE300E6311D1722","carnum":u"川AB0001","driverid":"7B079508CC9AD08B96A97F00F532F4D3 ","drivername":u"杨柳桦樱qwieuy*(! dj UAY","starttime":int(start_time) - 100,"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.289271","lat":"31.283928","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":28})
    b1=json.dumps({"event_id":id,"truckid":"CF2F75A8C9AE17620043515CD2F7879B","carnum":u"浙D929AB","driverid":"-1","drivername":u"吴可","starttime":int(start_time),"endtime":int(start_time),"stoptime":23746896,"maxspeed":max_speed,"speed":"999.8","distance":milaege,"lng":"119.8582015","lat":"34.2299174","endlng":"130.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":63})
    b2=json.dumps({"event_id":id,"truckid":"C6C918E8F9DD09146DAAA024340BC9FB","carnum":u"吴A12345","driverid":"-1","drivername":u"troierytyweqhjkhsdjhckhdsfjkho","starttime":int(start_time),"endtime":int(start_time),"stoptime":23746896,"maxspeed":max_speed,"speed":"999.8","distance":milaege,"lng":"119.8582015","lat":"34.2299174","endlng":"130.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":63})
    b3=json.dumps({"event_id":id,"truckid":"C86CDE9A6B135CDFA0121B1CF5B9E915","carnum":u"粤A3JJ06","driverid":"-1","drivername":u"吴可","starttime":int(start_time),"endtime":int(start_time),"stoptime":23746896,"maxspeed":max_speed,"speed":"999.8","distance":milaege,"lng":"119.8582015","lat":"34.2299174","endlng":"130.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":63})
    b4=json.dumps({"event_id":id,"truckid":"15C17462C5F203E5F94B250345D01DFD","carnum":u"川Z123WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":28})
    b5=json.dumps({"event_id":id,"truckid":"C86CDE9A6B135CDFA0121B1CF5B9E915","carnum":u"粤A3JJ06","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":54})
    start_time1  = time.time()
    #current_request = new_client.submit_job(a,b1)
    current_request = new_client.submit_job(a,b2)
    print 28
    end_time = time.time()
    duration = end_time - start_time1
    new_result = current_request.result
    print 'event_id   %s' %id
    print '距离   %s' %milaege
    print '最大  %s' %max_speed
    print 'finish   ' + new_result
    print '运行时间   %s' %duration
    
#下班打卡
def outin():
    ma = 'u'
    milaege = random.uniform(1000, 9999)  
    max_speed = random.uniform(80, 150) 
    a='notification.save'
    new_client = GearmanClient([serverdemo])
    #new_client = GearmanClient([server1])
    #new_client = GearmanClient([servertest])
    id = str(int(time.time()))[4:]
    start_time = time.time()
    b=json.dumps({"event_id":id,"truckid":"4D3D734E2691E669EFE300E6311D1722","carnum":u"川AB0001","driverid":"7B079508CC9AD08B96A97F00F532F4D3 ","drivername":u"杨柳桦樱qwieuy*(! dj UAY","starttime":int(start_time) - 100,"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.289271","lat":"31.283928","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":28})
    b1=json.dumps({"event_id":id,"truckid":"CF2F75A8C9AE17620043515CD2F7879B","carnum":u"浙D929AB","driverid":"-1","drivername":u"黄宇 和我我就和我换 发货积分和 JHDSJH hkjhf","starttime":int(start_time),"endtime":int(start_time),"stoptime":9926340,"maxspeed":max_speed,"speed":"999.8","distance":100000,"lng":"109.2582015","lat":"31.0099174","endlng":"130.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":64})
    b2=json.dumps({"event_id":id,"truckid":"C6C918E8F9DD09146DAAA024340BC9FB","carnum":u"吴A12345","driverid":"-1","drivername":u"黄宇 和我我就和我换 发货积分和 JHDSJH hkjhf","starttime":int(start_time),"endtime":int(start_time),"stoptime":9926340,"maxspeed":max_speed,"speed":"999.8","distance":100000,"lng":"109.2582015","lat":"31.0099174","endlng":"130.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":64})
    b3=json.dumps({"event_id":id,"truckid":"5877E51E19519E7A64B5AFCD3BB45B2C","carnum":u"川G987WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":54})
    b4=json.dumps({"event_id":id,"truckid":"15C17462C5F203E5F94B250345D01DFD","carnum":u"川Z123WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":28})
    b5=json.dumps({"event_id":id,"truckid":"C86CDE9A6B135CDFA0121B1CF5B9E915","carnum":u"粤A3JJ06","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":54})
    start_time1  = time.time()
    #current_request = new_client.submit_job(a,b1)
    current_request = new_client.submit_job(a,b2)
    print 28
    end_time = time.time()
    duration = end_time - start_time1
    new_result = current_request.result
    print 'event_id   %s' %id
    print '距离   %s' %milaege
    print '最大  %s' %max_speed
    print 'finish   ' + new_result
    print '运行时间   %s' %duration
    
#未打卡 - 1
def noclockin():
    milaege = random.uniform(1000, 9999)  
    max_speed = random.uniform(80, 150) 
    a='notification.save'
    new_client = GearmanClient([serverdemo])
    #new_client = GearmanClient([server1])
    #new_client = GearmanClient([servertest])
    id = str(int(time.time()))[4:]
    start_time = time.time()
    b=json.dumps({"event_id":id,"truckid":"4D3D734E2691E669EFE300E6311D1722","carnum":u"川AB0001","driverid":"7B079508CC9AD08B96A97F00F532F4D3 ","drivername":u"杨柳桦樱qwieuy*(! dj UAY","starttime":int(start_time) - 100,"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.289271","lat":"31.283928","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":28})
    b1=json.dumps({"event_id":id,"truckid":"CF2F75A8C9AE17620043515CD2F7879B","carnum":u"浙D929AB","driverid":"-1","drivername":u"吴可","starttime":int(start_time),"endtime":int(start_time),"stoptime":23746896,"maxspeed":max_speed,"speed":"999.8","distance":milaege,"lng":"151.2582015","lat":"31.0099174","endlng":"130.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":65,"nosigntype":0})
    b2=json.dumps({"event_id":id,"truckid":"C6C918E8F9DD09146DAAA024340BC9FB","carnum":u"吴A12345","driverid":"-1","drivername":u"吴可","starttime":int(start_time),"endtime":int(start_time),"stoptime":23746896,"maxspeed":max_speed,"speed":"999.8","distance":milaege,"lng":"151.2582015","lat":"31.0099174","endlng":"130.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":65,"nosigntype":0})
    b3=json.dumps({"event_id":id,"truckid":"5877E51E19519E7A64B5AFCD3BB45B2C","carnum":u"川G987WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":54})
    b4=json.dumps({"event_id":id,"truckid":"15C17462C5F203E5F94B250345D01DFD","carnum":u"川Z123WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":28})
    b5=json.dumps({"event_id":id,"truckid":"C86CDE9A6B135CDFA0121B1CF5B9E915","carnum":u"粤A3JJ06","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":54})
    start_time1  = time.time()
    current_request = new_client.submit_job(a,b2)
    print 28
    end_time = time.time()
    duration = end_time - start_time1
    new_result = current_request.result
    print 'event_id   %s' %id
    print '距离   %s' %milaege
    print '最大  %s' %max_speed
    print 'finish   ' + new_result
    print '运行时间   %s' %duration
    
#未打卡 -2
def noclockin1():
    milaege = random.uniform(1000, 9999)  
    max_speed = random.uniform(80, 150) 
    a='notification.save'
    new_client = GearmanClient([serverdemo])
    #new_client = GearmanClient([server1])
    #new_client = GearmanClient([servertest])
    id = str(int(time.time()))[4:]
    start_time = time.time()
    b=json.dumps({"event_id":id,"truckid":"4D3D734E2691E669EFE300E6311D1722","carnum":u"川AB0001","driverid":"7B079508CC9AD08B96A97F00F532F4D3 ","drivername":u"杨柳桦樱qwieuy*(! dj UAY","starttime":int(start_time) - 100,"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.289271","lat":"31.283928","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":28})
    b1=json.dumps({"event_id":id,"truckid":"CF2F75A8C9AE17620043515CD2F7879B","carnum":u"浙D929AB","driverid":"-1","drivername":u"吴可","starttime":int(start_time),"endtime":int(start_time),"stoptime":23746896,"maxspeed":max_speed,"speed":"999.8","distance":milaege,"lng":"151.2582015","lat":"31.0099174","endlng":"130.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":65,"nosigntype":1})
    b2=json.dumps({"event_id":id,"truckid":"C6C918E8F9DD09146DAAA024340BC9FB","carnum":u"吴A12345","driverid":"-1","drivername":u"吴可","starttime":int(start_time),"endtime":int(start_time),"stoptime":23746896,"maxspeed":max_speed,"speed":"999.8","distance":milaege,"lng":"151.2582015","lat":"31.0099174","endlng":"130.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":65,"nosigntype":1})
    b3=json.dumps({"event_id":id,"truckid":"5877E51E19519E7A64B5AFCD3BB45B2C","carnum":u"川G987WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":54})
    b4=json.dumps({"event_id":id,"truckid":"15C17462C5F203E5F94B250345D01DFD","carnum":u"川Z123WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":28})
    b5=json.dumps({"event_id":id,"truckid":"C86CDE9A6B135CDFA0121B1CF5B9E915","carnum":u"粤A3JJ06","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":54})
    start_time1  = time.time()
    #current_request = new_client.submit_job(a,b1)
    current_request = new_client.submit_job(a,b2)
    print 28
    end_time = time.time()
    duration = end_time - start_time1
    new_result = current_request.result
    print 'event_id   %s' %id
    print '距离   %s' %milaege
    print '最大  %s' %max_speed
    print 'finish   ' + new_result
    print '运行时间   %s' %duration
    
 #未打卡 -2
def noclockin2():
    milaege = random.uniform(1000, 9999)  
    max_speed = random.uniform(80, 150) 
    a='notification.save'
    new_client = GearmanClient([serverdemo])
    #new_client = GearmanClient([server1])
    #new_client = GearmanClient([servertest])
    id = str(int(time.time()))[4:]
    start_time = time.time()
    b=json.dumps({"event_id":id,"truckid":"4D3D734E2691E669EFE300E6311D1722","carnum":u"川AB0001","driverid":"7B079508CC9AD08B96A97F00F532F4D3 ","drivername":u"杨柳桦樱qwieuy*(! dj UAY","starttime":int(start_time) - 100,"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.289271","lat":"31.283928","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":28})
    b1=json.dumps({"event_id":id,"truckid":"CF2F75A8C9AE17620043515CD2F7879B","carnum":u"浙D929AB","driverid":"-1","drivername":u"吴可","starttime":int(start_time),"endtime":int(start_time),"stoptime":23746896,"maxspeed":max_speed,"speed":"999.8","distance":milaege,"lng":"151.2582015","lat":"31.0099174","endlng":"130.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":65,"nosigntype":2})
    b2=json.dumps({"event_id":id,"truckid":"C6C918E8F9DD09146DAAA024340BC9FB","carnum":u"吴A12345","driverid":"-1","drivername":u"吴可","starttime":int(start_time),"endtime":int(start_time),"stoptime":23746896,"maxspeed":max_speed,"speed":"999.8","distance":milaege,"lng":"151.2582015","lat":"31.0099174","endlng":"130.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":65,"nosigntype":2})
    b3=json.dumps({"event_id":id,"truckid":"5877E51E19519E7A64B5AFCD3BB45B2C","carnum":u"川G987WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":54})
    b4=json.dumps({"event_id":id,"truckid":"15C17462C5F203E5F94B250345D01DFD","carnum":u"川Z123WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":28})
    b5=json.dumps({"event_id":id,"truckid":"C86CDE9A6B135CDFA0121B1CF5B9E915","carnum":u"粤A3JJ06","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":54})
    start_time1  = time.time()
    #current_request = new_client.submit_job(a,b1)
    current_request = new_client.submit_job(a,b2)
    print 28
    end_time = time.time()
    duration = end_time - start_time1
    new_result = current_request.result
    print 'event_id   %s' %id
    print '距离   %s' %milaege
    print '最大  %s' %max_speed
    print 'finish   ' + new_result
    print '运行时间   %s' %duration   
    
#打卡器异常
def clockinexception():
    milaege = random.uniform(1000, 9999)  
    max_speed = random.uniform(80, 150) 
    a='notification.save'
    #new_client = GearmanClient([serverdemo])
    #new_client = GearmanClient([server1])
    new_client = GearmanClient([servertest])
    id = str(int(time.time()))[4:]
    start_time = time.time()
    b=json.dumps({"event_id":id,"truckid":"4D3D734E2691E669EFE300E6311D1722","carnum":u"川AB0001","driverid":"7B079508CC9AD08B96A97F00F532F4D3 ","drivername":u"杨柳桦樱qwieuy*(! dj UAY","starttime":int(start_time) - 100,"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.289271","lat":"31.283928","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":28})
    b1=json.dumps({"event_id":id,"truckid":"CF2F75A8C9AE17620043515CD2F7879B","carnum":u"浙D929AB","driverid":"-1","drivername":u"吴可","starttime":int(start_time),"endtime":int(start_time),"stoptime":23746896,"maxspeed":max_speed,"speed":"999.8","distance":milaege,"lng":"134.2582015","lat":"31.0099174","endlng":"130.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":66})
    b2=json.dumps({"event_id":id,"truckid":"C6C918E8F9DD09146DAAA024340BC9FB","carnum":u"吴A12345","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":54})
    b3=json.dumps({"event_id":id,"truckid":"5877E51E19519E7A64B5AFCD3BB45B2C","carnum":u"川G987WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":54})
    b4=json.dumps({"event_id":id,"truckid":"15C17462C5F203E5F94B250345D01DFD","carnum":u"川Z123WU","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":28})
    b5=json.dumps({"event_id":id,"truckid":"C86CDE9A6B135CDFA0121B1CF5B9E915","carnum":u"粤A3JJ06","driverid":"5D6359FE7C8B1236D8F60CD761AD4EDE","drivername":u"黄宇","starttime":int(start_time),"endtime":int(start_time),"stoptime":192,"maxspeed":max_speed,"speed":"28","distance":milaege,"lng":"104.1582865","lat":"30.0099174","endlng":"110.2582015","endlat":"20.0097995","client_createtime":int(start_time),"next_id":0,"noticetype":54})
    start_time1  = time.time()
    current_request = new_client.submit_job(a,b1)
    print 28
    end_time = time.time()
    duration = end_time - start_time1
    new_result = current_request.result
    print 'event_id   %s' %id
    print '距离   %s' %milaege
    print '最大  %s' %max_speed
    print 'finish   ' + new_result
    print '运行时间   %s' %duration
    
if __name__=='__main__':
    #inCity()
    n = 5
    #for i in range(5000):   
        #print "@@@@@@@@@@"  + str(i)
        #print id()
    for i in range(1):
        print '这是第%i次循环' %i
        #HighT()
#        gearmanclient()
#        time.sleep(n)        
#        out()
#        time.sleep(n)
#        inarea()
#        time.sleep(n)
#        on()
#        time.sleep(n)
#        off()
#        time.sleep(n)
#        inCity()
#        time.sleep(n)
#        brakes()
#        time.sleep(n)
#        openbox()
#        time.sleep(n)
#        closebox()
#        time.sleep(n)
#        removeGPS()
#        fixGPS()
#        time.sleep(n)
#        HighT()
#        time.sleep(n)
#        HighTE()
#        time.sleep(n)
#        Oil()
#        time.sleep(n)
#        exception()
#        time.sleep(n)
#        reduce()
#        time.sleep(n)
#        tired()
#        time.sleep(n)
#        speedup()
#        time.sleep(n)
        clockin()
        time.sleep(n)
        outin()
        time.sleep(n)
        noclockin()
        time.sleep(n)
        noclockin1()
        time.sleep(n)
        noclockin2()
        #time.sleep(5)
#        outin()
#        time.sleep(n)
        #stalled()
        
        