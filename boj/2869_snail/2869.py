import sys
import math
input = sys.stdin.readline
n = input().split()
a, b, v = int(n[0]), int(n[1]), int(n[2])
d = math.ceil((v-a)/(a-b)) + 1
print(d)
