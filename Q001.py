# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#
# result = []
# for i in range(2000,3200 -1):
#     result

result = [str(i) for i in range(2000,3201) if i%7==0 and i%5!=0]
result = ",".join(result)
print(result)

l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

l =','.join(l)

print(l == result)
