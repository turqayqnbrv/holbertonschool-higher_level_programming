#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
words = str.split()
middle = " ".join(words[5:7])
str = middle + " with " + words[0]
print(str)
