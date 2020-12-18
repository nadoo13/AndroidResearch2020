from __future__ import print_function

f = open("n_hash.txt","r");
out = open("010_time_hash.txt","w");
success=0
cnt=0;
s_count=0
f_count=0
for line in f : 
    line = line.replace("\n","").split("\t");
#    print(line[0])
    out.write(line[0]);
    indexed=open("index_list/"+line[1][:3].lower());
    success=0
    for ind_line in indexed : 
        ind_line = ind_line.replace("\n","").upper().split(",");
        if(ind_line[0] == line[1]) :
#            print(","+",".join(ind_line));
            out.write(","+",".join(ind_line)+"\n");
            success=1
            s_count=s_count+1
            break;
    if(success==0) :
#        print(","+line[1]+",,,");
        out.write(","+line[1]+",,,\n");
        f_count=f_count+1
    cnt=cnt+1;
    if(cnt%100==0) :
        print("success %d"%(cnt/100));
#    if(cnt>20) : 
#        break;
print("success : %d, fail : %d"%(s_count,f_count));



