#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 17:43:54 2019

@author: Carmenbvg
"""

import math

class Punto():
    #Se define el Método constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        print ("Se ha creado el punto ({},{})".format(x,y))
        
    #Se redefine el método string para que el punto se imprima en formato (X,Y)    
    def __str__(self):
        return "({},{})".format(self.x, self.y)
    
    #Se define el método cuadrante, para indicar el cuadrante del plano cartesiano en el que está el punto
    def cuadrante(self):
        if (self.x >0) and (self.y>0):
            print ("El punto ({},{}) está contenido en el 1º cuadrante".format(self.x, self.y))
        if (self.x <0) and (self.y>0):
            print ("El punto ({},{}) está contenido en el 2º cuadrante".format(self.x, self.y))
        if (self.x <0) and (self.y<0):
            print ("El punto ({},{}) está contenido en el 3º cuadrante".format(self.x, self.y))
        if (self.x >0) and (self.y<0):
            print ("El punto ({},{}) está contenido en el 4º cuadrante".format(self.x, self.y))
            
    #Se define el método vector, para generar vectores entre el punto y otro punto dado
    def vector(self,p):
        print("El vector generado entre {} y {} es V = ({},{})".format(self,p,p.x-self.x,p.y-self.y))
        
    #Se define el método distancia entre el punto y otro dado
    def distancia(self,p):
        X = p.x - self.x
        Y = p.y - self.y
        d = math.sqrt(X**2 + Y**2)
        print("la distancia entre {} y {} es d = {}".format(self, p, d))

class Rectangulo():
    #Método constructor
    def __init__(self, p = Punto(), q = Punto()):
        self.p = p
        self.q = q
        print ("Se ha creado el rectángulo de vértices {} y {}".format(p, q))
        if p==0 and q==0:
            print("Se ha creado un rectángulo con ambos vértices en el origen")

    #Se define el método "base" para mostrar la base del rectángulo
    def base(self):
        self.base = abs(self.p.x - self.q.x)
        print("La base del rectágulo es igual a {}".format(self.base))
    
    #Se define el método "altura" para mostrar la altura del rectángulo
    def altura(self):
        self.altura = abs(self.p.y - self.q.y)
        print("La altura del rectángulo es igual a {}".format(self.altura))
    
    #Se define el método "área" del rectángulo para mostrar el área del rectángulo
    def area(self):
        self.area = abs((self.p.x - self.q.x)*(self.p.y - self.q.y))
        print("El área del rectángulo es igual a {}".format(self.area))



A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3,-1)
D = Punto(0,0)

print(A)
A.cuadrante()
A.vector(B)
A.distancia(C)

r = Rectangulo(A,B)
s = Rectangulo()
              
r.base()
r.altura()
r.area()