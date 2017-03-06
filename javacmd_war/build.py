#!/usr/bin/python
#coding:UTF-8

import paramiko,datetime,os,logging
import os,shutil
import sys
import time

# 遍历文件侠
def getFiles(dir, suffix):
    res = []
    for root, directory, files in os.walk(dir):
        for filename in files:
            name, suf = os.path.splitext(filename)
            if suf == suffix:
                res.append(os.path.join(root, filename))
    return res


# 一些变量
jarFileName = "myh.jar"
webFold = "WebContent"

basedir = os.getcwd()

# clean,init some path
logging.error("current workplace:"+os.getcwd()+",clean build")

if os.path.exists(basedir+"\\"+"build"):
    shutil.rmtree(basedir+"\\"+"build")
os.mkdir(basedir+"\\"+"build")
os.mkdir(basedir+"\\"+"build\\classes")


# compile
logging.error("begin compile")

# 把文件列表加入到sourcefiles 文件中
file=open('sourcefiles','w')
for tfile in getFiles(basedir+'/src/', '.java'):
    file.writelines (tfile+'\n')
file.close()
# 执行编译
os.chdir(basedir)
result = os.system("javac -encoding utf8 -sourcepath src @sourcefiles -d build/classes  -Djava.ext.dirs=./lib ")
# result = os.system("javac -encoding utf8 -sourcepath src @sourcefiles -d build/classes  -cp ./lib/log4j.jar;./lib/jsp.jar;./lib/servlet-api.jar; ")

# 判断编译结果
if result!=0:
	logging.error('javac error')	
	os.system("pause")
	sys.exit()


# logging.error("开始copy配置文件")
os.system("cp conf/* build/classes")



# copy lib和classes
os.system('cp -r lib '+basedir+'/'+webFold+'/WEB-INF/')
os.system("cp -r "+basedir+"/build/classes  "+basedir+"/"+webFold+"/WEB-INF/")

# war
os.system("jar -cvf myh.war -C "+webFold+"/ .")

# clean
os.remove(basedir+"/sourcefiles")
os.system("pause")

