# -*- coding:utf-8 -*-
import os
import re
import time
#if __name__ == "__main__":
def get_phone():
    rootdir = './PhoneLabeling'
    list1 = os.listdir(rootdir)  
    list1.sort()
    for i in range(0, len(list1)):
        path = os.path.join(rootdir, list1[i])
        # if os.path.isfile(path):

#        print('path:',path,i)
        if True:
            file1 = open(path,'r')
            f = file1.readlines()
     
#        with open(path,encoding = 'utf-8') as f:
#            print(path)
            one_line = ''
            for  line in f[13:]:
#                line=line.strip();
                print(line)
                if line[0]=="\"" and len(line)<13 and line!='\"sp1\"\n':
                    print('w')
                    line=line.strip();
                    line = line.replace("\"", "")
                    f = open('no_pun_test_phone_with_prosody.txt','a+')
                    one_line+=line
                    one_line+=' '
#                    print(one_line)
#                if i==2:
#                    input()
            f.write(one_line[4:-4]+'\n')
def get_phone_with_prosody():
#    for i in range(0, len())
    file1 = open('no_pun_test_phone_with_prosody.txt','r')
    file2 = open('ProsodyLabeling/000001-010000.txt','r')
    text_1 = file1.readlines()
    text_2 = file2.readlines()
    text_3 = text_2[::2]
    a = []
    er =[0,0]
    for i in range(len(text_3)):
        
        a.append(text_3[i][7:])
#    print(len(a))
    f = open('finall_with_prosody','a+')
    for i in range(len(a)):
#        if i ==600: input()
        print(i,'th')
        no_pro = text_1[i]
        cn_with_pro = a[i]
        with_pro = no_pro
        tone_point = []
        for w,v in enumerate(with_pro):
            if v in '12345':
                tone_point.append(w+1)
#        tone_point.append(w+1)
        print(tone_point)
        pro_num=0
        cn_with_pro = cn_with_pro.replace('”','') 
        cn_with_pro = cn_with_pro.replace('“','')
        cn_with_pro = cn_with_pro.replace('、','')
        cn_with_pro = cn_with_pro.replace('，','')
        cn_with_pro = cn_with_pro.replace('。','')
        cn_with_pro = cn_with_pro.replace('：','')
        cn_with_pro = cn_with_pro.replace('？','')
        cn_with_pro = cn_with_pro.replace('！','')
        cn_with_pro = cn_with_pro.replace('…','')
        cn_with_pro = cn_with_pro.replace('—','')
        cn_with_pro = cn_with_pro.replace('（','')
        cn_with_pro = cn_with_pro.replace('）','')
        cn_with_pro = cn_with_pro.replace('；','')
        print('no_pun_cn:',cn_with_pro)
        if '儿'in cn_with_pro:
            cn_with_pro,er = er_diff(cn_with_pro, no_pro,er)
            print('cn_pro',cn_with_pro)
        for j,v in enumerate(cn_with_pro):
#            if v in  "“”’‘":
#                pro_num-=1
            if v =='#':
#                pro_num+=1
                print('j',j)
                real_j = j-pro_num*2
                print('real_j',real_j)
                print('pro_num',pro_num)
                print(tone_point)
                print('tone_point:',tone_point[real_j-1])
                with_pro = str_insert(with_pro, tone_point[real_j-1]+pro_num*3, ' '+cn_with_pro[j:j+2])
                print(with_pro)
                pro_num+=1
#        print(with_pro)
#        input()
        f.write(with_pro)
    print('three_er & four_er:',er[0],er[1])

#    print(text_1)

#def er_diff(cn, phone):
def er_diff(cn, phone, er):
#    cn = '眼下#1儿子#2高烧#1不退#3，他为#1给儿#1筹#1医药费#2决定#1扒窃#4儿。'
#    phone = 'ian3 x ia4 er2 z ii5 g ao1 sh ao1 b u2 t uei4 sp1 t a1 uei4 g ei3 er2 ch ou2 i1 iao4 f ei4 j ve2 d ing4 p a2 q ie4 n ar3'
    b = [m.start() for m in re.finditer('儿', cn)]
#    three_er=0
#    four_er=0
    if len(b) ==3:er[0]+=1
    if len(b)==4:er[1]+=1
    print('b:',b)
    num, q = [] ,[]      
    if '儿'in cn:
        for i,line in enumerate(phone):
            if line=='r'and phone[i+1] in '12345':
#                q.append(i)
                print('test:',phone[i-1], phone[i-2],phone[i-3],'end')
                if (phone[i-1]=='e'and phone[i-2] not in '12345 \t\n') or (phone[i-1]=='e'and phone[i-2] in ' 'and phone[i-3]not in '12345') or phone[i-1]!='e':
                    print('test2:',phone[i-1], phone[i-2],'end')
                    q.append(i)
                    num.append(q.index(i))
    print('er_config:',q,num ,b)
    if len(b)!=len(q):
        print('error')
    tmp=0
    for w in num:
        print(w,b,b[0])
#        if len(b)>1:
#            input()
        cn_index = b[w]
        print(w,cn_index,cn)
#        cn = cn.replace(cn[cn_index],'')
        print('concat',cn[:cn_index-tmp],cn[cn_index-tmp+1:])
        cn = cn[:cn_index-tmp] + cn[cn_index+1-tmp:]
        tmp+=1
#    if len(b)==2:
#        print('point',cn)
#        time.sleep(20)
#        input()
    return cn, er                
#    print(b,q,num,cn)
                
#        if 'er1' or 'er2' or 'er3' or 'er4' or 'er5' not in phone:
#            cn_with_pro = cn_with_pro.replace('儿','')
#    return cn_with_pro
#        elif:
#            if len(b)==2:

        
#   cn_with_pro = cn_with_pro.replace('儿','')

def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False

def str_insert(str_i,index, insert_str):
#    str_i = "20081231"
#    print('raw:',str_i)
    list_i = list(str_i)    # str -> list
#    print(list_i)

    list_i.insert(index,insert_str)  
#    list_i.insert(7, '/')
#    print(list_i)

    str_i = ''.join(list_i)    # list -> str
#    print('done:',str_i)
    return str_i


#er_diff()
get_phone_with_prosody()
#str_insert('20081231',4,'/')
#get_phone()

                      
            
