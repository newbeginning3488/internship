#!/usr/bin/env python
# coding: utf-8

# python program to find factorial of number

# In[1]:


def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("Input a number to compute factorial :")) 
print(factorial(n))

        


# python program to find whether a number is prime or composite

# In[2]:


# taking input from user
number = int(input("Enter any number: "))

#prime number is always greater than 1
if number > 1:
    for i in range(2, number):
        if (number % i) == 0: 
            print(number, "is not a prime number")
            break
    else:
        print(number,"is a prime number")

# if the entered number is lessthan or equal to 1
# then it is not prime number
else:
    print(number,"is not a prime number")
    


# python program to check whether given string is palindrome or not

# In[3]:


string=input(("Enter a string: "))
if (string == string [::-1]):
    print("The string is a palindrome")
else:
    print("Not a palindrome")


# python program to get the third side of right angled triangle from two given sides

# In[4]:


import math


# In[5]:


a = float(input("Enter base: "))
b = float(input("Enter height: "))
x = float(input("Enter angle: "))

c = math.sqrt(a ** 2 + b ** 2)

    
print("Hypotenuse =", c)    

    


# python program to print the frequency of each of the characters present in the string

# In[8]:


string=input("Enter the string: ")
str1=list(string)
strlist=[]

for k in str1:
    if k not in strlist:
        strlist.append(k)
        count=0
        
        for i in range(len(str1)):
            if k==str1[i]: 
              count+=1
        print("{},{}".format(k,count))        


# In[ ]:




