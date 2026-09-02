#brute force approach till n/2
# n = 20
# facts = []
# count = 0
# for i in range(1,(n//2)+1):
#     if n%i == 0:
#         facts.append(i)
# facts.append(n)
# print(facts)

#optimal approach
from math import *
n = 25
result = []
for i in range(1, int(sqrt(n))+1):
    if n%i == 0:
        result.append(i)
        if n//i != i:
            result.append(n//i)
print(result)