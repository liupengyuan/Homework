# -*- coding: utf-8 -*-
# my Anaconda is not working, sorry for the raw .py format


word = str(input('Please enter an English word:'))

if word.endswith('ch', 'sh', 'th', 'x'):
    word = word+"es"

elif word.endswith('y'):
    word = ''.join(list(word)[:-1])+"ies"

elif word.endswith('f'):
    word=''.join(list(word)[:-1])+"ves" 

elif word.endswith('o'):
    word = word+"es"

else:
    word = word+"s"
    
print(word)
