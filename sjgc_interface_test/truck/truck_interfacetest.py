#coding:utf-8
__author__ = 'we'
from interface_test_utils import utils

if __name__ == '__main__':
    u = utils.utils()
    #登录
    u.get(u.create_parameter('demo', 'truck.auth.login', 'username=wuke,password=Qq123456', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.auth.login', 'username=wk,password=Qq123456', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.auth.login', 'username=demotang,password=Qq123456', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.auth.login', 'username=wk,password=Qq1256', 'wuke'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #车辆列表
    u.get(u.create_parameter('demo', 'truck.truck.truckList', '', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.truck.truckList', '', 'wk'))
    u.get(u.create_parameter('demo', 'truck.truck.truckList', '', 'sdf'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #车辆详情
    u.get(u.create_parameter('demo', 'truck.truck.truckDetail', 'truckid=CC93307357BC4909C76F38E30649065E', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.truck.truckList', 'truckid=CC93307357BC4909C76F38E30649065E', 'sdf'))
    u.get(u.create_parameter('demo', 'truck.truck.truckList', 'truckid=', 'wuke'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #车辆实时状态
    u.get(u.create_parameter('demo', 'truck.truck.currentState', '', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.truck.currentState', '', 'sdf'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #里程查询
    u.get(u.create_parameter('demo', 'truck.truck.getTruckDailyMileage', '', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.truck.getTruckDailyMileage', '', 'sdf'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #获取时间内里程
    u.get(u.create_parameter('demo', 'truck.truck.getTruckDailyMileage', 'from=1474387200,to=1474442611,truckid=CC93307357BC4909C76F38E30649065E', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.truck.getTruckDailyMileage', 'from=1474387200,to=1474442611,truckid=CC93307357BC4909C76F38E30649065E', 'sdf'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #关注车辆
    u.get(u.create_parameter('demo', 'truck.truck.doFollow', 'truckid=CC93307357BC4909C76F38E30649065E', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.truck.doFollow', 'truckid=CC93307357BC4909C76F38E30649065E', 'sdf'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #取消关注车辆
    u.get(u.create_parameter('demo', 'truck.truck.doUnfollow', 'truckid=CC93307357BC4909C76F38E30649065E', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.truck.doUnfollow', 'truckid=CC93307357BC4909C76F38E30649065E', 'sdf'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #车队汇总
    u.get(u.create_parameter('demo', 'truck.truck.getTruckSummary', '', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.truck.getTruckSummary', '', 'wk'))
    u.get(u.create_parameter('demo', 'truck.truck.getTruckSummary', '', 'sdf'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #更新车辆别名
    u.get(u.create_parameter('demo', 'truck.truck.updateAliasname', 'truckid=CC93307357BC4909C76F38E30649065E,aliasname=成渝货运', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.truck.updateAliasname', 'truckid=CC93307357BC4909C76F38E30649065E,aliasname=成渝货运', 'sdf'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #下发指令
    u.get(u.create_parameter('demo', 'truck.truck.tmpLocTrace', 'truckid=CC93307357BC4909C76F38E30649065E,interval=1,validity=60', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.truck.tmpLocTrace', 'truckid=CC93307357BC4909C76F38E30649065E,interval=1,validity=60', 'sdf'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #油耗信息汇总
    u.get(u.create_parameter('demo', 'truck.truck.getFuelSummary', 'truckid=CC93307357BC4909C76F38E30649065E,from=1474387200,to=1474442611', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.truck.getFuelSummary', 'truckid=CC93307357BC4909C76F38E30649065E,from=1474387200,to=1474442611', 'sdf'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #加油量列表
    u.get(u.create_parameter('demo', 'truck.truck.getAddFuelList', 'truckid=CC93307357BC4909C76F38E30649065E,from=1474387200,to=1474442611', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.truck.getAddFuelList', 'truckid=CC93307357BC4909C76F38E30649065E,from=1474387200,to=1474442611', 'sdf'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #熄火少油列表
    u.get(u.create_parameter('demo', 'truck.truck.getLostFuelList', 'truckid=CC93307357BC4909C76F38E30649065E', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.truck.getLostFuelList', 'truckid=CC93307357BC4909C76F38E30649065E', 'sdf'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #油量监控
    u.get(u.create_parameter('demo', 'truck.truck.getFuelTrend', 'truckid=CC93307357BC4909C76F38E30649065E', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.truck.getFuelTrend', 'truckid=CC93307357BC4909C76F38E30649065E', 'sdf'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #查询车辆设备安装情况
    u.get(u.create_parameter('demo', 'truck.truck.getDeviceByTruck', 'truckid=CC93307357BC4909C76F38E30649065E', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.truck.getDeviceByTruck', 'truckid=CC93307357BC4909C76F38E30649065E', 'sdf'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #按车辆查询车辆设备开通产品类型
    u.get(u.create_parameter('demo', 'truck.truck.getProductTypeByTruck', 'truckid=CC93307357BC4909C76F38E30649065E', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.truck.getProductTypeByTruck', 'truckid=CC93307357BC4909C76F38E30649065E', 'sdf'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #设置主副驾司机
    u.get(u.create_parameter('demo', 'truck.truck.setDriverByTruck', 'truckid=CC93307357BC4909C76F38E30649065E,driverid=E637B0B31BC323A187EB25D76872D523,bindtrucktype=1', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.truck.setDriverByTruck', 'truckid=CC93307357BC4909C76F38E30649065E,driverid=E637B0B31BC323A187EB25D76872D523,bindtrucktype=2', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.truck.setDriverByTruck', 'truckid=CC93307357BC4909C76F38E30649065E,driverid=E637B0B31BC323A187EB25D76872D523,bindtrucktype=2', 'sdfe'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #车队是否有安装油耗设备的车辆
    u.get(u.create_parameter('demo', 'truck.truck.hasOilDeviceInVehicle', '', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.truck.hasOilDeviceInVehicle', '', 'sdfe'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #某天运转效率
    u.get(u.create_parameter('demo', 'truck.truck.speedImage', 'truckid=CC93307357BC4909C76F38E30649065E,dateTime=1474534383', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.truck.speedImage', 'truckid=CC93307357BC4909C76F38E30649065E,dateTime=1474534383', 'sdfe'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #单车运转效率
    u.get(u.create_parameter('demo', 'truck.truck.speedImages', 'truckId=CC93307357BC4909C76F38E30649065E,startDate=1474128000,endDate=1474534383', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.truck.speedImages', 'truckId=CC93307357BC4909C76F38E30649065E,startDate=1474128000,endDate=1474534383', 'sdfe'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #获取车辆信息
    u.get(u.create_parameter('demo', 'truck.truck.getTruckInfo', 'truckid=CC93307357BC4909C76F38E30649065E', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.truck.getTruckInfo', 'truckid=CC93307357BC4909C76F38E30649065E', 'sdfe'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #车辆配置信息列表：车长、箱型
    u.get(u.create_parameter('demo', 'truck.truck.truckConfig', '', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.truck.truckConfig', '', 'sdfe'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #查询车辆违章简要列表
    u.get(u.create_parameter('demo', 'truck.truck.listViolation', '', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.truck.listViolation', '', 'sdfe'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #违章车辆查询城市黑名单列表
    u.get(u.create_parameter('demo', 'truck.truck.carViolationBlackCity', '', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.truck.carViolationBlackCity', '', 'sdfe'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #车辆品牌查询接口
    u.get(u.create_parameter('demo', 'truck.truck.searchBrand', 'model=BJ1037', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.truck.searchBrand', 'model=BJ1037', 'sdfe'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #违章详情
    u.get(u.create_parameter('demo', 'truck.truck.detailViolation', 'truckid=FA4378A047B16F570564A3E70A59BBCE,vehicleId=139862847', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.truck.detailViolation', 'truckid=FA4378A047B16F570564A3E70A59BBCE,vehicleId=139862847', 'sdfe'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #编辑车辆基础信息
    u.get(u.create_parameter('demo', 'truck.truck.updateTruckInfo', 'truckid=FA4378A047B16F570564A3E70A59BBCE,queryAreaCode=130900000000,engineno=78100033,vehicleno=LGAX4C354E3024073', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.truck.updateTruckInfo', 'truckid=FA4378A047B16F570564A3E70A59BBCE,queryAreaCode=130900000000,engineno=78100033,vehicleno=LGAX4C354E3024073', 'sdfe'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #登出
    u.get(u.create_parameter('demo', 'truck.auth.logout', '', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.auth.logout', '', 'wk'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'

