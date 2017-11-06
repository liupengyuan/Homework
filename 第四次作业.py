
# coding: utf-8

# In[1]:


#练习1

def compute_factorial(end):
    i = 1
    fac = 1
    while i < end:
        i+=1
        fac*=i
    return fac

n = int(input('请输入第一个你想计算的数字，以回车建结束'))
m = int(input('请输入第二个你想计算的数字，以回车键结束'))
k = int(input('请输入第三个你想计算的数字，以回车键结束'))

print('m!+n!+k!=',compute_factorial(n)+compute_factorial(m)+compute_factorial(k))


# In[ ]:


练习2


# In[5]:


def sum_first_n(number):
    i = 1
    total = 1
    n=1
    
    
    while n<number:
        i = 1/(i+2)
        n = n+1
        total=total+i*(-1)**(n-1)
    return total
    
    

#计算前n项和

number=100000
print((sum_first_n(number))*4)
number=2
print((sum_first_n(number))*4)


# In[ ]:


练习3


# In[3]:


def ce():
    name = input('请输入姓名，回车结束')
    month = int(input('请输入出生月份（以阿拉伯数字表示）'))
    day = int(input('请输入出生日期（以阿拉伯数字表示）'))

    if month == 1 and day >= 21 or month == 2 and day <= 19:
        ce = "水瓶座"
    elif month == 2 and day >= 20 or month == 3 and day <= 20:
        ce = "双鱼座"
    elif month == 3 and day >= 21 or month == 4 and day <= 20:
        ce = "白羊座"
    elif month == 4 and day >= 21or month == 5 and day <= 21:
        ce = "金牛座"
    elif month == 5 and day >= 22 or month == 6 and day <= 21:
        ce = "双子座"
    elif month == 6 and day >= 22 or month == 7 and day <= 23:
        ce = "巨蟹座"
    elif month == 7 and day >= 24 or month == 8 and day <= 23:
        ce = "狮子座"
    elif month == 8 and day >= 24 or month == 9 and day <= 23:
        ce = "处女座"
    elif month == 9 and day >= 24 or month == 10 and day <= 23:
        ce = "天秤座"
    elif month == 10 and day >= 24 or month == 11 and day <= 22:
        ce = "天蝎座"
    elif month == 11and day >= 23 or month == 12 and day <= 21:
        ce = "射手座"
    elif month == 12 and day >= 22 or month == 1 and day <= 20:
        ce = "摩羯座"
    else:
        print('输入非法')

    print (name + ', 你是非常有性格的' + ce + '!')

ce()


# In[ ]:


挑战


# In[12]:


def _sum(m,n,k):
    total=0
    i=0
    
    while m+k*i<=n:
        x=m+k*i
        total=total+x
        i=i+1
    return total


#主程序
m = int(input('请输入一个较小的整数：'))
n = int(input('请输入一个较大的整数：'))
k = int(input('请输入两者间距：'))
print(_sum(m,n,k))

