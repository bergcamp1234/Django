#! /usr/bin/env python
#coding=utf-8

#使用该脚本前，确认mysql环境配置无问题，能使用~mysql/bin下的命令
import os
import datetime
import time
import shutil

#设定base_dir,确保该目录为需要删除的文件路径
base_dir = ('/data/test')
os.chdir(base_dir)
#获得路径下文件个数，确切的说是所有的文件名
filelist = os.listdir(base_dir)
length = len(filename)
todaytime = time.time()

i = 0 
for i in range(length):
    filetime = os.path.getctime(filename[i])
    differencetime = (todaytime - os.path.getctime(filename[i]))/3600 
    #除以3600，表示把相差的时间以小时来计数，若再除以24，则以天来表示
    filedate = datetime.datetime.fromtimestamp(filetime)
    if differencetime > 3:
        os.remove(filename[i])
    #print (filedate)
    #print (differencetime)
        print ('delete ', filename[i])
        i+=1
    else:
        print ('Nothing deleted')
#定义filetime变量并用当前时间给其赋值		
filetime2=time.strftime('%Y-%m-%d',time.localtime(time.time()))
#执行mysqldump命令备份数据库
os.system('mysqldump -uroot test>test.sql')
#把备份文件以当前时间重命名
os.rename('test.sql',filetime2+'.sql')
