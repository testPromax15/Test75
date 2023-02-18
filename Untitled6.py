#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Калькулятор
print('Добро пожаловать в мой калькулятор')
a=int(input('Введите число 1:'))
b=int(input('Введите число 2:'))
v=int(input('Какую операцию вы хотите выполнить? \n 1 Сложение \n 2 Вычитание \n 3 Деление \n 4 Умножение \n '))
if v==1:
    r=a+b
    p='сложение'
    t=p
if v==2:
    r=a-b
    q='вычитание'
    t=q
if v==3:
    r=float(a/b)
    m='деление'
    t=m
if v==4:
    r=a*b
    n='умножение'
    t=n
print('Результат',t,"=",r)    
       


# In[7]:


x=-4
if (x>0):
  X = x*10
else:
  X = x*8
print(X)


# In[12]:


x=15
if (x > 0):
   print("Положительное")
elif (X < 0):
   print("Отрицательное")
else :
   print("Равно нулю")


# In[16]:


print(True and True)
print(True or True)
print(not False)


# In[ ]:




