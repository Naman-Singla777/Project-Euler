def fact(n):
    ans = 1
    for i in range(2, n+1):
        ans*=i
    return ans
m, n = map(int, input().split())
print(int(fact(m+n) / (fact(m) * fact(n))))
