
# coding: utf-8

# In[27]:


#写函数，返回一个list中所有数字的和
numbers=[1,12,14,46,3]
total=0
for number in numbers:
        total+=number
print(total)


# In[28]:


#写函数，返回一个list中的最小值
numbers=[1,2,4,5,68,7]
print(min(numbers))


# In[8]:


#写函数，返回某个元素/对象在一个list中的位置，如果不在，则返回-1.
words=['plunder','expertise','paunch']
n=int(input('请输入你想返回的单词次序'))
if n in range(3):
    print(words[n])
else:
    print(-1)


# In[11]:


#写函数，可求两个向量的夹角余弦值，向量可放在list中。主程序调用该函数。
import math
arc(m,n)
s=(n_1*n_2+n_3*n_4)/(math.sqrt(n_1*n_1+n_2*n_2)+math.sqrt(n_3*n_3+n_4*n_4))
print(s)


# In[ ]:


#挑战性习题：python语言老师为了激励学生学python，自费买了100个完全相同的Macbook Pro，
#分给三个班级，每个班级至少分5个，用穷举法计算共有多少种分法？
s=100
for i in range(5,86):
    for j in range(5,86):
        for k in range(5,86):
            print('{},{},{}'.format(i,j,k))

