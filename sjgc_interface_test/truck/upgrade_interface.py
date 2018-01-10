#coding:utf-8
import urllib
import urllib2
__author__ = 'we'

#post方法请求
def upgrade(method):
    base_url = 'http://misc.mop.g7s.chinawayltd.com/rest/service.php'
    appkey = '417759E2B74C0C8C4A00F31225C55310'
    req = urllib2.Request(base_url)
    res = urllib2.urlopen(req, urllib.urlencode({'method': method,"versioncode": 3600, 'appkey': appkey}))
    print res.read().decode('unicode_escape')


if __name__ == '__main__':
    upgrade('mop.applicationinfo.getUpgradeByID')