# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 15:23:00 2019

@author: Lachtyy
"""

import random

def prevod():
    try:
        JmenoVS = input ('\nZadej jméno vstup souboru: ')
        SouborVS = open (JmenoVS, 'r')
        JmenoVYS = input ('Zadej jméno výstup souboru: ')
        SouborVY = open (JmenoVYS, 'w')
        while True:
            radek = SouborVS.readline()
            if radek == '':
                break
            else:
                SouborVY.write(radek.lower())
        print ('\nHotovo')
        SouborVS.close()
        SouborVY.close()
    except IOError:
        print ('\nChyba zkus to znova')

def nahrazení():
    try:
        JmenoVS = input ('\nZadej jméno vstupního souboru: ')
        SouborVS = open (JmenoVS, 'r')
        JmenoVYS = input ('Zadej jméno výstupního souboru: ')
        SouborVY = open (JmenoVYS, 'w')
        Stary = input ('Který znak se má nahradit: ')
        Novy = input ('Jakým znakem se má nahradit: ')
        while True:
            radek = SouborVS.readline()
            if radek == '':
                break
            else:
                SouborVY.write(radek.replace(Stary, Novy))
        print ('\nHotovo')
        SouborVS.close()
        SouborVY.close()
    except IOError:
        print ('\nChyba, zkus to znova')
        
def statistika():
    try:
        JmenoVS = input ('\nZadej jméno vstupního souboru: ')
        SouborVS = open (JmenoVS, 'r')
        radky = 0
        znaky = 0
        slova = 0
        cetnost = {}
        while True:
            radek = SouborVS.readline()
            if radek == '':
                break
            else:
                radky += 1
                znaky += len(radek)
                slova += len(radek.split())
                for STznak in radek:
                    znak = STznak.upper()
                    if znak in (' ', '\t', '\n'):
                        continue
                    if znak in cetnost:
                        cetnost[znak] += 1
                    else:
                        cetnost[znak] = 1
        
        for znak in sorted(cetnost):
            print (znak, '=', cetnost[znak])
        print ('Počet řádků:', radky)
        print ('Počet slov:', slova)
        print ('Počet znaků:', znaky)
        SouborVS.close()
        print ('\nHotovo')
    except IOError:
        print ('\nChyba, zkus to znova')
        
def nahodnytext():
    try:
        JmenoVYS = input ('\nZadej jméno výstupního souboru: ')
        SouborVY = open (JmenoVYS, 'w')
        samohlasky = 'aeiyou'
        souhlasky = 'qwrtzpsdfghjklxcvbnm'
        for i in range (50):
            delka = random.randint (2,8)
            zacatek = random.randint (0, 1)#začínám samohláskou nebo souhláskou
            for i in range (delka):
                if zacatek:
                    SouborVY.write(random.choice(souhlasky))
                else:
                    SouborVY.write(random.choice(samohlasky))
                zacatek = not(zacatek)
            SouborVY.write(' ')
        SouborVY.close()
        print ('\nHotovo')
    except IOError:
        print ('\nChyba, zkus to znova')
        
while True:
    print ('\nMenu')
    print ('1) Převod na malá písmena')
    print ('2) Nahrazení znaků')
    print ('3) Statistika souboru')
    print ('4) Generování náhodného textu')
    try:
        volba = int(input('Tvoje volba? '))
        if volba == 1:
            prevod()
        elif volba == 2:
            nahrazení()
        elif volba == 3:
            statistika ()
        elif volba == 4:
            nahodnytext()
        else:
            print ('Vyber číslo 1 - 5: ')
    except ValueError:
        print ('Vyber číslo 1 - 5: ')
    except EOFError:
        exit (0)        
