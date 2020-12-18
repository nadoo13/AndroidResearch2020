from __future__ import print_function
import os
import random


out = open("012_time_match_list.txt","r");
success=0
cnt=0;
s_count=0
f_count=0

    
#if(kind == 0) :os.system("ls backup/malware_2017 > tmp");
#elif(kind == 1) :os.system("ls backup/malware_2020 > tmp");
#elif(kind == 2) :os.system("ls backup/goodware_2017 > tmp");
#elif(kind == 3) :os.system("ls backup/goodware_2017 > tmp");
f = open("012_time_match_list.txt","r")
os.system("rm data/small_proto_apks/goodware/*");
os.system("rm data/small_proto_apks/malware/*");
os.system("rm data/apks/goodware/*");
os.system("rm data/apks/malware/*");

train_ratio = [100,100,100,70,50,30,0,0,0,0,0,0]

for line in f : 
    line = line.replace("\n","").lower().split(",");
#    if(line[4]!='1') : continue;
#    print(line)
    if(line[4] == '0') : filedir = "backup/malware_2017/"
    elif(line[4] == '1') : filedir = "backup/malware_2020/"
    elif(line[4] == '2') : filedir = "backup/goodware_2017/"
    elif(line[4] == '3') : filedir = "backup/goodware_2020/"
    
    filedir = filedir + line[0].lower()+".data"
    if((line[1] == '') or (line[1][:4] <= "2009")) : 
#        print ("dex time is null")
        continue;
#    print(line[1][:10])
#    print(int(line[1][:4]))
    if(random.randrange(0,100) < train_ratio[int(line[1][:4])-2010]) :
        if(line[4] <='1') : destdir = "data/small_proto_apks/malware/"
        else : destdir = "data/small_proto_apks/goodware/"
    else : 
        if(line[4] <='1') : destdir = "data/apks/malware/"
        else : destdir = "data/apks/goodware/"

    os.system("cp "+filedir+" "+destdir);

#    print("cp "+filedir+" "+destdir);

print("[*] data load completed");
print("starting learning & classification");
os.system("python src/Main.py --holdout 1 --ncpucores 4");

