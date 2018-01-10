#coding:utf-8
from interface_test_utils import utils

__author__ = 'we'

if __name__ == '__main__':
    u = utils.utils()
    # #消息汇总
    # u.get(u.create_parameter('demo', 'truck.message.getMessageSummary', 'startid=1,endid=5000000','wuke'))
    # u.get(u.create_parameter('demo', 'truck.message.getMessageSummary', 'startid=1,endid=5000000','wu第三方ke'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #消息明细
    # u.get(u.create_parameter('demo', 'truck.message.getMessageList', 'type=1','wuke'))
    # u.get(u.create_parameter('demo', 'truck.message.getMessageList', 'type=2','wuke'))
    # u.get(u.create_parameter('demo', 'truck.message.getMessageList', 'type=3','wuke'))
    # u.get(u.create_parameter('demo', 'truck.message.getMessageList', 'type=4','wuke'))
    # u.get(u.create_parameter('demo', 'truck.message.getMessageList', 'type=5','wuke'))
    # u.get(u.create_parameter('demo', 'truck.message.getMessageList', 'type=6','wuke'))
    # u.get(u.create_parameter('demo', 'truck.message.getMessageList', 'type=6','dsf'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #删除消息
    # #不能删除一种类型 {"code":103,"message":"更新未读消息数失败"}
    # u.get(u.create_parameter('demo', 'truck.message.removeMessage', 'type=4','wuke'))
    # u.get(u.create_parameter('demo', 'truck.message.removeMessage', 'type=6','dsf'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #获取用户未读消息总数
    # u.get(u.create_parameter('demo', 'truck.message.getUnreadMessageCount', '','wuke'))
    # u.get(u.create_parameter('demo', 'truck.message.getUnreadMessageCount', '','dsf'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #根据ID获取一个消息
    # u.get(u.create_parameter('demo', 'truck.message.getMessageById', 'id=1077','wuke'))
    # u.get(u.create_parameter('demo', 'truck.message.getMessageById', 'id=1077','dsf'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #第三方消息发送
    #u.get(u.third_create_parameter('test', 'external.message.sendMessage', 'message=3,title=lfchh,uid=79F4ED6BE54383D3D866B969002DB159,description=11111111111111111,linktext=阅读全文最多10个字符,linktype=1,linkurl=www.baidu.com'))
    #uri = 'http://test.truckmanager.g7s.chinawayltd.com/external.php?'
    u.post(u.third_create_parameter1('test'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'