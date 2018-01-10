#coding:utf-8
import random
import time
from interface_test_utils import utils
__author__ = 'we'


def get_mileage_score(ENV, orgcode):
    date = u.get_yesterday_date()
    signTime = u.get_timestamp()
    mileage = u.get_random_num()
    data = 'type=mileage,scoreDatas={\\"' + orgcode + '\\":' + mileage + '},date=' + date + ",signTime=" + signTime
    u.get(u.third_create_parameter(ENV, 'external.score.syncScore', data))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'


def get_etc_score(ENV, uid):
    signTime = str(int(time.time()))
    consume = str(random.randint(1000, 99999))
    paysn = u.get_32_string()
    data = 'type=etc,uid=' + uid + ',consume=' + consume + ',paysn=' + paysn + ",signTime=" + signTime
    u.get(u.third_create_parameter(ENV, 'external.score.syncScore', data))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'


if __name__ == '__main__':
    u = utils.utils()
    # #登录积分
    # u.get(u.create_parameter('demo', 'truck.score.loginScore', '', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.score.loginScore', '', 'tangdemo'))
    # u.get(u.create_parameter('demo', 'truck.score.loginScore', '', 'sd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #获取用户积分
    # u.get(u.create_parameter('demo', 'truck.score.getScore', '', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.score.getScore', '', 'demotang'))
    # u.get(u.create_parameter('demo', 'truck.score.getScore', '', 'sd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #获取当日积分明细
    # u.get(u.create_parameter('demo', 'truck.score.getDetails', 'timestamp=1474534383', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.score.getDetails', 'timestamp=1474534383', 'demotang'))
    # u.get(u.create_parameter('demo', 'truck.score.getDetails', 'timestamp=1474534383', 'sd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #查询是否有会员卡
    # u.get(u.create_parameter('demo', 'truck.score.isGotCard', '', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.score.isGotCard', '', 'demotang'))
    # u.get(u.create_parameter('demo', 'truck.score.isGotCard', '', 'sd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #是否关注了微信公众号
    # u.get(u.create_parameter('demo', 'truck.score.isFollowWechat', 'unionid=oTmj8s3g2xu3cp1KER7DGYss-32Y', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.score.isFollowWechat', 'unionid=oTmj8s3g2xu3cp1KER7DGYss-32Y', 'demotang'))
    # u.get(u.create_parameter('demo', 'truck.score.isFollowWechat', 'unionid=oTmj8s3g2xu3cp1KER7DGYss-32Y', 'sd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #查询微信是否已经绑定手机管车帐号
    # u.get(u.create_parameter('demo', 'truck.score.isUsedWechat', 'unionid=oTmj8s3g2xu3cp1KER7DGYss-32Y', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.score.isUsedWechat', 'unionid=oTmj8s3g2xu3cp1KER7DGYss-32Y', 'demotang'))
    # u.get(u.create_parameter('demo', 'truck.score.isUsedWechat', 'unionid=oTmj8s3g2xu3cp1KER7DGYss-32Y', 'sd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #绑定会员卡
    # u.get(u.create_parameter('demo', 'truck.score.bindCard', 'unionid=or9HosgcXBjA7F302CdboS7wUBYI,truename=朵朵,tel=19203,sex=3,baithday=123', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.score.bindCard', 'unionid=or9HosgcXBjA7F302CdboS7wUBYI,truename=朵朵,tel=19203,sex=3,baithday=123', 'demotang'))
    # u.get(u.create_parameter('demo', 'truck.score.bindCard', 'unionid=or9HosgcXBjA7F302CdboS7wUBYI,truename=朵朵,tel=19203,sex=3,baithday=123', 'sd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #同步积分 -  里程积分
    # 20000G - demo - CAN测试组
    get_mileage_score('demo', '20000G')
    #同步积分 -  ETC消费
    #demo - demotang - D72CE1FCF800E804CC4A4DB444FE5B81
    # get_etc_score('demo', 'D72CE1FCF800E804CC4A4DB444FE5B81')