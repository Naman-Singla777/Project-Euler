import time

s = int(input())

initial = time.time()

for i in range(2, s):
    a = 2*i
    b = i**2 - 1
    c = i**2 + 1
    if s % (a+b+c) == 0:
        k = s//(a+b+c)
        print(k*a, k*b, k*c)
        # print(k**3*a*b*c)
        # print(a)
