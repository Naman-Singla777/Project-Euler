import math as ma
n = int(input())
ans = 1
for i in range(1,n+1):
    x = ma.gcd(ans, i)
    ans*=(i//x)
print(ans)
