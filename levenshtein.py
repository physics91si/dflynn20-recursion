#!/usr/bin/env python3

# Lab 16: Recursion
# Levenshtein Distance


def lev(s1, s2):
    if s1 == "" and s2 == "":
        return 0
    elif s1 == "":
        return (1 + lev(s1, s2[1:]))
    elif s2 == "":
        return (1 + lev(s1[1:], s2))
    elif s1[0] == s2[0]:
        return lev(s1[1:],s2[1:])
    else:
        x = 1 + lev(s1[1:], s2)
        y = 1 + lev(s1, s2[1:])
        z = 1 + lev(s1[1:], s2[1:])
        return min(x,y,z)
    
        
    
    
    
    