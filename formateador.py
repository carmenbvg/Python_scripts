#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 20:09:45 2019

@author: Carmen
"""

texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

lineas = texto.split('#')

for i, linea in enumerate(lineas):
    
    lineas[i] = linea.capitalize()
    
    if i==0:
        lineas[i] = lineas[i] + '...'
    
    else:
        lineas[i] = '- ' + lineas[i] + '.'
    
    print(lineas[i])