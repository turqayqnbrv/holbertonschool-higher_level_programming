#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming language that combines remarkable power with very clear syntax"
words = str.split()
str = " ".join(words[7:10]) + " with " + words[0]
print(str)
