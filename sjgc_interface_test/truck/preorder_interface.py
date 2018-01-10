#coding:utf-8
from interface_test_utils import utils

__author__ = 'we'

if __name__ == '__main__':
    u = utils.utils()
    # #
    # u.get(u.create_parameter('demo', 'truck.appapi.createPreorder', 'username=测试,mobile=13888888888,identitycard=111111111111111,address=成都,number=2,type=1', 'wuke'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #
    # u.get(u.create_parameter('demo', 'truck.appapi.createLoginPreorder', 'username=测试,mobile=13888888888,identitycard=111111111111111,address=成都,number=2,type=1', 'wuke'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #
    u.get(u.create_parameter('demo', 'truck.appapi.getPurchasePackageUrl', 'type=0', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.appapi.getPurchasePackageUrl', 'type=1', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.appapi.getPurchasePackageUrl', 'type=2', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.appapi.getPurchasePackageUrl', 'type=3', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.appapi.getPurchasePackageUrl', 'type=4', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.appapi.getPurchasePackageUrl', 'type=5', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.appapi.getPurchasePackageUrl', 'type=6', 'wuke'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
