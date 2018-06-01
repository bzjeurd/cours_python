#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Calcul de PI
import random
iterations = int(input("Nombre d'itérations: "))

def calcul_pi(num):
    total = 0
    for i in range(1,num+1):
        total = total + 1/i**4
    return (total*90)**(1/4)

def calcul_pi2(num):
    cible = 0
    for i in range(1,num+1):
        x,y = random.random(), random.random()

        if x**2+y**2 <= 1:
            cible += 1

    return (cible/num*4)

print("Calcul de PI: " + str(calcul_pi(iterations)))
print("Calcul de PI2: " + str(calcul_pi2(iterations)))
