# coding=utf-8
import os
import re
import ConfigParser
import os.path
import time
import sys
import unicodedata
reload(sys)
sys.setdefaultencoding('utf8')

def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir.decode('gbk'))
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            #如果需要忽略某些文件夹，使用以下代码
            #if s == "xxx":
                #continue
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)
    return fileList

# config = ConfigParser.ConfigParser()
# file_path = 'D:\\daily\\config.ini'
# config.read(file_path)
# namelist = config.get("daily", "namelist")
# print (namelist)
rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
today_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
dir = os.path.dirname(os.path.abspath('.')) + '\\daily'
daily_path = dir + '\\' + today_time + '\\'
config_path = dir + '\\config.ini'
w_path = daily_path + rq + '.log'

w = open(w_path,'w')

f = open(config_path)
namelist = []
w.write(u"名单列表："),
for line in f:
    w.write(line.strip()),
    w.write(' '),
    # print(type(line))
    namelist.append(line.strip())
f.close()

file_list = dir + '\\' + today_time + '\\'
list = GetFileList(file_list, [])
last = []
for e in list:
    # print e
    e = os.path.basename(e)
    # e = u'平台支持中心-平台技术部-王一-日报-20180412.xlsx'
    # all_symptom = re.sub(u'', '', e)
    # e = re.split(u'平台支持中心-平台技术部-|-日报-20180412.xlsx',e)
    e = re.sub(u"(?isu)平台支持中心-平台技术部-", "", e)
    e = re.sub("[A-Za-z0-9\!\%\[\]\,\。\.\-]", "", e)
    e = re.sub(u"(?isu)日报", "", e)
    last.append(e)
w.write(u"\n\n最终提交的名单:")
for lastname in last:
    w.write(lastname),
    w.write(' '),
    # print(type(lastname))

w.write(u'\n\n未提交的名单：')
for m in namelist:
    m = m.decode("utf-8")
    # print(type(i))
    if m in last:
        pass
    else:
        w.write(m),
        w.write(' '),

w.close()
