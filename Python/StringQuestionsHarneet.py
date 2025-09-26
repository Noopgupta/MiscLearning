# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 17:36:33 2025

@author: Admin
"""
"""
🔤 String Counting and Analysis
	1.	wordCount(S1)
➡️ Write a function that counts the total number of words in a given string.
	2.	spaceCount(S2)
➡️ Write a function that counts the total number of spaces in a given string.
	3.	charCount(S3) (without space)
➡️ Write a function that counts the total number of characters in a string, excluding spaces.
	4.	vowelCount(S10)
➡️ Write a function that counts the total number of vowels (a, e, i, o, u) in a string.
	5.	length1(S11)
➡️ Write a function that returns the length of a string without using the built-in len() function.
	6.	frequencyCount(S12)
➡️ Write a function that prints the frequency of each character in a string, in frequency-wise order.
	7.	wordFrequencyCount(S)
➡️ Write a function that counts the frequency of each word in a string.


	8.	ascii2(c)
➡️ Write a function that returns the ASCII value of a given character.

🔄 String Modification
	9.	reverse(S4)
➡️ Write a function that returns the reverse of a given string.
	10.	palindrome(S5) (e.g., “abcddcba”)
➡️ Write a function that checks if a given string is a palindrome (reads the same forward and backward).
	11.	lTrim1(S6)
➡️ Write a function that removes all spaces from the left side of a string.
	12.	rTrim1(S7)
➡️ Write a function that removes all spaces from the right side of a string.
	13.	allTrim(S8)
➡️ Write a function that removes spaces from both sides of a string.
	14.	squeeze(S9)
➡️ Write a function that removes extra spaces between words in a string (only single space should remain between words).
	15.	changeCase(S13) (Example: IndIa → iNDiA)
➡️ Write a function that converts each uppercase letter to lowercase and each lowercase letter to uppercase.
	16.	singleOccurence(S14) (Example: nniittiinn → nitin)
➡️ Write a function that removes repeated consecutive characters and keeps only a single occurrence.
	17.	replace(S19_1, S19_2, S19_3)
➡️ Write a function that replaces all occurrences of a substring in S19_1 with another substring.

⸻

🔤 Sorting and Searching
	18.	sortedOrder(S15)
➡️ Write a function that returns the characters of a string in sorted order.
	19.	sortedWord(S)
➡️ Write a function that sorts all words of a string alphabetically and returns the sorted string.
	20.	find(S18_1, S18_2)
➡️ Write a function that checks if the second string (S18_2) exists inside the first string (S18_1).
	21.	equals(S20_1, S20_2)
➡️ Write a function that checks if two strings are exactly equal (case-sensitive).
	22.	compare(S25, S26)
➡️ Write a function that compares two strings lexicographically (like dictionary order).
	23.	SequenceCount(S)
➡️ Write a function that counts the number of consecutive repeated character sequences in a string (e.g., “aaabbc” → 3 sequences: “aaa”, “bb”, “c”).



Print these formats with variable names:::
H
Ha
Har
Harn
Harne
Harnee
Harneet

Harneet
Harnee
Harne
Harn
Har
Ha
H

      t
     et
    eet
   neet
  rneet
 arneet
Harneet

Harneet
 arneet
  rneet
   neet
    eet
     et
      t

      tH
     etHa
    eetHar
   neetHarn
  rneetHarne
 arneetHarnee
HarneetHarneet

HarneetHarneet
Harnee  arneet
Harne    rneet
Harn      neet
Har        eet
Ha          et
H            t


H 
H a 
H a r 
H a r n 
H a r n e 
H a r n e e 
H a r n e e t 
H a r n e e 
H a r n e 
H a r n 
H a r 
H a 
H 

H a r n e e t 
  a r n e e t 
    r n e e t 
      n e e t 
        e e t 
          e t 
            t 
            t 
          e t 
        e e t 
      n e e t 
    r n e e t 
  a r n e e t 
H a r n e e t 

                           t H
                         e t H a
                       e e t H a r
                     n e e t H a r n
                   r n e e t H a r n e
                 a r n e e t H a r n e e
               H a r n e e t H a r n e e t
 H a r n e e t                             H a r n e e t
   a r n e e t                             H a r n e e
     r n e e t                             H a r n e
       n e e t                             H a r n
         e e t                             H a r
           e t                             H a
             t                             H
             t                             H
           e t                             H a
         e e t                             H a r
       n e e t                             H a r n
     r n e e t                             H a r n e
   a r n e e t                             H a r n e e
 H a r n e e t                             H a r n e e t
               H a r n e e t H a r n e e t
                 a r n e e t H a r n e e
                   r n e e t H a r n e
                     n e e t H a r n
                       e e t H a r
                         e t H a
                           t H
                           
                           
# Two strings are said to be complete if on concatenation, they contain all the 26 English alphabets. 
# For example, “abcdefghi” and “jklmnopqrstuvwxyz” are complete as they together have all characters from ‘a’ to ‘z’. 
# We are given two sets of sizes n and m respectively and we need to find the number of pairs that are complete 
# on concatenating each string from set 1 to each string from set 2

"""