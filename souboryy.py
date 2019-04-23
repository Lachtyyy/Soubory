#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 08:08:59 2019

@author: lac35158
"""
import random

def mala(vstup, vystup):
    with open(vstup, 'r') as f:
        text = f.read()
    text = text.lower()
    with open(vystup, 'w') as f:
        f.write(text)
        

def mala_znovu(vstup, vystup):
    try:
        with open(vstup, 'r', encoding='cp1250') as fr, open(vystup, 'w') as fw:
            while True:
                radek = fr.read(1)
                print(type(radek), radek)
                if radek == '':
                    break
                fw.write(radek)
    except FileNotFoundError:
        print('nenašel se ;-(')
    except OSError as err:
        print(err.strerror)
        print('Chyba zápisu')


def replace(vstup, vystup):
    try: 
        inName = raw_input(">>> zadej jmého vstupního souboru: ")
        inFile = open(inName,"r")
        outName = raw_input(">>> zadej jmého výtupního souboru: ")
        outFile = open(outName,"w")
        while True:
            radek = inFile.readline()
            if radek == '':
                break
            outFile.write(radek.decode('utf-8').upper().encode('utf-8'))
            outFile.write(radek.decode('utf-8').lower().encode('utf-8'))
        inFile.close()
        outFile.close()
        while True:
            znak = inFile.read(1)
            if znak == '':
                break
            if znak == znakStary:
                outFile.write(znakNovy)
            else:
                outFile.write(znak)
        while True:
            radek = inFile.readline()
            if radek == '':
                break
            outFile.write(radek.decode('utf-8').replace(znakStary,znakNovy).encode('utf-8'))
            
    # mala_znovu('soubor.cp1250', '/etc/fstab')

def statistika(vstup):
    cetnost = dict()
    with open(vstup, 'r') as f:
        while True:
            pismenko = f.read(1)
            if pismenko == '':
                break
            if pismenko == '\n' or pismenko == ' ':
                continue
            pismenko = pismenko.upper()
            if pismenko in cetnost:
                cetnost[pismenko] += 1
            else:
                cetnost[pismenko] = 1
    max_ = max(cetnost.values())
    for klic in sorted(cetnost):
        print(klic, cetnost[klic], '#' * int(cetnost[klic] * (70 / max_)))

def nahodnyText(pocetSlov):
           samohlasky = 'aeiyou'
           souhlasky ='qwrtpsdfghjklzxcvbnm'
    
           for i in range(pocetSlov):
           #jedno slovo
               delkaSlova = random.randint(1,8)
               zacatek = random.randint(0,1)  # zacinam samohlaskou nebo souhlaskou?
               for i in range(delkaSlova):
                   if i % 2 == zacatek:       # ztrida se samohlaska a souhlaska
                       sys.stdout.write( random.choice(souhlasky) )
                   else:
                       sys.stdout.write( random.choice(samohlasky) )
               sys.stdout.write(' ')
           sys.stdout.write('\n\n')

statistika('statisticka.data')