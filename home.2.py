#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1.eligible to vote or not
a=int(input("enter a value"))
if(a>18):
    print("a is eligible to vote ")
else:
    print("a is not eligible to vote")
    


# In[3]:


#2.even or odd
a=int(input("enter value of a"))
if(a%2)==0:
    print("the no is even")
else:
    print("the no is odd")


# 

# In[14]:


#3.print string in reverse order
a=str(input("enter a string "))
print("reverse of the string is ")
print(a[::-1])


# In[16]:


#4.positive or negative 
n=int(input("enter a number"))
if(n>0):
    print("no is positive")
else:
    print("no is negative")


# In[24]:


#5.quadratic equation
import math
a=float(input("enter value of a "))
b=float(input("enter value of b "))
c=float(input("enter value of c "))
d=b*b-4*a*c;
if d>0:
    r1=(-b+math.sqrt(d))/(2*a)
    r2=(-b-math.sqrt(d))/(2*a)
    print("roots are real and equal",r1,"and",r2)
elif d>0:
    r1=-b/(2*a)
    print("roots are real and same",r1)
else:
    print("no real roots are there")


# In[28]:


#6.positive or negative or zero
num=int(input("enter a number"))
if num>=0:
    if num==0:
        print("zero")
    else:
        print("positive no")
else:
    print("negative no")


# In[31]:


#7.to accept a no(1-5)and print the given no in words
num=(" ","one","two","three","four""five")
n=int(input("enter a number"))
print(num[n])


# In[32]:


#8.read a char and print the given char is vowel or consonant
ch=input("enter a character")
if(ch=='A' or ch=='a' or ch=='E' or ch=='e' or ch=='I' or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print(ch,"is a vowel")
else:
    print(ch,"is a consonant ")


# In[ ]:




