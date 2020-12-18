from __future__ import print_function
import os


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


count_dex_mal = [0,0,0,0,0,0,0,0,0,0,0,0]
count_dex_good = [0,0,0,0,0,0,0,0,0,0,0,0]

for line in f : 
    line = line.replace("\n","").lower().split(",");
#    if(line[4]!='1') : continue;
    print(line)
    if(line[4] == '0') : filedir = "backup/malware_2017/"
    elif(line[4] == '1') : filedir = "backup/malware_2020/"
    elif(line[4] == '2') : filedir = "backup/goodware_2017/"
    elif(line[4] == '3') : filedir = "backup/goodware_2020/"
    
    if((line[4]>='2') or(line[1] == '') or (line[1][:4] <= "2010")) : 
        print ("dex time is null")
    else : 
        for year in range(2010,2022) : 
            if(line[1][:10] <str(year) + "-01-01") : 
                print("dex time before %d"%year)
                count_dex_mal[year-2010]=count_dex_mal[year-2010]+1
                break;


    if((line[4]<'2') or(line[1] == '') or (line[1][:4] <= "2010")) : 
        print ("dex time is null")
    else : 
        for year in range(2010,2022) : 
            if(line[1][:10] <str(year) + "-01-01") : 
                print("dex time before %d"%year)
                count_dex_good[year-2010]=count_dex_good[year-2010]+1
                break;

for year in range(2010,2022) :
    print("count of dex_mal %d : %d"%(year,count_dex_mal[year-2010]))

for year in range(2010,2022) :
    print("count of dex_good %d : %d"%(year,count_dex_good[year-2010]))











