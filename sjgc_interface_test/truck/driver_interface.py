#coding:utf-8
from interface_test_utils import utils

__author__ = 'we'

if __name__ == '__main__':
    u = utils.utils()
    # #编辑司机
    # u.get(u.create_parameter('demo', 'truck.driver.saveDriver', 'drivername=阿斯顿马丁1,id=E637B0B31BC323A187EB25D76872D523', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.driver.saveDriver', 'drivername=阿斯顿马丁1,id=E637B0B31BC323A187EB25D76872D523', 'sdf'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #读取司机列表
    # u.get(u.create_parameter('demo', 'truck.driver.getDriverList', '', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.driver.getDriverList', '', 'sdf'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #读取一条司机信息
    # u.get(u.create_parameter('demo', 'truck.driver.getDriver', 'id=E637B0B31BC323A187EB25D76872D523', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.driver.getDriver', 'id=E637B0B31BC323A187EB25D76872D523', 'sdf'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #删除一条司机信息
    u.get(u.create_parameter('demo', 'truck.driver.deleteDriver', 'id=E637B0B31BC323A187EB25D76872D523', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.driver.deleteDriver', 'id=E637B0B31BC323A187EB25D76872D523', 'sdf'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
