#coding:utf-8
from interface_test_utils import utils

__author__ = 'we'

if __name__ == '__main__':
    u = utils.utils()
    #pwd= u.get_MD5('Qq123123')
    u.get(u.create_parameter_siji5('test', 'truck.report.vehicleOilConsumptionTotal','truckId=F3D1D96F9A45CA2D9A942AB39D30EECC,startDate=1498838399,endDate=1496246400', 'siji5'))
    #u.get(u.create_parameter('test', 'truck.auth.login', 'username=smart040,password=Qq123123','smart040'))

    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'


