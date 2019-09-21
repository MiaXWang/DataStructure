#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 12:20:10 2019

@author: mia.wang
"""

class BubbleSort:
    def __init__(self):
        self.data=[]
    def inputData(self,nums):
        self.data=nums
    def getSize(self):
        return len(self.data)
    def sort(self):
        size=self.getSize()
        for i in range(size-1):
            for j in range(size-i-1):
                if self.data[j]>self.data[j+1]:
                    self.data[j],self.data[j+1]=self.data[j+1],self.data[j]
        return self.data
                
    