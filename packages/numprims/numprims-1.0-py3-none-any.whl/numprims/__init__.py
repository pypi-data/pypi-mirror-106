# -*- coding: utf-8 -*-
"""
Created on Sat May 22 19:39:08 2021

@author: Usuario
"""

def numerosprimos(n):
    
    for i in range(2,n):
        es_primo=True;
        for j in range(2,i):
            if(i%j==0):
                es_primo= False
        if(es_primo):
            print(f"{i} es numero primo")
            
    return es_primo