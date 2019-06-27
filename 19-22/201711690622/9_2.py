
# coding: utf-8

# In[16]:


#2、随机生成1万个整数，范围在0-10万之间，求其中每个整数出现的次数。并按照整数大小排序输出整数及出现次数。
import random
list=[]
i=0
while i<10000:
    a=random.randint(1,100000)
    list.append(a)
    i+=1
    def count_words_freq(filename, words):
        word_freq_pairs = []
        for a in list:
            number = list.count(a)
            word_freq_pairs.append([a, number])
        return word_freq_pairs


# In[18]:


#3、对本任务中的语料.txt文件，抽取其5001-10000行存为test1.txt文件，
#写函数，可得到其与本任务中test.txt文件的共用字以及独用字


filename = r'd:\temp\语料.txt'
word_table = []
with open(filename) as f:
    if 5000<i<=10000:
        i+=1
        for line[i] in f:
            word_table.append(line[i])
            fh=open(r'd:\temp\test1.txt','w')
            fh.writelines(word_table)
            fh.close()
            
            def A(word):
                words1=open(r'd:\temp\test.txt','w')
                words2=open(r'd:\temp\test1.txt','w')
                B=[]
                C=[]
                for word in words1:
                    for item in words2:
                        if word==item:
                            B.append()
                        else:
                            C.append()


# In[ ]:


#4、挑战性任务：统计本任务中的语料.txt文件，得到每一个词对应不同词性的频次，可表示为：
#{词:[('n',1000), ('v', 98)...],...}，
#即在dict对象中，key为词，value为列表，输出词频最高的50个条目。
def D(filename):
    dict1={}
    whith open(filename) as f:
        for line in f:
            words = [word.split('/')[0] for word in line.split()]
            for word in words:
                if word in dict1:
                    dict1[word]+=1
                else:
                    dict1[word]=1
    return dict1

filename=r'd:\temp\语料.txt'
T=D(filename)
for i,item in enumerate(T):
    print(item,T[item])
    if i==50:
        break

