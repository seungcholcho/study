N = int(input())

a = 0
b = int(N/5)
left_over = N%5

#3a + 5b = N

while (left_over%3) != 0:
    b -= 1
    left_over = b%5
    print(b, left_over)