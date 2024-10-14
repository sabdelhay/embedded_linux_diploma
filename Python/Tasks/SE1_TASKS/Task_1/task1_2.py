#!/usr/bin/python3

def vowels_check(letter):
    vowels = str(["a", "e", "i","o","u"]).lower()
    return print ("Letter is a vowel ") if letter in vowels else print("The letter is a consonant")
    
vowels_check('x')