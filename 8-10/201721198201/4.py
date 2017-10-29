
# coding: utf-8

# In[5]:

#练习 1：仿照求$ \sum_{i=1}^mi + \sum_{i=1}^ni  + \sum_{i=1}^ki$的完整代码，写程序，可求m!+n!+k!
def compute_sum(end):
    i=0
    ji=1
    while i< end:
        i=i+1
        ji=ji*i
    return ji
n=int(input("请输入第1个整数，以回车结束。"))
m=int(input("请输入第2个整数，以回车结束。"))
k=int(input("请输入第3个整数，以回车结束。"))

print("最终的和是：",compute_sum(m)+compute_sum(n)+compute_sum(k))


# In[6]:

#挑战性练习：写程序，可以求从整数m到整数n累加的和，间隔为k，求和部分需用函数实现，主程序中由用户输入m，n，k调用函数验证正确性。
def compute_sum(end):
    i=n
    he=n
    while i < m:
        i=n+k
        he=he+i
    return he

n=int(input("请输入1个正整数，以回车结束。"))
m=int(input("请输入1个正整数，以回车结束。"))
k=int(input("请输入1个正整数，以回车结束。"))
print(compute_sum(n))


# In[7]:

#练习 3：将task3中的练习1及练习4改写为函数，并进行调用。
def str(str):
    if str.endswith("y"):
        str=str[:-1]
        str=(str+"ies")
    elif str.endswith("f"):
        str=str[:-1]
        str=(str+"ves")
    elif str.endswith("fe"):
        str=str[:-2]
        str=(str+"ves")
    elif str.endswith("o"):
        str=(str+"es")
    elif str.endswith("s" or "x" or "ch"or"sh"):
        str=(str+"es")
    else :
        str=(str+"s")
    return str
str1=input("请输入一个单数名词")
str(str1)
print(str(str1))


# In[9]:

#练习 3：将task3中的练习1及练习4改写为函数，并进行调用。
def str(str):
    if str.endswith("ves"):
        str=str[:-3]
        str=(str+"f")
    elif str.endswith("oes" or "ses" or "xes" or "ches" or "shes"):
        str=str[:-2]
    elif str.endswith("ies"):
        str[:-3]
        str(str+"y")
    else:
        str=str[:-1]
    return str

str1=input("请输入一个英文复数名词")
str(str1)
print(str(str1))


# In[10]:

#练习 3：将task3中的练习1及练习4改写为函数，并进行调用。
n=input("请输入你的名字！")
m=int(input("请输入你的生日（例如122）！"))     
def xz(r):
    if r > 321 and r < 419:
        k=("白羊座")
    elif r > 420 and r < 520:
        k=("金牛座")
    elif r > 521 and r < 621:
        k=("双子座")
    elif r > 622 and r < 722:
        k=("巨蟹座")
    elif r > 723 and r < 822:
        k=("狮子座")
    elif r > 823 and r < 922:
        k=("处女座")
    elif r > 923 and r < 1023:
        k=("天秤座")
    elif r > 1024 and r < 1122:
        k=("天蝎座")
    elif r > 1123 and r < 1221:
        k=("射手座")
    elif r > 1222 and r < 119:
        k=("摩羯座")
    elif r > 120 and r < 218:
        k=("水瓶座")
    else :
        k=("双鱼")
    return k

print(n,",你是非常有性格的",xz(m),"!")


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:

#练习 2：写函数可返回1 - 1/3 + 1/5 - 1/7...的前n项的和。在主程序中，分别令n=1000及100000，打印4倍该函数的和。
def my_abs(number):
    if number % 2 == 0:
         number = number*(-1)
    else:
        number = number
    return number
def compute_sum(end):
    i=0
    he=0
    number=my_abs(end)
        
    while i < end:
        i=1/(2*i-1)
        he=he+i
    return he

#主程序
i=3
print(compute_sum(i))


# In[ ]:




# In[ ]:



