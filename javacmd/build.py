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
basedir = os.getcwd()
mainclass = "com.yp.test.HelloWorld"


# clean
logging.error("当前工作目录:"+os.getcwd()+",清理build")
shutil.rmtree(basedir+"\\"+"build")
os.mkdir(basedir+"\\"+"build")

# compile
logging.error("开始compile")
# javac -encoding "utf8" src/com/yp/test/HelloWorld.java -sourcepath src -d build -g -cp ./lib/*.jar
# os.system("javac -encoding utf8 src/com/yp/test/HelloWorld.java -sourcepath src -d build -g -cp ./lib/*.jar")

# 把文件列表加入到sourcefiles 文件中
file=open('sourcefiles','w')
for tfile in getFiles(basedir+'/src/', '.java'):
    file.writelines (tfile+'\n')
file.close()
# 执行编译
os.system("javac -encoding utf8 -sourcepath src @sourcefiles -d build  -cp ./lib/*.jar ")

# logging.error("开始copy配置文件")
os.system("cp conf/* build/")


# 用python生成清单文件
jarfile=open('manifest.mf','w')
jarfile.writelines('Class-Path: ')
for tfile in getFiles(basedir+'/lib/', '.jar'):
	tmppath,filename = os.path.split(tfile)
	tmpfilepath = 'lib/'+filename
	logging.error(tmpfilepath)
	jarfile.writelines(tmpfilepath)
jarfile.writelines('\n\n')
jarfile.close()

# 打jar包
os.chdir(basedir+"/build")
os.system("jar cvfem "+basedir+"/"+jarFileName+"  "+mainclass+"  "+basedir+"/manifest.mf  *")
os.chdir(basedir)


# 清理
os.remove(basedir+"/manifest.mf")
os.remove(basedir+"/sourcefiles")


#test
logging.error("test")
os.chdir(basedir)
os.system('java -jar '+jarFileName)
os.system('pause')