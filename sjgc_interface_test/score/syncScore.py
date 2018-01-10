#coding:utf-8
from interface_test_utils import utils

__author__ = 'we'

if __name__ == '__main__':
    u = utils.utils()
    #pwd= u.get_MD5('Qq123123')
    u.get(u.create_parameter_syncScore('test', 'external.score.syncScore','type=mileage,scoreDatas={"2008P4":1235.1,"2000PO":1456.8},date=	2016-02-16,signTime=14568712547,sign', 'smart040'))
    #u.get(u.create_parameter('test', 'truck.auth.login', 'username=smart040,password=Qq123123','smart040'))

    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'


