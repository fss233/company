#!/bin/python
#create by 20201106
import os

##ps: 2019/04/* 
indate = "2019/06/"

def getLinuxdu():
	sum = 0
	c1 = "ls /opt/supp_app/track/freight_track/" + indate
	listdir = os.popen(c1).read()
	for i in listdir.split("\n"):
		if (i != ""):
			command = "du -b /opt/supp_app/track/freight_track/" + indate + i + "/*lzo | awk '{sum += $1};END {print sum}'"
			#print(command)
			dul = os.popen(command).read()
			#print(dul)
			sum += int(dul)
	print("...")
	return sum

def getEmrdu():
#	sum = 0
#	c1 = "/opt/supp_app/hadoop-2.6.5/bin/hadoop fs -ls -d   /datasource/freight_track/" + indate + "/* |awk '{print $8}'"
#	listdir = os.popen(c1).read()
#	for i in listdir.split("\n"):
#		if (i != ""):
#			command = "/opt/supp_app/hadoop-2.6.5/bin/hadoop fs -du -s " + i + "/*lzo | awk '{sum += $1};END {print sum}'"
#			print(command)
#			dul = os.popen(command).read()
#			sum += int(dul)
#	print(sum)
	command = "/opt/supp_app/hadoop-2.6.5/bin/hadoop fs -du -s /datasource/freight_track/" + indate + "*/*lzo | awk '{sum += $1};END {print sum}'"
	#print(command)
	dul = os.popen(command).read()
	sum = int(dul)
	print("...")
	return sum
	
##TEST
dulin = getLinuxdu()
duemr = getEmrdu()
print(indate + "Linux_du:" + str(dulin))
print(indate + "EMR_du:" + str(duemr))

if (dulin == duemr):
	print("OK.")
else:
	print("Error!!!")
