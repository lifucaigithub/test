#coding:utf-8
import threading

__author__ = 'we'

import time
from  gearman import GearmanClient
import json


server1 = '120.26.214.57:4730'
server2 = '121.41.14.170:4730'
servertest = '172.16.1.14:4730'
serverstress = '172.16.1.102:4730'
serverdemo = '172.16.1.20:4730'


#邮件配置
sendmail = 'email.send'
mail_list = 'wuke@g7.com.cn;tangyuzhou@g7.com.cn;zhangyi_cd@g7.com.cn;huyong@g7.com.cn;lifucai@g7.com.cn;guocuilian@g7.com.cn'
mail = 'lifucai@g7.com.cn'
mail_group1 = 'list.proj.truckmanager@g7.com.cn'
mail_mix = 'list.proj.truckmanager@g7.com.cn;kizitang@163.com;45685137@qq.com'
mail_group2 = 'cd.mobiletest.list@g7.com.cn'
mail_max = 'wuke@g7.com.cn;' \
           'tangyuzhou@g7.com.cn;' \
           'zhangyi_cd@g7.com.cn;' \
           'huyong@g7.com.cn;' \
           'lifucai@g7.com.cn;' \
           'guocuilian@g7.com.cn;' \
           'longyanqiong@g7.com.cn;' \
           'wangjiao@g7.com.cn;' \
           'zhuhongmei@g7.com.cn;' \
           'chenxiaofeng@g7.com.cn;' \
           'xiongpeipei@g7.com.cn;' \
           'gongruijun@g7.com.cn;' \
           'xuyanmei@g7.com.cn;' \
           'tangxiaoyan@g7.com.cn;' \
           'zhuhongmei@g7.com.cn;' \
           'chenxiaofeng@g7.com.cn;' \
           'xiongpeipei@g7.com.cn;' \
           'gongruijun@g7.com.cn;' \
           'xuyanmei@g7.com.cn;' \
           'tangxiaoyan@g7.com.cn;' \
           'zhangxinjie@g7.com.cn;' \
           'wuke@g7.cm.cn;' \
           'tangyuzhou@g7.cm.cn;' \
           'zhangyi_cd@g7.cm.cn;' \
           'huyong@g7.cm.cn;' \
           'ifucai@g7.cm.cn;' \
           'uke@g7.com.cn;' \
           'angyuzhou@g7.com.cn;' \
           'hangyi_cd@g7.com.cn;' \
           'uyong@g7.com.cn;' \
           'liucai@g7.com.cn;' \
           'wke@g7.com.cn;' \
           'tanyuzhou@g7.com.cn;' \
           'zhngyi_cd@g7.com.cn;' \
           'huong@g7.com.cn;' \
           'lifuca@g7.com.cn;' \
           'wuk@g7.com.cn;' \
           'tangyuzho@g7.com.cn;' \
           'zhangyi_c@g7.com.cn;' \
           'huyon@g7.com.cn;' \
           'lifucai@g7.cn;' \
           'tangyuzhou@g7.cn;' \
           'zhangyi_cd@g7.cn;' \
           'huyong@g7.cn;' \
           'lifucai@g7.cn;' \
           'wuke@g7.com;' \
           'tangyuzhou@g7.com;' \
           'zhangyi_cd@g7.com;' \
           'huyong@g7.com;' \
           'lifucai@g7.com'

    #邮件内容
purchase_subject = u'[手机管车线上续单通知][HTWL-SJGC-OL-00000%d]'
purchase_body = u'''
        姓名:王舒舒<br>
        手机号:18081060766<br>
        身份证号码:111111111111111<br>
        安装地区:mailiang<br>
        安装台数:1<br>
        合同编号:HTWL-SJGC-OL-00000648<br>
        签约时间:2016-08-08 14:06:38<br>
        机构名称:smart测试机构<br>
        销售组织:华北事业部<br>
        销售姓名:厉福才测试<br>
        购买类型:手机管车专业版+打卡设备+油感设备<br>'''


feedback_subject = '[G7手机管车客户反馈 - 0000000%d]'
feedback_body = u'''
        机构名称: smart测试机构<br>
        反馈内容:lfc测试<br>
        客户联系方式:13555555555<br>'''


#设备订购
def purchase(i, mail):
    method = sendmail
    start_time = time.time()
    new_client = GearmanClient([serverdemo])
    data = json.dumps(
        {"configuration": "errorReport", "to": mail, "subject": purchase_subject % i, "body": purchase_body})
    current_request = new_client.submit_job(method, data, background=True)
    new_result = current_request.result
    end_time = time.time()
    duration = end_time - start_time
    print '运行时间   %s' % duration, new_result
    return duration


#客户反馈
def feedback(i, mail):
    timestamp = time.localtime(int(time.time()))
    format = '[' + time.strftime("%Y年%m月%d日%H时%M分%S秒", timestamp) + ']'
    #print format
    method = sendmail
    start_time = time.time()
    new_client = GearmanClient([serverdemo])
    data = json.dumps(
        {"configuration": "errorReport", "to": mail, "subject": feedback_subject % i + format,
         "body": feedback_body})
    current_request = new_client.submit_job(method, data, background=True)
    new_result = current_request.result
    end_time = time.time()
    duration = end_time - start_time
    print '运行时间   %s' % duration, new_result
    time.sleep(1)
    return duration


#多线程
threads = []


if __name__ == '__main__':
    t = 0
    times = 5
    for i in range(1, times):
        if i % 2 ==1:
            t += purchase(i, mail)
        else:
            t += feedback(i, mail)
    print '平均时间   %s' % str(t/(times-1))
    # s = 1
    # e = s + 500
    # for i in range(s, e):
    #     t1 = threading.Thread(target=purchase, args=(i, mail))
    #     threads.append(t1)
    #     # t2 = threading.Thread(target=feedback, args=(i, mail_list))
    #     # threads.append(t2)
    # for t in threads:
    #     t.setDaemon(True)
    #     t.start()
    # t.join()
    #purchase(1, mail)



