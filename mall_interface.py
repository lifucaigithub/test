#coding:utf-8
from interface_test_utils import utilstest
import  time
import random
from interface_test_utils.changeOrderStatus import ChangeOrderStatus
__author__ = 'li'

if __name__ == '__main__':
    u = utilstest.utils()
    #转盘banner
    u.banner_list('banner','3','smart040')
    #抽奖路口
    #u.draw_times('draw/times','smart040')
    #u.draw_winList('draw/winList','smart040')
    #u.draw_useOutOfTimes('draw/useOutOfTimes','smart040')
    #u.draw('draw','smart040')

    #续费相关接口

    #u.renew_trucks('renew/trucks','smart040')

    #u.renew_price('renew/price/','55','smart040')

    #08D1A5968DFDD6C52906D9B58CC58ADD  E23557902A796511F461806F5AAFCCB9   其他类型车辆  ,recId=5276
    #u.renew_add('renew/add','truckid=5488FA6336C7FC21BBEEFC619FB20E08,goodsAttrId=55','smart040')

    #u.renew_list('renew/list','smart040')

    #demo
    #u.renew_postdemoconsignee('renew/consignee','name=lfc,mobile=12345678900','lfc123')

    #test
    #u.renew_posttestconsignee('renew/consignee','name=lfc,mobile=11111111111','smart040')

    #u.renew_getconsignee('renew/consignee','smart040')
    #u.renew_checkout('renew/checkout','smart040')

    #u.renew_deleteRecId('renew/delete/','smart040')

    #u.renew_submit('renew/submit','smart040')

    #u.renew_deleteAll('renew/delete','smart040')

    #升级相关接口

    #u.upgrade_trucks('upgrade/trucks','goodsId=144','smart040')

    #08D1A5968DFDD6C52906D9B58CC58ADD 北O11111,882C1E3AF3DF27BD46994A08EE4F2F7A 照SE0002   5488FA6336C7FC21BBEEFC619FB20E08  川A773HE  25EE731D4CF22DB1F33CA7D0CE043D1E  川AC050A
    #u.upgrade_add('upgrade/add','truckid=5488FA6336C7FC21BBEEFC619FB20E08,25EE731D4CF22DB1F33CA7D0CE043D1E;goodsId=144','smart040')

    #u.upgrade_list1('upgrade/list','smart040')

    #u.upgrade_postconsignee('upgrade/consignee','name=lfc,mobile=11111111111,provinceCode=310000000000,cityCode=310000000000,districtCode=310101000000,address=上海路22号,refereeName=,refereeMobile=1','smart040')

    #u.upgrade_getconsignee('upgrade/consignee','smart040')

    #u.upgrade_checkout('upgrade/checkout','smart040')

    #u.upgrade_deleteRecId('upgrade/delete/','smart040')

    #u.upgrade_submit('upgrade/submit','smart040')

    #u.upgrade_deleteAll('upgrade/delete','smart040')
    #获取商城跳转url

    #u.jumpURL('jumpURL','type=10','smart040')

    #u.allJumpURL('jumpURL','smart040')

    #curent = str(time.time())
    #u.synchronizeStatus('test','gspOrder/synchronizeStatus','orderId=4117;orderStatusList=[{\\"orderStatus\\" : \\"4\\", \\"modifyTime\\":\\"'+ curent + '\\", \\"remark\\":\\"\\",\\"codPayStatus\\" : \\"1\\",\\"expressCompany\\" : \\"\\", \\"logisticsNo\\" : \\"\\",\\"workOrderStatus\\" : \\"1\\",\\"engineerName\\":\\"\\",\\"engineerMobile\\" : \\"\\",\\"installTime\\" :\\"'+ curent + '\\",\\"installAddress\\" : \\"\\"}]')
    #u.synchronizeStatus('test','gspOrder/synchronizeStatus','orderId=10;orderStatusList=[{"orderStatus" : "1", "modifyTime":"'+ curent + '", "remark":"","codPayStatus" : "1","expressCompany" : "", "logisticsNo" : "","workOrderStatus" : "1","engineerName":"","engineerMobile" : "","installTime" :" ' + curent + '","installAddress" : ""}]')
    #u.synchronizeStatus('test','gspOrder/synchronizeStatus','orderId=10;orderStatusList=[{"orderStatus" : "1", "modifyTime":"'+ curent + '", "remark":"","codPayStatus" : "1","expressCompany" : "", "logisticsNo" : "","workOrderStatus" : "1","engineerName":"","engineerMobile" : "","installTime" :" ' + curent + '","installAddress" : ""}]')

    #用户订单API

    #订单状态；例如：ALL-所有 UNFINISHED-未完成 FINISHED-已完成
    #u.order_orderlist('order','page=1,type=ALL','smart040')

    #u.order_orderOrderId('order/','smart040')


    #u.post_order('flow/add','goodsId=1,number=1')
    # u.get(u.mall_test('category','',''))
    # u.get(u.mall_test('flow/add','',''))
    #获取验证码
    # u.post_sms('sms','mobile=13340962986')
    #获取用户订单列表
    #u.put_sms('sms','mobile=13340962986,verifyCode=669508')
    # u.agreements('flow/add','goodsId=13,number=1')
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
