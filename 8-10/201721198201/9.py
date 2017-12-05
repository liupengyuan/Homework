
# coding: utf-8

# In[1]:


#2、随机生成1万个整数，范围在0-10万之间，求其中每个整数出现的次数。并按照整数大小排序输出整数及出现次数。
import random
x=[random.randint(0,100000) for i in range(10000)]
d=set(x)
a=sorted(d)
for v in a:
    print(v,':',x.count(v))


# In[2]:


#对本任务中的语料.txt文件，随机抽取其5001-10000行存为test1.txt文件，写函数，可得到其与本任务中test.txt文件的共用字以及独用字
#coding: utf-8
import random

with open(r'F:\BaiduNetdiskDownload\temp\test.txt','w') as fw, open(r'F:\BaiduNetdiskDownload\temp\语料.txt',) as fr:
    line_number=0
    for line in fr:
        if line_number < 5000:
            fw.write(line)
            line_number +=1
        else:
            break
with open(r'F:\BaiduNetdiskDownload\temp\test1.txt','w') as fw1, open(r'F:\BaiduNetdiskDownload\temp\语料.txt',) as fr:
    line_number=0
    linesNumber = 1000
    temp=0
    for line in fr:
        line_number +=1
        if line_number > 5000 and line_number < 10000:
           if temp == linesNumber:
               break
           if random.choice([True,False]):
               fw1.write(line)
               temp+=1
    
   # lines=fr.readlines()
   # for fr in range(10):
       # fw1.write(lines[random.randint(5, 10)])

def get_word_table(filename):   
    word_table = []
    with open(filename) as f:
        text = f.read()
    words = [word.split('/')[0] for word in text.split()]
    for word in words:
        if word not in word_table:
            word_table.append(word)
    return word_table

def publicword_privateword(filename1,filename2): 
    word_list1 = get_word_table(filename1)
    word_list2 = get_word_table(filename2)
    publicword = []
    privateword = []
    
    for item1 in word_list1:
        flag = 0
        for item2 in word_list2:
            if item1 == item2:
                publicword.append(item1)
                flag = flag + 1
                break 
        if flag == 0:
            privateword.append(item1)
            
    print('共用字：',publicword)
    print('--------------------------------------------------------------------------------------------------------')
    print('独用字：',privateword)
        
filename1 = r'F:\BaiduNetdiskDownload\temp\test1.txt'
filename2 = r'F:\BaiduNetdiskDownload\temp\成语.txt'
publicword_privateword(filename1,filename2)

