#coding:utf-8
__author__ = 'we'
import MySQLdb as m
import paramiko

from interface_test_utils.config import Config


class ChangeOrderStatus(Config):
    #获取test环境token
    def change_order_status(self, orderSn):

        status_query = "update ecshop3.ecs_order_info set pay_status='2' where order_sn= '" + orderSn + "';"
        con = m.connect(user=Config.ECUser, db=Config.TYPE, passwd=Config.ECPassword, host=Config.ECHost,
                        charset=Config.CHARSET)
        cursor = con.cursor()
        cursor.execute(status_query)

    def delete_draw_win(self,username):
        user_id = self.get_user_id(username)
        #delete_query = "delete from ecshop3.ecs_draw_win where user_id= '" + str(user_id)+ "';"
        delete_query = "delete from ecshop3.ecs_draw_win where user_id= '" + str(user_id)+ "' and prize_level!=1;"
        #print delete_query
        con = m.connect(user=Config.ECUser, db=Config.TYPE, passwd=Config.ECPassword, host=Config.ECHost,
                        charset=Config.CHARSET)
        cursor = con.cursor()
        cursor.execute(delete_query)

    def get_user_id(self, username):
        target = ''
        userid_query = "select user_id from ecshop3.ecs_users where user_name= '" + username + "';"
        #print userid_query
        con = m.connect(user=Config.ECUser, db=Config.TYPE, passwd=Config.ECPassword, host=Config.ECHost,
                        charset=Config.CHARSET)
        cursor = con.cursor()
        cursor.execute(userid_query)
        result = cursor.fetchone()

        if result is not None:
            target = result[0]
        cursor.close()
        con.close()
        #print 'userid:',target
        return target
    def delete_order(self,orderSn):

        delete_query = "delete from ecshop3.ecs_order_info where order_sn= '" +orderSn+ "';"
        #print delete_query
        con = m.connect(user=Config.ECUser, db=Config.TYPE, passwd=Config.ECPassword, host=Config.ECHost,
                        charset=Config.CHARSET)
        cursor = con.cursor()
        cursor.execute(delete_query)


if __name__ == '__main__':
    aa = ChangeOrderStatus()
    #aa.get_test_token('wuke')
    #aa.change_order_status('G7mall-2017071472207')
    #aa.get_user_id('smart040')
    #aa.delete_draw_win('smart040')
    aa.delete_order('G7mall-2017071732377')