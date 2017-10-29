
# coding: utf-8

# In[1]:

#练习 1：写函数，求n个随机整数均值的平方根，整数范围在m与k之间（n,m,k由用户输入）。
m=int(input("请输入一个大于0的整数，以回车结束。"))
k=int(input("请输入一个大于0的整数，以回车结束。"))
n=int(input("请输入你想随机生成的整数个数，以回车结束。"))
import random
list=[]
for i in range(n):
    list.append(random.randint(m,k))
print(list)
def sum(list):
    s=0
    for x in list:
        s=s+x
    return s
def average(list):
    avg=0
    avg=sum(list)/(len(list)*1.0)
    return avg
import math
math.sqrt( average(list) )

print("math.sqrt: ", math.sqrt(average(list)))


# In[2]:

#练习 2：写函数，共n个随机整数，整数范围在m与k之间，（n,m,k由用户输入）。求1：西格玛log(随机整数)
m=int(input("请输入一个大于0的整数，以回车结束。"))
k=int(input("请输入一个大于0的整数，以回车结束。"))
n=int(input("请输入你想随机生成的整数个数，以回车结束。"))
import random
rand_list=[]
for i in range(n):
    rand_list.append(random.randint(m,k))
print(rand_list)
import math
log_list=[]
for i in rand_list:
    log_list.append(math.log(i))
    
print(log_list)
def sum(log_list):
    s=0
    for x in log_list:
        s=s+x
    return s


print(sum(log_list))




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



