#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 12:19:15 2019

@author: mia.wang
"""

class Heap:
    def __init__(self):
        self.data_list=[None];#should not start from 0 because when right child 2*n-1 will be negative
        
    def size(self):
        return len(self.data_list)-1
    
    def left_child(self,root):
        return root*2
    def right_child(self,root):
        return root*2+1
    
    def father(self,node):
        return int(node/2)
    
    def heapify(self,root):
        if root>self.size():
            return
        left_idx=self.left_child(root)
        right_idx=self.right_child(root)
        largest=root
        if left_idx<=self.size():
            if self.data_list[left_idx]>self.data_list[largest]:
                largest=left_idx
        if right_idx<=self.size():
            if self.data_list[right_idx]>self.data_list[largest]:
                largest=right_idx
        if largest!=root:
            self.data_list[root],self.data_list[largest]=self.data_list[largest],self.data_list[root]
            self.heapify(largest)
            
    def build_heap(self):
        for i in range(int(self.size()/2),0,-1):
            self.heapify(i)
    
    def get_max(self):
        if self.size()==0:
            return None
        ret=self.data_list[1]
        self.data_list[1]=self.data_list[-1]
        del self.data_list[-1]
        self.heapify(1)
        return ret
    
    def insert(self,data):
        self.data_list.append(data)
        now_index=self.size()
        pre=self.father(now_index)
        while now_index!=1 and self.data_list[pre]<data:
            self.data_list[pre],self.data_list[now_index]=self.data_list[now_index],self.data_list[pre]
            now_index=pre
            pre=int(now_index/2)
            print(pre)