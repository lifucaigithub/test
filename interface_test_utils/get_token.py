#coding:utf-8
__author__ = 'we'
import MySQLdb as m
import paramiko

from interface_test_utils.config import Config


class GetToken(Config):
    #获取test环境token
    def get_test_token(self, username):
        target = ''
        token_query = "select api_token from cat_truck_manager.truck_app_authorization WHERE user_" \
                      "info LIKE '%\"username\":\"" + username + "\"%';"


        con = m.connect(user=Config.TUSER, db=Config.TYPE, passwd=Config.TPASSWD, host=Config.THOST,
                        charset=Config.CHARSET)
        cursor = con.cursor()
        cursor.execute(token_query)
        result = cursor.fetchone()

        if result is not None:
            target = result[0]
        cursor.close()
        con.close()
        print 'token:',target
        return target
    def get_testsiji5_token(self, username):
        target = ''
        token_query = "select api_token from cat_truck_manager.truck_app_authorization WHERE user_" \
                      "info LIKE '%\"username\":\"" + username + "\"%'and uid ='901D6C7E3A6099E8EA0E87F6E86A9C5E' ;"

        con = m.connect(user=Config.TUSER, db=Config.TYPE, passwd=Config.TPASSWD, host=Config.THOST,
                        charset=Config.CHARSET)
        cursor = con.cursor()
        cursor.execute(token_query)
        result = cursor.fetchone()

        if result is not None:
            target = result[0]
        cursor.close()
        con.close()
        print 'token:',target
        return target
    #获取demo环境token
    def get_demo_token(self, user):
        key = paramiko.RSAKey.from_private_key_file(Config.PK_PATH, Config.PAWSSWORD)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(Config.HOSTNAME, Config.PORT, Config.USERNAME, pkey=key)
        target = ''
        token_query = "select api_token from cat_truck_manager.truck_app_authorization WHERE " \
                      "user_info LIKE '%\"username\":\"" + user + "\"%';"
        con = m.connect(user=Config.DUSER, db=Config.TYPE, passwd=Config.DPASSWD, host=Config.DHOST,
                        charset=Config.CHARSET)
        cursor = con.cursor()
        cursor.execute(token_query)
        result = cursor.fetchone()
        if result is not None:
            target = result[0]
        cursor.close()
        con.close()
        ssh.close()
        print target
        return target

    def get_demo_token(self, user):
        key = paramiko.RSAKey.from_private_key_file(Config.PK_PATH, Config.PAWSSWORD)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(Config.HOSTNAME, Config.PORT, Config.USERNAME, pkey=key)
        target = ''
        token_query = "select api_token from cat_truck_manager.truck_app_authorization WHERE " \
                      "user_info LIKE '%\"username\":\"" + user + "\"%';"
        con = m.connect(user=Config.DUSER, db=Config.TYPE, passwd=Config.DPASSWD, host=Config.DHOST,
                        charset=Config.CHARSET)
        cursor = con.cursor()
        cursor.execute(token_query)
        result = cursor.fetchone()
        if result is not None:
            target = result[0]
        cursor.close()
        con.close()
        ssh.close()
        print target
        return target

if __name__ == '__main__':
    aa = GetToken()
    #aa.get_test_token('wuke')
    aa.get_testsiji5_token('siji5')
    #aa.get_demo_token('wuke')