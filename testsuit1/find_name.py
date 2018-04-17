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
dir = os.getcwd()
# dir = 'D:\\daily'
daily_path = dir + '\\' + today_time + '\\'
config_path = dir + '\\config.ini'
w_path = rq + '.log'

w = open(w_path, 'w')

f = open(config_path, 'r')
# namelist = f.readlines()
namelist = []
w.write(u"名单"),
for line in f:
    line = line.strip()
    w.write(line),
    w.write(' '),
    # print(type(line))
    namelist.append(line)
len_namelist = len(namelist)-1
if len_namelist < 0:
    len_namelist = 0
w.write('[%d]' % len_namelist)
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

    # 使用中
    # e = re.sub(u"(?isu)平台支持中心-平台技术部-", "", e)
    # e = re.sub(u"(?isu)平台支持中心-平台产品部-", "", e)
    # e = re.sub(u"(?isu)平台支持中心-平台运营部-", "", e)
    # e = re.sub(u"(?isu)平台支持中心", "", e)
    # e = re.sub(u"(?isu)平台技术部", "", e)
    # e = re.sub(u"(?isu)平台产品部", "", e)
    # e = re.sub(u"(?isu)平台运营部", "", e)
    # e = re.sub("[A-Za-z0-9\!\%\[\]\,\。\.\-\(\)]", "", e)
    # e = re.sub(u"(?isu)日报", "", e)
    # e = re.sub(u"(?isu)副本", "", e)
    # e = re.sub(" ", "", e)
    # 使用中

    # 新的匹配
    e = re.sub(" ", "", e)
    e = re.sub(u"(?isu)\S*技术部", "", e)
    e = re.sub(u"(?isu)\S*产品部", "", e)
    e = re.sub(u"(?isu)\S*运营部", "", e)
    e = re.sub(u"(?isu)日报\S*", "", e)
    e = re.sub("[A-Za-z0-9\!\%\[\]\,\。\.\-\(\)]", "", e)
    # 新的匹配

    last.append(e)
w.write(u"\n\n最终提交的列表："),
for last_name in last:
    w.write(last_name),
    w.write(' '),
    # print(type(lastname))
w.write('[%d]' % len(last))

w.write(u"\n\n未提交"),
nolast = []
for m in namelist:
    m = m.decode("utf-8")
    # print(type(i))
    if m in last:
        pass
    else:
        nolast.append(m)
        w.write(m),
        w.write(' '),
len_nolast = len(nolast)-1
if len_nolast<0:
    len_nolast = 1
w.write('[%d]' % len_nolast)

w.close()
