#coding:utf-8
from interface_test_utils import utils

__author__ = 'we'

if __name__ == '__main__':
    u = utils.utils()
    # #获取用户信息
    # u.get(u.create_parameter('demo', 'truck.user.getUserInfo', '', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.user.getUserInfo', '', 'sd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #用户反馈
    # u.get(u.create_parameter('demo', 'truck.user.saveFeedback', 'content=吴可demo测试一下,contactinfo=13888888888', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.user.saveFeedback', 'content=吴可demo测试一下,contactinfo=13888888888', 'sd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #获取用户身份证号码(RSA加密)API
    # u.get(u.create_parameter('demo', 'truck.user.getRsaIdcardNumber', '', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.user.getRsaIdcardNumber', '', 'sd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #生成分享链接
    # u.get(u.create_parameter('demo', 'truck.user.saveShareInfo', 'truckid=FA4378A047B16F570564A3E70A59BBCE,sharetype=1,lng=104.293829,lat=30.372893', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.user.saveShareInfo', 'truckid=FA4378A047B16F570564A3E70A59BBCE,sharetype=1,lng=104.293829,lat=30.372893', 'sd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #修改密码
    # u.get(u.create_parameter('demo', 'truck.user.changePassword', 'username=wuke,password=Qq123456,newPassword=Qq123456,newPasswordAgain=Qq123456', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.user.changePassword', 'username=wuke,password=Qq123456,newPassword=Qq123456,newPasswordAgain=Qq123456','sd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #发送验证码
    # u.get(u.create_parameter('demo', 'truck.user.getMobileRandnum', 'mobile=18980863517,username=wuke', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.user.getMobileRandnum', 'mobile=18980863517,username=wuke','sd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #绑定手机号
    # u.get(u.create_parameter('demo', 'truck.user.bindMobileForUser', 'mobilerandnum=130580,mrt=7501FD9D4CF56760B2E7132EB858DE25', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.user.bindMobileForUser', 'mobilerandnum=130580,mrt=7501FD9D4CF56760B2E7132EB858DE25','sd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #用户找回密码发送验证码
    # u.get(u.create_parameter('demo', 'truck.user.getMobileRandnumByUsername', 'username=wuke', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.user.getMobileRandnumByUsername', 'username=wuke','sd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #检查验证码是否正确
    # u.get(u.create_parameter('demo', 'truck.user.checkMobileRandnum', 'mobilerandnum=130580,mrt=7501FD9D4CF56760B2E7132EB858DE25', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.user.checkMobileRandnum', 'mobilerandnum=234,mrt=fferere', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.user.checkMobileRandnum', 'mobilerandnum=130580,mrt=7501FD9D4CF56760B2E7132EB858DE25','sd'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #根据验证码修改密码
    # u.get(u.create_parameter('demo', 'truck.user.changePasswordByMobile', 'newpassword=Qq123456,mrt=7501FD9D4CF56760B2E7132EB858DE25', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.user.changePasswordByMobile', 'newpassword=Qq123456,mrt=7501FD9D4CF56760B2E7132EB858DE25', 'sdf'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    # #按用户查询用户开通产品类型
    # u.get(u.create_parameter('demo', 'truck.user.getProductTypeByUser', '', 'wuke'))
    # u.get(u.create_parameter('demo', 'truck.user.getProductTypeByUser', '', 'wk'))
    # u.get(u.create_parameter('demo', 'truck.user.getProductTypeByUser', '', 'wuksfe'))
    # print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
    #用户是否绑定了手机
    #print u.create_parameter('test', 'truck.truck.truckList', '', 'smart040')
    u.get(u.create_parameter('test', 'truck.truck.truckList', '', 'smart040'))
    #u.get(u.create_parameter('demo', 'truck.user.isBindedMobile', '', 'wk'))
    #u.get(u.create_parameter('demo', 'truck.user.isBindedMobile', '', 'wusdfke'))
    print '- - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - -'
