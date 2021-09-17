       
def PrimeFact(n):
    import math as ma
    factors = {}
    for i in range(2, int(ma.sqrt(n)) + 1):
        c = 0
        while n % i == 0:
            n//=i
            c+=1
            factors[i] = c
    if n > 1:
        factors[n] = 1
    return factors  

i = 1
while True:

    k = i*(i+1)//2
    factors = PrimeFact(k)
    mx = 1
    for key, v in factors.items():
        mx *= (v+1)

    if mx >= 500:
        print(k, i)
        break

    i+=1

