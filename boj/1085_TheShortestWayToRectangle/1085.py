import sys
input = sys.stdin.readline
n = input().split()
for i in range(0,4):
    n[i] = int(n[i])
n[2] = n[2]-n[0]
n[3] = n[3]-n[1]
print(min(n))
