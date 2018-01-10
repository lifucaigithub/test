#coding:utf-8
from interface_test_utils import utils

__author__ = 'we'

if __name__ == '__main__':
    u = utils.utils()
    #pwd= u.get_MD5('Qq123123')
    u.get(u.create_parameter('test', 'truck.notification.doReadByDriver','driverid=be2ff38296ed6a9960773650431d7c91', 'smart040'))
    #u.get(u.create_parameter('test', 'truck.auth.login', 'username=smart040,password=Qq123123','smart040'))

    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'


