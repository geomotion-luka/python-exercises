# #----------------------------------------#
# Question 10
# Level 2
#
# Question:
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

input = "hello world and practice makes perfect and hello world again"
# input = input().split(" ")
input = input.split(" ")
input.sort()

removeArray = []

for i in range(1, len(input)):
    if (input[i] == input[i-1]):
        removeArray.append(input[i])

for i in removeArray:
    input.remove(i)

print(input)
