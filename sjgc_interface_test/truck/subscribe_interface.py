#coding:utf-8
from interface_test_utils import utils

__author__ = 'we'

if __name__ == '__main__':
    u = utils.utils()
    # #查询订阅车辆
    # u.get(u.create_parameter('demo', 'truck.appaccount.getSubscribeByTruck', 'truckid=CC93307357BC4909C76F38E30649065E','wuke'))
    # u.get(u.create_parameter('demo', 'truck.appaccount.getSubscribeByTruckn', 'truckid=CC93307357BC4909C76F38E30649065E','wu第三方ke'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #订阅所有车辆
    # u.get(u.create_parameter('demo', 'truck.appaccount.subscribeAllTruck', 'issubscribe=1','wuke'))
    # u.get(u.create_parameter('demo', 'truck.appaccount.subscribeAllTruck', 'issubscribe=0','wuke'))
    # u.get(u.create_parameter('demo', 'truck.appaccount.subscribeAllTruck', 'issubscribe=1','wu第三方ke'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #查询订阅状态
    # u.get(u.create_parameter('demo', 'truck.appaccount.getSubscribeOfAllTruck', '','wuke'))
    # u.get(u.create_parameter('demo', 'truck.appaccount.getSubscribeOfAllTruck', '','wk'))
    # u.get(u.create_parameter('demo', 'truck.appaccount.getSubscribeOfAllTruck', '','wu第三方ke'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #订阅车辆
    # u.get(u.create_parameter('demo', 'truck.appaccount.truckSubscribe', 'truckids=[\"CC93307357BC4909C76F38E30649065E\"]','wuke'))
    # u.get(u.create_parameter('demo', 'truck.appaccount.truckSubscribe', 'truckids=[\"CC93307357BC4909C76F38E30649065E\"]','wu第三方ke'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #取消订阅车辆
    # u.get(u.create_parameter('demo', 'truck.appaccount.truckUnsubscribe', 'truckids=[\"CC93307357BC4909C76F38E30649065E\"]','wuke'))
    # u.get(u.create_parameter('demo', 'truck.appaccount.truckUnsubscribe', 'truckids=[\"CC93307357BC4909C76F38E30649065E\"]','wu第三方ke'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #订阅和取消订阅车辆
    u.get(u.create_parameter('demo', 'truck.appaccount.subscribeAndUnSubscribe', '', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.appaccount.subscribeAndUnSubscribe', '', 'wu第三方ke'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
