
# coding: utf-8

# In[2]:


#练习 1：仿照求$ \sum_{i=1}^mi + \sum_{i=1}^ni  + \sum_{i=1}^ki$的完整代码，写程序，可求m!+n!+k!
def compute_sum(end):
    i=0
    total_m=0
    while i<end:
        i+=1
        total_m+=i
    return total_m
m=int(input('请输入一个整数，以回车结束。'))
n=int(input('请输入一个整数，以回车结束。'))
k=int(input('请输入一个整数，以回车结束。'))
print('最终的和是;',compute_sum(m)+compute_sum(n)+compute_sum(k))


# In[2]:


#练习 2：写函数可返回1 - 1/3 + 1/5 - 1/7...的前n项的和。在主程序中，分别令n=1000及100000，打印4倍该函数的和。
def compute_sum(end):
    i=0
    total_n=0
    s=0
    m=0
    while i<end:
        i=i+1
        s=i%2
        m=1/(2*i-1)
        if s==0:
            m=-m
        else:
            m=m
        total_n+=m
    return total_n
n=1000
print('当n=1000时，函数前n项和的四倍为：',compute_sum(n)*4)
n=100000
print('当n=100000时，函数前n项和的四倍为：',compute_sum(n)*4)


# In[3]:


#练习 3：将task3中的练习1及练习4改写为函数，并进行调用。
k=str(input('请输入你的名字:'))
m=int(input('请输入你出生的月份:'))
n=int(input('请输入你出生的日期:'))
if (m==1 and 20<n<32)or(m==2 and 0<n<20):
    s='水瓶座'
if (m==2 and 19<n<30)or(m==3 and 0<n<21):
    s='双鱼座'
if (m==3 and 20<n<32)or(m==4 and 0<n<21):
    s='白羊座'
if (m==4 and 20<n<31)or(m==5 and 0<n<22):
    s='金牛座'
if (m==5 and 21<n<32)or(m==6 and 0<n<22):
    s='双子座'
if (m==6 and 21<n<31)or(m==7 and 0<n<23):
    s='巨蟹座'
if (m==7 and 22<n<32)or(m==8 and 0<n<24):
    s='狮子座'
if (m==8 and 23<n<32)or(m==9 and 0<n<24):
    s='处女座'
if (m==9 and 23<n<31)or(m==10 and 0<n<24):
    s='天秤座'
if (m==10 and 23<n<32)or(m==11 and 0<n<23):
    s='天蝎座'
if (m==11 and 22<n<31)or(m==12 and 0<n<22):
    s='射手座'
if (m==12 and 21<n<32)or(m==1 and 0<n<21):
    s='摩羯座'
print(k,'你是一个非常有性格的',s,sep='')


# In[28]:


#挑战性练习：写程序，可以求从整数m到整数n累加的和，间隔为k，求和部分需用函数实现，主程序中由用户输入m，n，k调用函数验证正确性。
m=int(input('请输入一个整数'))
n=int(input('请输入一个整数'))
k=int(input('请输入一个正整数'))
if m>=n or k<0 or (n-m)%k!=0:
    print('Flase')
else:
    total=(m+n)*((n-m)/k+1)/2
    print(total)

