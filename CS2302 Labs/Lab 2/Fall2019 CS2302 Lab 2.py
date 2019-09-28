# Course:CS 2302 MW 1:30-2:50, Author:David Ayala
# Assignment:Lab #2B, Instructor: Diego Aguirre
# Teaching Assistant: ????, Date of last Modification: 9/27/2019
# Purpose of program:write a Python 3 program that finds the 20 most used password.

#Solution A
import time
import collections
# I put some German in this lab, since I'm currently taking it and
# I'm trying to get better at it.
# i is pronounced ee in German.
# j is pronounced yott in German.
# k is pronounced kah in German.
# a is pronounced ah in German.
# b is pronounced beh in German.
# c is pronounced tseh in German.
# password is Passwort in German.
# duplicates is Duplikate in German.
# duplicate is Duplikat in German.
# yield is Ergebnis in German.
# commonly used is häufig verwendet in German.
# number is Nummer in German.
# part is Teil in German.
# identification is Identifizierung in German.
# cleanser is Reiniger in German.
# part is teil in German.

class Node(object):
    def __init__(self):
        self.DuplikatMenge = 0
        self.Passworts = []
        self.Duplikate = []

    def Reiniger(self):
        tseh = collections.Counter(self.Duplikate)
        print('Most Commonly used passwords:')
        ee = 0
        häufigVerwendet = []
        for Identifizierung, Ergebnis in tseh.most_common(20):
            ee += 1
            häufigVerwendet.append("\"{}\" was used {} times".format(Identifizierung.rstrip(), Ergebnis))
        for ee in range(len(häufigVerwendet)):
            print(häufigVerwendet[len(häufigVerwendet) - (ee + 1)])

    # will find number of duplicates using a loop and if no duplicates then add to link list.
    def TeilAh(self, Passwort):
        for ee in range(len(Passwort)):
            if Passwort[ee] in self.Passworts:
                self.DuplikatMenge += 1
                self.Duplikate.append(Passwort[ee])
            else:
                self.Passworts.append(Passwort[ee])

with open('10-million-combos.txt', 'r', encoding='utf-8', errors='ignore') as text:
    motor = Node()
    startTime = time.time()
    print('This will take a while depending on the range that was in inputted.')
    print('Nothing will printed until it is finished.')
    for ee in range(1000):     # Change range to any int that is that is not 10 million or more
        motor.TeilAh(text.readline().split('\t'))
    print('The running time of this was {0:.2f} Seconds.'.format(time.time() - startTime))
    motor.Reiniger()


