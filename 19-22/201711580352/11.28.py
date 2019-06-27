
# coding: utf-8

# In[8]:


a = 'abcdefghijklmnopqrstuvwxyz'
for i in range(1,26):
    print(a[:i])


# In[40]:


n = int(input('请输入个数'))

for i in range(1,1+n):
    for j in range(n*2-i,0,-1):
        print('',end=' ')
    for s in range(0,i):
        print('*',end=' ')
    print()


