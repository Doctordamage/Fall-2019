# Course:CS 2302 MW 1:30-2:50, Author:David Ayala
# Assignment:Lab #1, Instructor: Diego Aguirre
# Teaching Assistant: ????, Date of last Modification: 9/10/2019
# Purpose of program:Use recursion to generate all possible passwords
# and check to see if once hashed, that it matches the given hash.
import hashlib

# I put some German in this lab, since I'm currently taking it and
# I'm trying to get better at it.

# i is pronounced ee in German.
# j is pronounced yott in German.
# password is Passwort in German.
# Salt Value is Salzwert in German.
# line is Linie in German.
# Produce is erzeugen in German.
# compare is vergleichen in German.
# file is Datei in German.
# found is Gefunden in German.
# Characters is Schriftzeichen(for computing) in German.
# Confirm is bestätigen in German.

originalHashedPasswort = []
userID = []
Salzwert = []

# code that was given to use so that we can hash.
def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode("utf-8"))
    hex_dig = hash_object.hexdigest()
    return hex_dig

# saves passwords
def bestätigenPasswort(userID, minimumSchriftzeichen, maximumSchriftzeichen, Salzwert, originalHashedPasswort):
    Passworts = []
    if minimumSchriftzeichen < maximumSchriftzeichen:
        Passwort = erzeugenPasswort(userID, minimumSchriftzeichen, Salzwert, originalHashedPasswort)
        Passworts.append(Passwort)
        return Passworts + bestätigenPasswort(userID, minimumSchriftzeichen+1, maximumSchriftzeichen, Salzwert, originalHashedPasswort)
    return []

# produces passwords that will be return to and used in bestätigenPasswort
def erzeugenPasswort(userID, minimumSchriftzeichen, Salzwert, originalHashedPasswort):
    for ee in range(len(originalHashedPasswort)):
        for yott in range((len(originalHashedPasswort))*20):
            yott = str(yott).format(yott).zfill(minimumSchriftzeichen)
            Gefunden = vergleichenHash(yott, Salzwert[ee], originalHashedPasswort[ee], userID[ee])
    return Gefunden

# checks to see if the hashed password is the same as the one that was given.
def vergleichenHash(Passwort, Salzwert, originalHashedPasswort, userID):
    tempStr = Passwort + Salzwert
    tempHash = hash_with_sha256(tempStr)

    if tempHash == originalHashedPasswort:
        with open("PasswortsCracked.txt", "a+") as List:
            List.write(userID + " " + Passwort+ " ")
        print(userID + ":")
        print(originalHashedPasswort, tempHash, Passwort)
        return Passwort
    return

try:
    Datei = open("password_file.txt", "r")
except FileNotFoundError:
    print("File not located, please check again.")

for currentLinie in Datei:
    Salzwert.append(currentLinie.rstrip().split(",")[1])
    userID.append(currentLinie.rstrip().split(",")[0])
    originalHashedPasswort.append(currentLinie.rstrip().split(",")[2])

bestätigenPasswort(userID, 3, 7, Salzwert, originalHashedPasswort)
