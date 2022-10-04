import sys
import math
input = sys.stdin.readline

n = input().split()
a, b, v = int(n[0]), int(n[1]), int(n[2])

temp = v-a
temp2 = temp/(a-b)
print(temp2)
day = math.ceil(temp/(a-b)) + 1

print(day)
