# #----------------------------------------#
# Question 9
# Level 2
#
# Question£º
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

while True:
    s = input()
    if s:
        print(s.upper())
    else:
        break
