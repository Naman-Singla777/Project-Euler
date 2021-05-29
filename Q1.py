def trunc(n):
    return int(n)

def s2l(a, l):
    n = trunc((l-1)/a)
    n = float(n)
    return (n)*(n+1)*(a)/2

a = int(input())
b = int(input())
l = int(input())

print(int(s2l(a, l) + s2l(b, l) - s2l(a*b, l)))
