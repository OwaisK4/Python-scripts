#!/usr/bin/python

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for letter in letters:
    if letter in "AEIOU":
        print(letter, "is a vowel")
    else:
        print(letter, "is a consonant")
