import math as ma 
def IsPrime(n):
    for i in range(2, int(ma.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

target = int(input())
c = 1
i = 2
while c <= target:
    if IsPrime(i) == True:
        c+=1
    i+=1

print(i-1)
