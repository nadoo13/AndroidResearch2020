from __future__ import print_function
import csv
import numpy as np

f = open("cut.csv","r");
#index_list = np.arange(16*16*16*16).reshape(16,16,16,16);
index_list = []
hash_ord = "0123456789abcdef"

for i in range(0,16) :
    for j in range(0,16) : 
        for k in range(0,16) :
            temp_list = open("index_list/"+hash_ord[i]+hash_ord[j]+hash_ord[k],"w");
            temp_list.write("");
            temp_list.close();

i=0;
for line in f :
    i=i+1
    if(i%10000==0) : print("processing %d"%(i/10000))
    temp_open = open("index_list/"+line[:3].lower(),"a");
    temp_open.write(line);
 

