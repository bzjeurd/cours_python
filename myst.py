#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Trouver le nombre mystérieux
import random

borne = int(input("Nombre mytérieux compris entre 1 et : "))

myst = random.randint(1,borne)
numinput = 0;
essai = 0;

while (numinput != myst):

    numinput = int(input("Entrez un nombre entre 1 et " + str(borne) + " : "))

    if (numinput > myst):
        print("Nombre trop grand")
    else:
        print ("Nombre trop petit")

    essai += 1


print("Trouvé en " + str(essai) + " essai(s)")
