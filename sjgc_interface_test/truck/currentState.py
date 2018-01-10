__author__ = 'Elvis'
#coding:utf-8
from interface_test_utils import utils

if __name__ == '__main__':
    u = utils.utils()
    #登录
    u.get(u.create_parameter('test', 'truck.truck.currentState', 'gpsnos=90000010,11001176', 'smart029'))