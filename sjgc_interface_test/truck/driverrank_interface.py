#coding:utf-8
from interface_test_utils import utils

__author__ = 'we'

if __name__ == '__main__':
    u = utils.utils()
    # #司机排名
    # u.get(u.create_parameter('demo', 'truck.report.driverRanking', 'resultType=0,startDate=1474128000,endDate=1474534383', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.report.driverRanking', 'resultType=0,startDate=1474128000,endDate=1474534383', 'sd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #未打卡行程列表
    # u.get(u.create_parameter('demo', 'truck.report.unsignedTrips', 'startDate=1474128000,endDate=1474534383', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.report.unsignedTrips', 'startDate=1474128000,endDate=1474534383', 'sd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #司机补签
    # u.get(u.create_parameter('demo', 'truck.report.addUnsignedTrip', 'tripId=28654,driverNumber=E637B0B31BC323A187EB25D76872D523', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.report.addUnsignedTrip', 'tripId=28654,driverNumber=E637B0B31BC323A187EB25D76872D523', 'sd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #司机摘要
    # u.get(u.create_parameter('demo', 'truck.report.driverTotal', 'startDate=1474128000,endDate=1474534383,driverNumber=E637B0B31BC323A187EB25D76872D523', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.report.driverTotal', 'startDate=1474128000,endDate=1474534383,driverNumber=E637B0B31BC323A187EB25D76872D523', 'sd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #单个司机统计列表
    # u.get(u.create_parameter('demo', 'truck.report.driverTotalDetail', 'startDate=1474128000,endDate=1474534383,driverNumber=E637B0B31BC323A187EB25D76872D523,periodType=1,resultType=0', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.report.driverTotalDetail', 'startDate=1474128000,endDate=1474534383,driverNumber=E637B0B31BC323A187EB25D76872D523,periodType=1,resultType=0', 'sd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #单个司机某天事件列表
    # u.get(u.create_parameter('demo', 'truck.report.driverEventDetail', 'startDate=1474546556,endDate=1474534383,driverNumber=E637B0B31BC323A187EB25D76872D523,resultType=0', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.report.driverEventDetail', 'startDate=1474546556,endDate=1474534383,driverNumber=E637B0B31BC323A187EB25D76872D523,resultType=0', 'sd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #司机打卡情况
    # u.get(u.create_parameter('demo', 'truck.report.listDriverSign', 'startDate=1474546556,endDate=1474534383,driverNumber=E637B0B31BC323A187EB25D76872D523', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.report.listDriverSign', 'startDate=1474546556,endDate=1474534383,driverNumber=E637B0B31BC323A187EB25D76872D523', 'sd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #车辆打卡情况
    # u.get(u.create_parameter('demo', 'truck.report.listVehicleDriverSign', 'startDate=1474546556,endDate=1474534383,truckId=CC93307357BC4909C76F38E30649065E', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.report.listVehicleDriverSign', 'startDate=1474546556,endDate=1474534383,truckId=CC93307357BC4909C76F38E30649065E', 'sd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #未知司机
    # u.get(u.create_parameter('demo', 'truck.report.unknownDriverTotal', 'startDate=1474546556,endDate=1474534383,resultType=0', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.report.unknownDriverTotal', 'startDate=1474546556,endDate=1474534383,resultType=1', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.report.unknownDriverTotal', 'startDate=1474546556,endDate=1474534383,resultType=0', '水电费'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #未打卡车辆列表
    # u.get(u.create_parameter('demo', 'truck.report.unsignedTrucks', '', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.report.unsignedTrucks', '', '水电费'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #某段时间的打卡流水 - no
    u.get(u.create_parameter('demo', 'truck.report.listVehicleDriverSignForTrack', 'startDate=1474546556,endDate=1474534383,truckId=CC93307357BC4909C76F38E30649065E', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.report.listVehicleDriverSignForTrack', 'startDate=1474546556,endDate=1474534383,truckId=CC93307357BC4909C76F38E30649065E', '水电费'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
