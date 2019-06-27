
# coding: utf-8

# In[14]:


import random

def idiom_list(x):
    with open('C:\temp\成语大全.txt','r') as fh:
        for i in set(fh.readlines()):
            if x == i.strip():
                return True
        return False

def idiom_test(idiom1, idiom2):
    if idiom2[0] != idiom1[-1] or len(idiom2) != 4:
        return False
    return True

def idiom_select(x):
    if x == None:
        with open('C:\temp\成语大全.txt','r') as fh:
            return random.choice(fh.readlines())[:-1]
    else:
        with open('C:\temp\成语大全.txt','r') as fh:
            base = fh.readlines()
            random.shuffle(base)
            for i in base:
                if i[:-1] == x or len(i) != 5:
                    continue
                if i[0] == x[-1]:
                    return i[:-1]
        return None

def idiom_main(start ):
    computer=0
    people=0
    start=0
    memory = set()
    if start == 0:
        while True:
            t = idiom_select(None)
            if idiom_select(t) != None and len(t) == 4:
                break
        print(t)
    else:
        p = input("请输入成语:")
        if p.strip() == '':
            print("游戏结束！你输了")
            return 0
        if idiom_list(p) == False:
            print("游戏结束！该成语不存在")
            return 0
        memory.add(p)
        cycle = 0
        while True:
            t = idiom_select(p)
            cycle += 1
            if t not in memory:
                break
            if cycle == 10:
                t = None
                break
        if t == None:
            print("恭喜你，你赢了！")
            return 1
        else:
            print(t)
            memory.add(t)        
    while True:
        p = input("请输入成语:")
        if p.strip() == '':
            print("游戏结束！你输了")
        if idiom_list(p) == False:
            print("游戏结束！该成语不存在")
            return 0
        if p in memory:
            print("游戏结束！该成语已被使用过")
            return 0
        if idiom_test(t, p) == False:
            print("游戏结束！你未遵守游戏规则")
            return 0
        memory.add(p)
        cycle = 0
        while True:
            t = idiom_select(p)
            cycle += 1
            if t not in memory:
                break
            if cycle == 10:
                t = None
                break
        if t == None:
            print("恭喜你，你赢了！")
            return 1
        else:
            print(t)
            memory.add(t)

idiom_main()

