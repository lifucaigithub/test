#coding:utf-8
from interface_test_utils import utils

__author__ = 'we'

if __name__ == '__main__':
    u = utils.utils()
    # #获取app图片
    # u.get(u.create_parameter('demo', 'truck.appimage.getAppImage', 'type=1', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.appimage.getAppImage', 'type=2', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.appimage.getAppImage', 'type=3', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.appimage.getAppImage', 'type=4', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.appimage.getAppImage', 'type=5', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.appimage.getAppImage', 'type=0', 'wuke'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #获取管车图标 - {"code":104,"message":"查询应用配置失败"}
    u.get(u.create_parameter('demo', 'truck.secretinfo.getAppOrder', 'applevel=6', 'wuke'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'