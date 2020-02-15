# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 19:05:23 2020

@author: Anonymous
"""

'''prime nos'''
import math 
for i in range(1,20):
    if i<=3:
        print(i)
    elif i>3:
        for j in range(2,int(math.sqrt(i)//1)+1):
            if i%j==0:
                print(i,'np')
                break
        else:
               print(i,'p')