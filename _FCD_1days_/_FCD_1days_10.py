#时间戳 车辆编号 经度 纬度 车速 角度
#武汉地区 2009/3/8 0：0：1 开始
#一天的数据量：fileline：14263886，v_num：11218
#xrange 一次只创建一个数
import os
import time
import sys

def reader(filedict,fileroute,last_time,boundary,filename):
	f = open(filename+".txt")
	days = [1236528000,1236614400,1236700800,1236787200,1236873600,1236960000]
	for line in f:
		lis = line.split()#当前行列表
		#如果一行数据不全，丢弃
		if len(lis) < 6:
			print("line false!!!")
			continue
		for day in days:#循环天数,寻找属于哪一天
			if eval(lis[0])<day:#判断时间2009-03-09 00:00:00
				#创建文件夹,创建一次
				if fileroute[days.index(day)] is "":#文件路径数组还没有被记录
					path = os.path.abspath(os.curdir)#获取当前目录,前面自带r
					path_name = str(days.index(day)+1)+"st_day_data_moni"#建立文件夹名字
					path = path + "\\" + path_name#计算建立文件夹路径
					os.mkdir(path)
					fileroute[days.index(day)] = path#更新文件路径数组
					filedict[path] = []#建立对应路径的空字典列表

				#创建文件
				if lis[1] not in filedict[fileroute[days.index(day)]]:#如果没有记录过该车辆
					filedict[fileroute[days.index(day)]] += [lis[1]] #列表化车辆编号存入列表
				path_now = fileroute[days.index(day)]+"\\"+str(filedict[fileroute[days.index(day)]].index(lis[1])) +".txt"

				#记录最后时间
				last = day - int(lis[0])
				if last<last_time[days.index(day)]:
					last_time[days.index(day)] = int(lis[0])

				#记录边界
				x1 = "%.5f"%float(lis[2])
				y1 = "%.6f"%float(lis[3])
				if str(x1) in boundary:
					if float(y1) > float(boundary[str(x1)][1]):#>maxy
						boundary[str(x1)][1] = str(y1)
					if float(y1) < float(boundary[str(x1)][0]):#<miny
						boundary[str(x1)][0] = str(y1)
				else:
					boundary[str(x1)] = [str(y1),str(y1)]#miny,maxy,数值列表

				writedata(lis[0],lis[2],lis[3],path_now)#写入文件信息
				break
	# os.system("pause")
	f.close()

def writedata(t,x,y,p):#传入参数：&时间&经度&纬度&文件路径
	a = "%.5f"%float(x)#不能用round，0会丢失
	b = "%.6f"%float(y)
	c = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(t)))
	f = open(p,"a")#创建文件||或者追加文件
	#输出：时间格式+时间戳+经度+纬度
	f.write(c+" "+t+" "+str(a)+" "+str(b)+"\n")
	f.close()