
# coding: utf-8

# In[1]:


# 练习一：自己定义一个reverse(s)函数，功能返回字符串s的倒序字符串。
def reverse(s):
    x=len(s)
    a=(s[x::-1])
    return a 

s=input()
reverse(s)


# In[24]:


def right_tri():
    i=0
    while i<n:
        i+=1
        print(x*i)
        
n=int(input('行数为：'))
x=input('符号为：')
right_tri()


# In[4]:


#练习二：写函数，根据给定符号和行数，打印相应等腰三角形.
def equi_tri():
    i=0
    while i<n:
        i+=1
        print(' '*(n-i)+x*(2*i-1))
        
n=int(input('行数为：'))
x=input('符号为：')
equi_tri()


# In[27]:


#练习二：写函数，根据给定符号和行数，打印其他形式的三角形.
def other_tri():
    i=0
    while i<n/2:
        i+=1
        print(x*i)
    while i>=n/2:
        i+=1
        print(x*(n-(i-1)))
        if i==n:
            break
                
        
n=int(input('行数为：'))
x=input('符号为：')
other_tri()


# In[31]:


#练习五：写函数，根据给定符号，打印各种菱形。
def rhombus():
    i=0
    while i<n/2:
        i+=1
        print(' '*(n-i)+x*(2*i-1))
    while i>=n/2:
        i+=1
        print(' '*(n-(n-(i-1)))+x*(2*(n-(i-1))-1))
        if i==n:
            break 
                   
n=int(input('行数为：'))
x=input('符号为：')
rhombus()

