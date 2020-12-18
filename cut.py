from __future__ import print_function
import csv

f = csv.reader(open("latest.csv","r"));
out = open("cut.csv","w");

i=0
print_list = [2,3,7,8];
for line in f :
    for i in print_list : 
        print("%s"%line[i], end='')
        out.write(line[i])
        if i==8 : 
            print("\n", end='')
            out.write("\n");
        else : 
            print(",", end='')
            out.write(",");

    

