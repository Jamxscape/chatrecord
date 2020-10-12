# import math
# 语法错误
# 运行错误
# adb devices
# 语义错误
# r = 5;
# print(v=(4/3)*format(math.pi)*(r**3))

import subprocess
import time
import os
import shutil
class Screenshot():#截取手机屏幕并保存到电脑
    def __init__(self):
        #查看连接的手机
        connect=subprocess.Popen("adb devices",stderr=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
        stdout,stderr=connect.communicate()   #获取返回命令
        #输出执行命令结果结果
        
    
    def screen(self,cmd):#在手机上截图
        screenExecute=subprocess.Popen(str(cmd),stderr=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
        stdout, stderr = screenExecute.communicate()
        # 输出执行命令结果结果
       
    
    
    def saveComputer(self,cmd):#将截图保存到电脑
        screenExecute = subprocess.Popen(str(cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        stdout, stderr = screenExecute.communicate()
        stdout = stdout.decode("utf-8")
        stderr = stderr.decode("utf-8")
        # 输出执行命令结果结果


for i in range(0,100):
    cmd1=r"adb shell /system/bin/screencap -p /sdcard/alovejingjing/fold_name" + str(i) +".png"      #命令1：在手机上截图3.png为图片名
    cmd2=r"adb pull /sdcard/test" + str(i) + ".png /Volumes/photo/fold_name"                        #命令2：将图片保存到电脑 d:/3.png为要保存到电脑的路径
    screen=Screenshot()
    screen.screen(cmd1)
    screen.saveComputer(cmd2)
    time.sleep(1);
    print("输出第"+str(i)+"张")
    # os.system("adb shell input swipe 250 750 250 500 50")
    os.system("adb shell input swipe 250 750 250 500 50")
    time.sleep(1)
