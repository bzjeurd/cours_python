#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Calcul de PI

iterations = int(input("Nombre d'itérations: "))

def calcul_pi(num):
    total = 0
    for i in range(1,num+1):
        total = total + 1/i**4
    return (total*90)**(1/4)

print(calcul_pi(iterations))
