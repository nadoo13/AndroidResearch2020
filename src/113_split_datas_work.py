from __future__ import print_function
import os
import random
import copy



train_set = [[100,100,0,0,0,0,0,0,0,0,0,0],
        [100,100,100,0,0,0,0,0,0,0,0,0]
#        [100,100,100,100,0,0,0,0,0,0,0,0],
#        [100,100,100,100,100,0,0,0,0,0,0,0],
#        [100,100,100,100,100,100,0,0,0,0,0,0],
#        [100,100,90,10,0,0,0,0,0,0,0,0],
#        [100,100,90,70,30,10,0,0,0,0,0,0],
#        [100,100,90,70,50,50,30,10,0,0,0,0],
#        [100,100,90,80,60,50,50,40,20,10,0,0],
#        [100,100,80,20,0,0,0,0,0,0,0,0],
#        [100,100,80,60,40,20,0,0,0,0,0,0],
#        [100,100,70,60,50,40,30,0,0,0,0,0],
#        [100,100,50,50,50,50,50,0,0,0,0,0],
#        [100,100,100,10,10,10,0,0,0,0,0,0],
#        [100,100,100,10,10,10,10,10,10,10,10,10]

]
rand_set = [0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(0,100) : 
    rand_set[0]=100
    for j in range(1,12) :
        rand_set[j] = 90-i*j/5
        if rand_set[j] < 0 :
            rand_set[j] = 0

    print(rand_set)
    train_set.append(copy.deepcopy(rand_set))
    


'''
for i in range(0,100) : 
    sum_value = i*5;
    for j in range(0,12) :
        if j == 0 : 
            rand_set[j] = 100
        elif sum_value>=100 :
            rand_set[j] = 100
            sum_value = sum_value - 100;
        else : 
            rand_set[j] = sum_value;
            sum_value=0;
    print(rand_set)
    train_set.append(copy.deepcopy(rand_set))
'''
'''
for i in range(0,1) :
    for j in range(0,12) :
        if j == 0 :
            rand_set[j] = 100
        elif j == 1 : 
            rand_set[j] = 100-i
        else :
            rand_set[j] = random.randrange(0,rand_set[j-1] + 3);
    print(rand_set)
    train_set.append(copy.deepcopy(rand_set))

print(train_set)
'''

for train_ratio in train_set :
    f = open("../012_time_match_list.txt","r")
    os.system("rm ../data/small_proto_apks/goodware/*");
    os.system("rm ../data/small_proto_apks/malware/*");
    os.system("rm ../data/apks/goodware/*");
    os.system("rm ../data/apks/malware/*");
    for line in f : 
        line = line.replace("\n","").lower().split(",");
    #    if(line[4]!='1') : continue;
    #    print(line)
        if(line[4] == '0') : filedir = "../backup/malware_2017/"
        elif(line[4] == '1') : filedir = "../backup/malware_2020/"
        elif(line[4] == '2') : filedir = "../backup/goodware_2017/"
        elif(line[4] == '3') : filedir = "../backup/goodware_2020/"
        
        filedir = filedir + line[0].lower()+".data"
        if((line[1] == '') or (line[1][:4] <= "2009")) : 
    #        print ("dex time is null")
            continue;
    #    print(line[1][:10])
    #    print(int(line[1][:4]))
        if(random.randrange(0,100) < train_ratio[int(line[1][:4])-2010]) :
            if(line[4] <='1') : destdir = "../data/small_proto_apks/malware/"
            else : destdir = "../data/small_proto_apks/goodware/"
        else : 
            if(line[4] <='1') : destdir = "../data/apks/malware/"
            else : destdir = "../data/apks/goodware/"
    
        os.system("cp "+filedir+" "+destdir);
    
    #    print("cp "+filedir+" "+destdir);
    f.close()
    print("[*] data load completed");
    print("starting learning & classification");
    printout = open("test_result.log","a");
    printout.write("train_ratio : %s\n"%train_ratio);
    printout.close();
    os.system("python Main.py --holdout 1 --ncpucores 4");

