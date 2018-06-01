#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Fonction diverses

def f(x):
    return 3 * x + 2

def g(x):
    return x**2

def h(x,y):
    return x + 2 * y

def i(x):
    return str(x)

def j(x):
    return f(g(x))

def k(x,y):
    return i(h(x,y))

def strictement_positif(a):
    return a > 0

def maximum(a,b):
    if a > b
        return a
    else
        return b

def minimum(a,b):
    if maximum(a,b) == a
        return b
    else
        return a

def negatif(a):
    return strictement_positif(a)!=True

def pair(a):
    return a % 2 == 0

def oppose(a):
    return a*-1

def absolue(a):
    if negatif(a)
        return oppose(a)
    else
        return a

def ff(x):
    return x if x >= 2 else 2
