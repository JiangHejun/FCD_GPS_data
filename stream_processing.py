import os
import time
import sys

filedict = {}#路径字典，路径：车辆列表
fileroute = [""]*6#文件路径数组
boundary = {}#记录边界点，x:[miny,maxy]

def read_txt(data_floder,filename):
	global filedict
	global fileroute
	global boundary
	days = [1236528000,1236614400,1236700800,1236787200,1236873600,1236960000]
	path = os.path.abspath(os.curdir)+"\\"+data_floder+"/"+filename+".txt"
	cars = {}#day:car:["date time x y\n","date time x y\n"]
	f = open(path)
	data = f.readlines()
	for line in data:
		lis = line.split()
		if len(lis) < 6:#如果一行数据不全，丢弃
			print("false!!!")
			continue
		for day in days:#循环天数,寻找属于哪一天
			if int(lis[0])<day:#判断时间2009-03-09 00:00:00
				#创建文件夹,创建一次
				if fileroute[days.index(day)] is "":#文件路径数组还没有被记录
						path = os.path.abspath(os.curdir)#获取当前目录,前面自带r
						path_name = str(days.index(day)+1)+"st_day_data_moni"#建立文件夹名字
						path = path + "\\" + path_name#计算建立文件夹路径
						os.mkdir(path)#Create folder
						fileroute[days.index(day)] = path#更新文件路径数组
						filedict[path] = []#建立对应路径的空字典列表

				x1 = "%.5f"%float(lis[2])
				y1 = "%.6f"%float(lis[3])
				#记录边界
				if str(x1) in boundary:
					if float(y1) > float(boundary[str(x1)][1]):#>maxy
						boundary[str(x1)][1] = str(y1)
					if float(y1) < float(boundary[str(x1)][0]):#<miny
						boundary[str(x1)][0] = str(y1)
				else:
					boundary[str(x1)] = [str(y1),str(y1)]#miny,maxy,数值列表

				#deal with cars
				date = time.strftime("%Y-%m-%d-%H:%M:%S",time.localtime(int(lis[0])))
				if lis[1] not in filedict[fileroute[days.index(day)]]:#如果没有记录过该车辆
					filedict[fileroute[days.index(day)]] += [lis[1]] #列表化车辆编号存入列表
				car_line = date+" "+lis[0]+" "+str(x1)+" "+str(y1)+"\n"
				if days.index(day) in cars:#if remenbered the day				
					if lis[1] in cars[days.index(day)]:#if the day's car remenbered
						cars[days.index(day)][lis[1]].append(car_line)#add a car's data
					else:
						cars[days.index(day)][lis[1]] = [car_line]#creat a car
				else:
					cars[days.index(day)] = {lis[1]:[car_line]}#creat the day's car
				break#this is very important
	f.close()#close file
	#write cars
	for day_num in cars:#ergodic cars[day] 
		path_now = fileroute[day_num]
		i = 0
		for v_num in cars[day_num]:
			f = open(path_now+"/"+str(i)+".txt","a")#append mode
			f.writelines(cars[day_num][v_num])
			f.close()
			i+=1
#main program
data_floder = "_FCD_1days_"
start = time.clock()
for i in range(1,11):
	starttime = time.clock()
	filename = data_floder+str("%02d"%i)
	read_txt(data_floder,filename)
	endtime = time.clock()
	print("%s.txt spend time:%f"%(filename,endtime-starttime))
end = time.clock()
print("spend total time:%d"%end-start)

#print message 
for p in filedict:#print vechile number
	path_v_num = filedict+"/"+str(fileroute.index(p)+1)+"_vehicle_number.txt"
	for i in range(len(filedict[p])):
		filedict[p][i] += "\n"
	f = open(path_v_num,"w")
	f.writelines(filedict[p])
	f.close()
	print("%s saved!"%path_v_num)
boun = []
for x in boundary:#print boundary
	boun.append(x+" "+" ".join(boundary[x])+"\n")
f = open("boundary.txt","w")
f.writelines(boun)
f.close()
print("boundary.txt saved!")