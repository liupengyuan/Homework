
# coding: utf-8

# In[ ]:


1


# In[16]:


def tuxin(m,n):
    
    
    for i in range(1,n+1):
        print(' '*((n+1)-i) + i*m + m*n + i*m + ' '*((n+1)-i))
m=str(input('输入符号：  '))
n=int(input('输入行数：  '))
tuxin(m,n)


# In[ ]:


2


# In[15]:


def ackermann(m,n):
    if m==0:
        print(n+1)
    elif m>0 and n==0:
        ackermann(m-1,1)
    elif m>0 and n>0:
        ackermann(m-1,ackermann(m,n-1))
m=int(input('输入数字：  '))
n=int(input('输入行数：  '))
ackermann(m,n)


# In[ ]:


3.a


# In[32]:


import random
def exam(a,b,n):
    line=['+','-','*','/']
    total=0
    for i in range(n):
        n3 = random.randint(0,3)
        n1 = random.randint(a,b)
        n2 = random.randint(a,b)
        total=0
        if line[n3]== '+' and n1+n2>0 :
            print(n1 ,'+',n2, '=')
        if line[n3]== '-' and n1>n2:
            print(n1 ,'-', n2, '=')
        if line[n3]== '*' and n1*n2>0 :
            print(n1 ,'*', n2 ,'=')
        if line[n3]== '/' and n1%n2==0 and n1*n2>0:
            print(n1 ,'/', n2, '=')
n=int(input('输入题数n=' ))
a=int(input('输入整数a=' ))
b=int(input('输入整数b=' ))            
exam(a,b,n)
m=


# In[ ]:


3.b


# In[ ]:


4.a


# In[69]:


def write(filename):
    with open(filename,encoding = 'utf-8') as f :
        text=f.read()
        
    A= [word.split('拼音')[0] for word in text.split('\n')]
    print(A)
filename = r'D:\temp\成语大全(含成语解释)_utf8.txt'
write(filename)
        


# In[ ]:


4.b(8.md中的成语库)


# In[70]:


def count_words_freq1(filename):
    
    word_freq_pairs = []
    
    with open(filename) as f:
        text = f.read()
            
    text = text.replace('、', '')
    words = text.split('\n')

    for word in words:
        for item in word_freq_pairs:
            if word == item[0]:
                item[1] += 1
                break
        else:
            word_freq_pairs.append([word, 1])
                    
    return word_freq_pairs

#测试用

filename = r'E:\成语大全.txt'
table = count_words_freq1(filename)
print(table)
print()


# In[ ]:


4.c


# In[3]:


def count_words_freq2(filename):
    
    word_freq_pairs = []
    
    with open(filename) as f:
        text = f.read()
            
    
    words = [word.split('/')[1] for word in text.split()]
    

    for word in words:
        for item in word_freq_pairs:
            if word == item[0]:
                item[1] += 1
                break
        else:
            word_freq_pairs.append([word, 1])
                    
    return word_freq_pairs


filename = r'D:\temp\test_re_gbk.txt'
table = count_words_freq2(filename)
print(table)


# In[ ]:


4.d


# In[7]:


def nr(filename):
    word_table = []
    with open(filename) as f:
        text = f.read()
    words = [word.split(' ')[-1] for word in text.split('/nr ')]
    for word in words:
        if word not in word_table:
            word_table.append(word)
    return word_table


filename = r'D:\temp\test_re_gbk.txt'
table = nr(filename)
print(table)


# In[ ]:


4.e

