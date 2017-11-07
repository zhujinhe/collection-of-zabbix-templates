#!/usr/bin/python

#def local_run_command_test(cmd,file):
#     cmd = cmd + " | tee > " + file 
#     if os.path.isfile(file) == False:
#         os.system(cmd)
 #    else:
#         (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(file)
#         ticks=int(time.time())
#         delta=ticks-mtime
#         if (delta > 60):
#             os.system(cmd)
# 
#         with open(file,"r") as f:
#             return f.read()





import sys
import subprocess
import os
import time
import json
import traceback

def local_run_command(cmd,file):
    cmd = cmd + " | tee > " + file 
    if os.path.isfile(file) == False:
        os.system(cmd)
    else:
        (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(file)
	ticks=int(time.time())
	delta=ticks-mtime
	if (delta > 60):
	    os.system(cmd)

	with open(file,"r") as f:
            return f.read()

cmd="docker inspect " + sys.argv[1]
strings = local_run_command(cmd,"/tmp/zabbix-docker-inspect-"+sys.argv[1]+".out")
try:
    parsed_json = json.loads(strings)
except:
    f=open("/tmp/zabbix-debug",'a')  
    f.write(time.ctime()) 
    traceback.print_exc(file=f)
    f.write("input params arg : %s " %  sys.argv[1])  
    f.write(sys.argv[1])  
    #f.write("input params s : "+strings)  
    #f.write("input params s : "+strings)  
    #f.write("input params s : %s " strings)  
    #f.write("input params f : %s" file)  
    #f.write("input params cmd : %s" cmd)
    f.flush()  
    f.close()

key_path = sys.argv[2].split('.')
ptr = parsed_json[0]

for i in range(0,len(key_path)):
    ptr=ptr[key_path[i]]

print ptr
