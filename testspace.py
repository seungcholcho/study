list1 = [1,0,0,0,2,3,0,0]

i=0
while (i<=len(list1)):
    print(i, list1)
    if list1[i]==0:
        print("deleting index: ", i)
        del list1[i]
        print(list1)
        i-=1
    i+=1
    

print(list1)