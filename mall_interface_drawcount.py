#coding:utf-8
from interface_test_utils import utilstest
import  time
import random
from interface_test_utils.changeOrderStatus import ChangeOrderStatus
__author__ = 'li'

if __name__ == '__main__':
    u = utilstest.utils()
    acc = 'smart040'
    cos =ChangeOrderStatus()
    cos.delete_draw_win(acc)
    flag =False
    for i in range(1,1101):
        print "第%d次" %i
        level = u.draw_count('draw',acc)
        if level=='1':
            flag=True
        #print flag
        if(flag==True):
            if i%2==0:
                #print '整除2'
                cos.delete_draw_win(acc)
        elif(flag==False):
            if i%3==0:
                #print '整除3'
                cos.delete_draw_win(acc)
            #u.draw('draw',acc)
