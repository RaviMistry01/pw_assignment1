#!/usr/bin/env python
# coding: utf-8

# Q1.Explain with an example each when to use a for loop and a while loop.
# 
# -->
# 1)For loop: A for loop is a control flow statement that executes code repeatedly for a particular number of iterations. In this control flow statement, the keyword used is for. The for loop is used when the number of iterations is already known.

# In[1]:


n = [1, 2, 3]  
for i in n:  
    print(i)


# 2)While loop: A loop that executes a single statement or a group of statements for the given true condition. The keyword used to represent this loop is "while". A "while" loop is used when the number of iterations is unknown. The statement repeats itself till the boolean value becomes false.
# 

# In[2]:


i = 1  # Initialization
while i < 6:  # Condition
    print(i)
    i += 1  # Updation



# Q2. Write a python program to print the sum and product of the first 10 natural numbers using for
# and while loop.

# In[36]:


num=10
sum1=0
while(num>0):
    sum1 = sum1 + num
    num = num-1
sum1    
    
    


# In[38]:


num = 10
sum2=0
for i in range(0,11):
    sum2 = sum2+i
sum2    


# Q3. Create a python program to compute the electricity bill for a household.
# 
# The per-unit charges in rupees are as follows: For the first 100 units, the user will be charged Rs. 4.5 per
# unit, for the next 100 units, the user will be charged Rs. 6 per unit, and for the next 100 units, the user will
# be charged Rs. 10 per unit, After 300 units and above the user will be charged Rs. 20 per unit.
# You are required to take the units of electricity consumed in a month from the user as input.
# Your program must pass this test case: when the unit of electricity consumed by the user in a month is
# 310, the total electricity bill should be 2250.

# In[41]:


def electricity_bill(units):
    bill = 0
    if units <= 100:
        bill = units * 4.5
    elif units <= 200:
        bill = 100 * 4.5 + (units - 100) * 6
    elif units <= 300:
        bill = 100 * 4.5 + 100 * 6 + (units - 200) * 10
    else:
        bill = 100 * 4.5 + 100 * 6 + 100 * 10 + (units - 300) * 20
    return bill

units = int(input("Enter the number of units consumed: "))
print("The total electricity bill is: ", electricity_bill(units))


# Q4. Create a list of numbers from 1 to 100. Use for loop and while loop to calculate the cube of each
# number and if the cube of that number is divisible by 4 or 5 then append that number in a list and print
# that list.

# In[43]:


# using for loop
num_for = []
for i in range(1, 101):
    cube = i**3
    if cube % 4 == 0 or cube % 5 == 0:
        num_for.append(i)

print("Numbers using for loop:", numbers_for)

# using while loop
num_while = []
i = 1
while i <= 100:
    cube = i**3
    if cube % 4 == 0 or cube % 5 == 0:
        num_while.append(i)
    i += 1

print("Numbers using while loop:", numbers_while)


# Q5. Write a program to filter count vowels in the below-given string.
# string = "I want to become a data scientist"

# In[44]:


string = "I want to become a data scientist"
vowels = "aeiouAEIOU"
count = 0

for i in string:
    if i in vowels:
        count += 1

print("Number of vowels:", count)


# In[ ]:




