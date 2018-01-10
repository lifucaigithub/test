#coding:utf-8
from interface_test_utils import utils
__author__ = 'we'

if __name__ == '__main__':
    list = [2643080,
            2643081,
            2643082,
            2643083,
            2643084,
            2643085,
            2643086,
            2643087,
            2643088,
            2643089,
            2643090,
            2643091,
            2643092,
            2643093,
            2643094,
            2643095,
            2643096,
            2643097,
            2643098,
            2643099,
            2643100,
            2643101,
            2643102,
            2643103,
            2643104,
            2643105,
            2643106,
            2643107,
            2643108,
            2643109,
            2643110,
            2643111,
            2643112,
            2643113,
            2643114,
            2643115,
            2643116,
            2643117,
            2643118,
            2643119,
            2643120,
            2643121,
            2643122,
            2643123,
            2643124,
            2643125,
            2643126,
            2643127,
            2643128,
            2643129]
    u = utils.utils()
    # #通知摘要
    # u.get(u.create_parameter('demo', 'truck.notification.getNoticeSummary', '', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.notification.getNoticeSummary', '', 'sd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #通知列表
    # u.get(u.create_parameter('demo', 'truck.notification.getNotice', 'truckid=CC93307357BC4909C76F38E30649065E', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.notification.getNotice', 'truckid=CC93307357BC4909C76F38E30649065E', 'sd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #标记通知已读
    # u.get(u.create_parameter('demo', 'truck.notification.doRead', 'truckid=CC93307357BC4909C76F38E30649065E', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.notification.doRead', 'truckid=CC93307357BC4909C76F38E30649065E', 'sd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #标记所有通知已读
    # u.get(u.create_parameter('demo', 'truck.notification.readAllNotice', '', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.notification.readAllNotice', '', 'sd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #标记司机通知为已读
    # u.get(u.create_parameter('demo', 'truck.notification.doReadByDriver', 'driverid=E637B0B31BC323A187EB25D76872D523', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.notification.doReadByDriver', 'driverid=E637B0B31BC323A187EB25D76872D523', 'sd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #通知推送送达回执确认API
    for i in range(50):
        u.get(u.create_parameter('test', 'truck.notification.updatePushedStatus', 'truckid=5FBC042A907BC269525E7B8897A65667,notification_id=' + str(list[i]) + ',platform=android','smart040'))
    #u.get(u.create_parameter('demo', 'truck.notification.updatePushedStatus', 'truckid=CC93307357BC4909C76F38E30649065E,type=1,eventid=1', 'sd'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
