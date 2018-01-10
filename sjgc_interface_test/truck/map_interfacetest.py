#coding:utf-8
from interface_test_utils import utils

__author__ = 'we'

if __name__ == '__main__':
    u = utils.utils()
    # #停留点
    # u.get(u.create_parameter('demo', 'truck.map.getStopPoints', 'truckid=CC93307357BC4909C76F38E30649065E,from=1474387200,to=1474442611', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.map.getStopPoints', 'truckid=CC93307357BC4909C76F38E30649065E,from=1474387200,to=1474442611', 'sd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #轨迹点
    # u.get(u.create_parameter('demo', 'truck.map.getHistoryPoint', 'truckid=CC93307357BC4909C76F38E30649065E,from=1474387200,to=1474442611', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.map.getHistoryPoint', 'truckid=CC93307357BC4909C76F38E30649065E,from=1474387200,to=1474442611', 'dd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #获取标注点
    # u.get(u.create_parameter('demo', 'truck.map.getMarkerList', 'truckid=CC93307357BC4909C76F38E30649065E,from=1474387200,to=1474442611', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.map.getMarkerList', 'truckid=CC93307357BC4909C76F38E30649065E,from=1474387200,to=1474442611', 'wk'))
    # u.get(u.create_parameter('demo', 'truck.map.getMarkerList', 'truckid=CC93307357BC4909C76F38E30649065E,from=1474387200,to=1474442611', 'dd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #经纬度解析
    # u.get(u.create_parameter('demo', 'truck.map.geoCode', 'lnglats=[{\"longitude\":117.2317635,\"latitude\":39.0207755},{\"longitude\":116.2317635,\"latitude\":38.0207755}]', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.map.geoCode', 'truckid=CC93307357BC4909C76F38E30649065E,from=1474387200,to=1474442611', 'dd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #车辆ID获取坐标
    # u.get(u.create_parameter('demo', 'truck.map.getGpsLocate', 'truckid=CC93307357BC4909C76F38E30649065E,timestamp=1474387200', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.map.getGpsLocate', 'truckid=CC93307357BC4909C76F38E30649065E,timestamp=1474387200', 'dd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #获取城市代码
    # u.get(u.create_parameter('demo', 'truck.map.getAreaCode', '', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.map.getAreaCode', '', 'wk'))
    # u.get(u.create_parameter('demo', 'truck.map.getAreaCode', '', 'dd'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #新增地图标注
    u.get(u.create_parameter('demo', 'truck.map.saveMarker', '', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.map.getAreaCode', '', 'wk'))
    u.get(u.create_parameter('demo', 'truck.map.getAreaCode', '', 'dd'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #删除地图标注
    u.get(u.create_parameter('demo', 'truck.map.deleteMarker', '', 'wuke'))
    u.get(u.create_parameter('demo', 'truck.map.getAreaCode', '', 'wk'))
    u.get(u.create_parameter('demo', 'truck.map.getAreaCode', '', 'dd'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'

