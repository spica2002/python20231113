# DemoOS.py
from os.path import *
import glob
import os


#print(dir())

# 풀패스(전체경로)
print(abspath("demo.py"))
# 파일이름만
print(basename("c:\\work\\demo.py"))

fName = "c:\\python310\\python.exe"
if exists(fName):
    print("파일크기: {0}".format(getsize(fName)))
else:
    print("파일 없음")

result = glob.glob("c:\\work\\*.py")
print(result)
for item in result:
    print(item)

print("운영체제이름:{0}".format(os.name))
print("환경변수:{0}".format(os.environ))

#os.system("notepad.exe")

os.chdir("..")
os.chdir("c:\\python310")
result = glob.glob("*.*")
print(result)
