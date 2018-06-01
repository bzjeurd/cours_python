#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Calcul d'un intérêt composé annuel
cap = int(input("Capital de départ: "))
taux = int(input("Taux d'intérêt: "))/100
annee = int(input("Nombre d'années: "))

cap_final = cap * (1 + taux)**annee

print("Capital final: " + cap_final)
