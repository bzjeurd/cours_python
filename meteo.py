#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from pprint import pprint

ville = input("Ville cible: ")

r = requests.get('https://www.prevision-meteo.ch/services/json/'+ville)

if r.status_code == 200:

    if r.text.count("error") > 0:
        print(r.json()["errors"][0]["text"])

    else:
        infometeo = r.json()
        print("Altitude de " + infometeo["city_info"]["name"] + " : " + infometeo["city_info"]["elevation"] + 'm')
