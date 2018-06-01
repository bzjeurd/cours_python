#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Fonctions diverses listes et string

def est_numerique(val):
    if val.isnumeric():
        return True
    else:
        if "-" == val[0]:
            return val[1:].isnumeric()
        else:
            return False

def double(value):
    newval = []
    for x in value:
        if est_numerique(x):
            newval.append(int(x)*2)

    return newval

def verifier(value):
    return len(value) == len(double(value))

def serpent():
    serp = ["o"]
    print ("".join(serp))
    while len(serp) > 0:
        croissance = input("Taille du serpent (+ ou -): ")
        if croissance == "+":
            serp.insert(0,"~")
        elif croissance == "-":
            if serp[0] == "~":
                serp.remove("~")
        else:
            print("Veuillez utiliser les caratères (+ ou -)")
        if len(serp) > 0:
            print ("".join(serp))

def serpent2():
    index = 0;
    while index >= 0:
        print(index * "~" + "o")
        croissance = input("Taille du serpent (+ ou -): ")
        index += croissance == "+"
        index -= croissance == "-"

def longueur(liste):
    long = 0
    for i in liste:
        long += 1
    return long

def moyenne(liste):
    total = 0
    for i in liste:
        total += i
    return total/longueur(liste) if longueur(list) > 0 else 0

def plus_grand_ou_egal(liste, seuil):
    res = []
    for i in liste:
        if i >= seuil:
            res.append(i)
    return res

def plus_petit_ou_egal(liste, seuil):
    res = []
    for i in liste:
        if i >= seuil:
            res.append(i)
    return res

def positive(liste):
    return plus_grand_ou_egal(liste, 0)

def negative(liste):
    return plus_petit_ou_egal(liste, 0)

def dans(liste, valeur):
    for i in liste:
        if i == valeur:
            return True
    return False

def minimum(liste):
    mini = liste[0]
    for i in liste:
        if i < mini:
            mini = i
    return mini

def minimum(liste):
    maxi = liste[0]
    for i in liste:
        if i > maxi:
            maxi = i
    return maxi

def repeter(chaine, multi):
    res = ""
    for i in range(0,multi):
        res += chaine
    return res

def binaire(chaine):
    res = 0
    for index, valeur in enumerate(reversed(chaine)):
        res += int(valeur) * 2**index
    return res

def and_lst(liste):
    for i in liste:
        if not i:
            return False
    return True

def or_lst(liste):
    for i in liste:
        if i:
            return True
    return False

def table_mult(valeur):
    for i in range(2,valeur+1):
        for j in range(2, valeur+1):
            print(i,"*",j,"=",i*j)

def zip(liste1, liste2):
    if longueur(liste1) != longueur(liste2):
        return []
    tuplex = []
    i = 0
    while i < longueur(liste1):
        tuplex.append((liste1[i],liste2[i]))
        i += 1
    return tuplex

def zip2(liste1, liste2):
    if longueur(liste1) != longueur(liste2):
        return []
    tuplex = []
    for index, valeur in enumerate(liste1):
        tuplex.append((valeur,liste2[index]))
    return tuplex

def enum(liste):
    return zip(range(longueur(liste)), liste)

def unzip(tuples):
    liste1, liste2 = [], []
    for i1,i2 in tuples:
        liste1.append(i1)
        liste2.append(i2)
    return liste1, liste2

def fonct(valeur):
    return 2*valeur+2

# ([A], A -> B) -> [B]
def transform(liste, fonction):
    res = []
    for i in liste:
        res.append(fonction(i))
    return res

def majeur(age):
    return age >= 18

# ([A], A -> Bool) -> [A]
def filter(liste, predicate):
    res = []
    for i in liste:
        if predicate(i):
            res.append(i)
    return res

def remove_duplicates(liste):
    return list(set(liste))


# [A] -> A
def reduce(liste, fonction, elem_neutre):
    res = elem_neutre
    for i in liste:
        res = fonction(res,  i)
    return res

assert( reduce( [1, 2, 3], lambda a,b: a+b, 0) == 6 )
assert( reduce( [1, 2, 3], lambda a,b: a*b, 0) == 0 )
assert( reduce( [1, 2, 3, 3], lambda a,b: a*b , 1) == 18 )
