from __future__ import print_function
import os


out = open("012_time_match_list.txt","w");
success=0
cnt=0;
s_count=0
f_count=0

for kind in range(0,4) :
    
    if(kind == 0) :os.system("ls backup/malware_2017 > tmp");
    elif(kind == 1) :os.system("ls backup/malware_2020 > tmp");
    elif(kind == 2) :os.system("ls backup/goodware_2017 > tmp");
    elif(kind == 3) :os.system("ls backup/goodware_2020 > tmp");
    f = open("tmp","r")
    for line in f : 
        line = line.replace("\n","").replace(".data","").upper().split("\t");
    #    print(line[0])
        indexed=open("index_list/"+line[0][:3].lower());
        success=0
        for ind_line in indexed : 
            ind_line = ind_line.replace("\n","").upper().split(",");
            if(ind_line[0] == line[0]) :
    #            print(","+",".join(ind_line));
                out.write(",".join(ind_line)+",%d"%kind+"\n");
                success=1
                s_count=s_count+1
                break;
        if(success==0) :
    #        print(","+line[1]+",,,");
            out.write(line[0]+",,,,%d"%kind+"\n");
            f_count=f_count+1
        cnt=cnt+1;
        if(cnt%100==0) :
            print("success %d"%(cnt/100));
    #    if(cnt>20) : 
    #        break;
print("success : %d, fail : %d"%(s_count,f_count));



