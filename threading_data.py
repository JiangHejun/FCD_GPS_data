import sys
import time
import threading
import sys
filepath = "C:/Users/JiangHejun/Desktop/~/Python/文件读取/_FCD_1days_"
sys.path.append(filepath)
import _FCD_1days_01
import _FCD_1days_02
import _FCD_1days_03
import _FCD_1days_04
import _FCD_1days_05
import _FCD_1days_06
import _FCD_1days_07
import _FCD_1days_08
import _FCD_1days_09
import _FCD_1days_10

filedict = {}#路径字典，路径：车辆列表
fileroute = [""]*6#文件路径数组
last_time = [sys.maxsize]*6#一天结束时间数组
boundary = {}#记录边界点，x:[miny,maxy]

def printf(path,i):
	global filedict
	print(path)
	print(" v_num:%d"%len(filedict[path]))
	print(" finatime:%d"%last_time[i])
	print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(last_time[i]))+"\n")

def print_boundary():
	out = open("boundary.txt","w")
	for x in boundary:
		lin = x+" "+" ".join(boundary[x])+"\n"
		out.write(lin)
	out.close()

#程序调用
filename = "_FCD_1days_"
#各项数据只是在增加，没有删除改变，所以并不用加lock来acquire&release
thread1 = _FCD_1days_01.reader(filedict,fileroute,last_time,boundary,filepath+"/"+filename+"01")
thread2 = _FCD_1days_02.reader(filedict,fileroute,last_time,boundary,filepath+"/"+filename+"02")
thread3 = _FCD_1days_03.reader(filedict,fileroute,last_time,boundary,filepath+"/"+filename+"03")
thread4 = _FCD_1days_04.reader(filedict,fileroute,last_time,boundary,filepath+"/"+filename+"04")
thread5 = _FCD_1days_05.reader(filedict,fileroute,last_time,boundary,filepath+"/"+filename+"05")
thread6 = _FCD_1days_06.reader(filedict,fileroute,last_time,boundary,filepath+"/"+filename+"06")
thread7 = _FCD_1days_07.reader(filedict,fileroute,last_time,boundary,filepath+"/"+filename+"07")
thread8 = _FCD_1days_08.reader(filedict,fileroute,last_time,boundary,filepath+"/"+filename+"08")
thread9 = _FCD_1days_09.reader(filedict,fileroute,last_time,boundary,filepath+"/"+filename+"09")
thread10 = _FCD_1days_10.reader(filedict,fileroute,last_time,boundary,filepath+"/"+filename+"10")
#加入线程列表
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)
threads.append(thread4)
threads.append(thread5)
threads.append(thread6)
threads.append(thread7)
threads.append(thread8)
threads.append(thread9)
threads.append(thread10)
#启动线程
for t in threads:
	t.start()
#阻塞主线程
for t in threads:
	t.join()

for i in range(len(fileroute)):
	printf(fileroute[i],i)

print_boundary()
