#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random


# In[ ]:


correct_number = str(random.randint(1,100))
guess_number = input("Please Enter any number between 1 to 100: ")

for i in range(1,10):
    if guess_number == correct_number:
        print("Congratulation!!! You Won")
        break
    elif guess_number < correct_number:
        print("The number is Too Low")
        guess_number = input()
    elif guess_number > correct_number:
        print("The number is Too High")
        guess_number = input()
    if i == 10:
        print("Your all 10 Attemps are exhausted")
        break
print("Please Try AGAIN")
guess_number = input()

        


# In[ ]:




