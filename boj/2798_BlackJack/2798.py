import sys
input = sys.stdin.readline
s = 0
c = []
n = input().split()
p, b = int(n[0]), int(n[1])
n = input().split()
for i in range(0,p):
    c.append(int(n[i]))
for i in range(0,len(c)-2):
    for j in range(i+1,len(c)-1):
        for k in range(j+1,len(c)):
            t = c[i]+c[j]+c[k]
            if(b >= t > s):
                s = t
print(s)