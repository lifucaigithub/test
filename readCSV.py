__author__ = 'Elvis'
#coding:utf-8
import  csv
import time
csvFile = open("export.csv", "r")
reader = csv.DictReader(csvFile)
data = []
for item in reader:
    print item
    data.append(item['\xb5\xb1\xc7\xb0\xca\xb1\xbc\xe4'])
    #data.append(item)
print data
for ti in data:
    time.strptime(ti,'%Y/%m/%d %H:%M')
    time.struct_time(tm_year=2011, tm_mon=9, tm_mday=27, tm_hour=10, tm_min=50,  tm_wday=1, tm_yday=270, tm_isdst=-1)

#将"2011-09-28 10:00:00"转化为时间戳

    time.mktime(time.strptime(ti,'%Y/%m/%d %H:%M'))
print data
