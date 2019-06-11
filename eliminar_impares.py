#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 12:25:36 2019

@author: Carmen
"""

lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

def fuera_impares(l):
    
   l_tmp = [] #lista temporal que contendrá los valores pares de la lista inicial
   
   for n in l:
        
        if n%2 == 0:
            
            l_tmp.append(n)
    
   return l_tmp

print(fuera_impares(lista))