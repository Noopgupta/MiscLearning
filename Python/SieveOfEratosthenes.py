# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 15:20:22 2025

@author: Admin
"""

# Sieve of Eratosthenes 
# https://www.geeksforgeeks.org/dsa/sieve-of-eratosthenes/

# Given a number n, find all prime numbers less than or equal to n.

# Examples:

# Input: n = 10
# Output: [2, 3, 5, 7]
# Explanation: The prime numbers up to 10 obtained by Sieve of Eratosthenes are [2, 3, 5, 7].

# Input: n = 35
# Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
# Explanation: The prime numbers up to 35 obtained by Sieve of Eratosthenes are [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31].

Output_list = [2]
n = 11

for i in range(3,n+1):
    IsPrime = True
    for j in range(2,i):
        if i%j == 0:
            IsPrime = False
            break
        
    if IsPrime:
        Output_list.append(i)
        
    
# Output_list = set(Output_list) 
print(Output_list)          

