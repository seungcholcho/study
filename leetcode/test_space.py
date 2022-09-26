n=66
r,l=1,7
while True:
    if n <= l:
        print(r+1)
        break
    elif n > l:
        r+=1
        l = l + r * 6