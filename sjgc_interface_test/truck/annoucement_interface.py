#coding:utf-8
from interface_test_utils import utils

__author__ = 'we'

if __name__ == '__main__':
    u = utils.utils()
    # #获取公告
    # u.get(u.create_parameter('demo', 'truck.announcement.announcement', '', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.announcement.announcement', '', 'sd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #获取公告
    u.get(u.create_parameter('demo', 'truck.announcement.announcement', '', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.announcement.announcement', '', 'sd'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
