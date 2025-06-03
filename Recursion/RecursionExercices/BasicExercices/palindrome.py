#! /usr/bin/python3

def is_palindrome(s):
    """
    pre: `s` est un str
    post: détermine itérativement si `s` est un palindrome ou non
    """
    reversed_s = s[::-1]
    for i in range(len(s)):
        if s[i] != reversed_s[i]:
            return False

    return True

#Exemple de test:
if not is_palindrome("kayak"):
    print("Erreur : kayak est un palindrome")