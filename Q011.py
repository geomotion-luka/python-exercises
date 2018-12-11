
# #----------------------------------------#
# Question 11
# Level 2
#
# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.
rawInput = '0100,0011,1010,1001'
input = rawInput.split(',')
# input = input().split(',')
# print(input)
removeArray = []
for i in input:
    if len(i) != 4:
        removeArray.append(i)

for i in removeArray:
    input.remove(i)

totalArray = []
for i in range(len(input)):
    binary = list(input[i])
    total = 0
    index = 0
    for j in range(len(binary)-1,-1,-1):
        total += 2**index*int(binary[j])
        index += 1
    totalArray.append(total)
# print(totalArray)

result = []
for i in range(len(totalArray)):
    if (totalArray[i]%5 == 0):
        result.append(input[i])

print(','.join(result))
