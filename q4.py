# Author: Antonio Loureiro Dunch
# GitHub username: aloureirodunch
# Date: April 16th, 2026
# Description: asks for a word and prins some manipulations of it.

word = input("Enter any word: ")

print(f"The first character is: {word[0]}")

print(f"The last character is: {word[len(word)-1]}")

print(f"The first four characters are: {word[0:4:1]}")

print(f"Every other character in the word is {word[::2]}")

print(f"The word backwards is {word[::-1]}")