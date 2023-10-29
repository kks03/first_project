# 1








# 2

"""
from collections import deque

def func(prices):
    result = deque()
    for i in range(len(prices)):
        count = 0
        for j in range(i+1,len(prices)):
            if prices[i] <= prices[j]:
                count += 1
        result.append(count)
    return result

prices = [1000,2000,3000,2000,3000]

print(func(prices))
"""

# 3

from collections import Counter

f1 = open("06 file01.txt",'r')
f2 = open("06 file02.txt","r")

list1 = f1.readlines()
list2 = f2.readlines()

n1 = []
n2 = []

for i in range(len(list1)):
    list1[i] = list1[i].strip('\n')
    n1 = n1 + list1[i].split()
for i in range(len(list2)):
    list2[i] = list2[i].strip('\n')
    n2 = n2 + list2[i].split()

c1 = Counter(n1)
c2 = Counter(n2)

c3 = list(dict(c1 & c2).keys())

print('공통된 단어와 각 파일에서의 빈도:')
for i in range(len(c3)):
    print("'"+c3[i]+"': 파일 1 - "+str(c1[c3[i]]),end = '')
    print(", 파일 2 - "+str(c2[c3[i]]))