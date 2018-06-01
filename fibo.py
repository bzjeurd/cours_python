#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Fibonacci

maxiter = int(input("Fibonacci index : "))
current, previous = 1,0

for i in range(1,maxiter):
    current, previous = current + previous, current

print(previous);
