
# coding: utf-8

# In[4]:


#练习 1：写函数，求n个随机整数均值的平方根，整数范围在m与k之间（n,m,k由用户输入）。
import random
m=int(input('请输入一个整数，以回车结束'))
k=int(input('请输入一个大于m整数，以回车结束'))
n=int(input('请输入你想输入的数字个数，以回车结束'))
i=0
while i<n:
    if (k<m)or(n<1)or(k==m):
        print('Flase')
        break
    else:
        number=random.randint(m,k)
    s=number**(1/2)
    i+=1
    print(s)
    


# In[4]:


#练习 2：写函数，共n个随机整数，整数范围在m与k之间，（n,m,k由用户输入）。求1：西格玛log(随机整数)，2：西格玛1/log(随机整数)
import random,math
m=int(input('请输入一个整数m，以回车结束'))
k=int(input('请输入一个大于m的整数，以回车结束'))
n=int(input('请输入一个随机正整数，以回车结束'))
i=0
total_1=0
total_2=0
while i<n:
    number=random.randint(m,k)
    i+=1
    total_1=total_1+math.log(number)
    total_2=total_2+1/math.log(number)
print(total_1,total_2)

