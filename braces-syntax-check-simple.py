#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'parseBracers' function below.

mystack=[]
found_braces=False

def push(c):
    if(c=='(' or c=='{' or c=='['):
        mystack.append(c)
        return True
    elif(c==')'):
        if(not mystack):#empty
            return False
        last=mystack.pop()
        if(last !='('):
            return False
        else:
            return True
    
    elif(c=='}'):
        if(not mystack):#empty
            return False
        last=mystack.pop()
        if(last !='{'):
            return False
        else:
            return True
    
    elif(c==']'):
        if(not mystack):#empty
            return False
        last=mystack.pop()
        if(last !='['):
            return False
        else:
            return True
    
    #characters other than braces
    else:
        return True
    

def parseBracers(code):
    # place your code here
    mystack.clear()
    for c in code:
        #print(c,end='')
        if(not push(c)): #if braces are incorrect
            #no
            print("INCORRECT")
            return
    
    if(not mystack): #empty stack
        print("CORRECT")
    else: #unbalanced
        print("INCORRECT")
        
    
    

if __name__ == '__main__':
    # Write your code here
    n=int(input())
    for x in range(0,n):
        code=input()
        parseBracers(code)
