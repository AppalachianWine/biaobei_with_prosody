file1 = open('finall_with_prosody','r')
f = file1.readlines()
out_path=open('metadata_with_prosody.csv','a+')
for i,line in enumerate(f,1):
    num = str(i).zfill(6)
    line = line.strip()
    new_line = num+'|^ '+line+' $|^ '+line+' $'
    print(new_line,file=out_path)
#    out_path.write(new_line+'\n')
    

