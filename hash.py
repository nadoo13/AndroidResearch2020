import hashlib

f_list = open("list.txt","r")

out_list = open("outlist.txt","a")

for filename in f_list : 
    filename = filename.replace("\n","");
    print filename
    file = open("data/small_proto_apks/good_apk/" + filename,"rb")
    bytes = file.read();
    hash = hashlib.md5(bytes).hexdigest();
    print(hash)
    out_list.write(filename+"\t"+hash+"\n");


