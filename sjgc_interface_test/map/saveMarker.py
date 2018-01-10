#coding:utf-8
from interface_test_utils import utils

__author__ = 'we'

if __name__ == '__main__':
    u = utils.utils()
    #pwd= u.get_MD5('Qq123123')
    u.get(u.create_parameter('test', 'truck.map.saveMarker','lng=116.31767,lat=36.31767,lnglats=120.297341,radius=100,name=test', 'smart040'))
    #u.get(u.create_parameter('test', 'truck.auth.login', 'username=smart040,password=Qq123123','smart040'))

    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'


