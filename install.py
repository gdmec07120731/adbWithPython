import os
import subprocess

def install():
    files = os.listdir("apks")
    for apk in files:
        if apk.endswith('.zip'):
            pushZip(apk)
        elif apk.endswith('.apk'):
            installApk(apk)

#推送zip包到根目录
def pushZip(apk):
    order ='adb push apks/' + apk + ' /storage/emulated/0'
    print(order)
    pi=subprocess.Popen(order,shell=True,stdout=subprocess.PIPE)
    pi.stdout.read()
    print('finish success') 

#安装apk
def installApk(apk):
    order ='adb install -r apks/' + apk
    print(order)
    pi=subprocess.Popen(order,shell=True,stdout=subprocess.PIPE)
    print('finish', (pi.stdout.read()))

#开始安装    
install()
