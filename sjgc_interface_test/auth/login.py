#coding:utf-8
from interface_test_utils import utils

__author__ = 'we'

if __name__ == '__main__':
    u = utils.utils()
    pwd= u.encryption('Qq123456')
    u.get(u.create_parameter_login('demo', 'truck.auth.login', 'username=mobileapitest,password=' + pwd))
    #u.get(u.create_parameter('test', 'truck.auth.login', 'username=smart040,password=Qq123123','smart040'))

    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
