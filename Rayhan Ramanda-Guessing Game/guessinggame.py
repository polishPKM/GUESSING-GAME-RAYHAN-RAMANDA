# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
t = 0
g = int(input("total of guesses"))
low = int(input("enter the lower range: "))
high = int(input("enter the higher range: "))
x = random.randint(low, high)
n = int(input("Enter an integer between the given range: "))
 
while (x != 'n'):
    if(t<(g-1)):
        if n < x:
            print("The number guessed is low")
            t = t+1
            n = int(input("Enter an integer between the given range: "))
        elif (n > x):
            print("The number guessed is high")
            t = t+1
            n = int(input("Enter an integer between the given range: "))
        else:
            print("The number guessed is right")
            print("Total guesses taken: ", t+1)
            break
    else:
        print("You ran out of chances, now out")
        break