length = int(input())
numbers = list(map(int, input().split()))

cnt = 0
for num in numbers:
    count = 0
    for i in range (1 , num+1):
        if (num % i == 0):
            count += 1
        if count>2 or num == 1:
            cnt += 1
            break

print(len(numbers)-cnt)