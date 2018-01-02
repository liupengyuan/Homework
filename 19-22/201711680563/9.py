
# coding: utf-8

# In[8]:


import time
import random
A=[]
B=[]
C=[]
for x in range(1,100001):
    A.append(x)
for x in range(100000):
    b=random.choice(A)
    B.append(b)
for x in range(1000):
    C.append(random.randint(1,110000))
def cA(n,la):
        for x in range(len(la)):
                if n == la[x]:
                        return True
                return False
def cB(n,lb):
        left=0
        right=len(lb)-1
        while left <= right:
                mid = (left+right)//2
                if lb[mid] == n:
                        return True
                if n < lb[mid]:
                        right=mid-1
                else:
                        left=mid+1
        return False
def r():
        for x in range(len(A)):
                cA(x,C)
        for x in range(len(B)):
                cB(x,C)
start = time.time()
r()
end = time.time()
print (end,start)

