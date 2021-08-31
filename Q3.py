def PrimeFact(n):
    import math as ma

    ans = []


    for i in range(2, n):
        
        while n % i == 0 and n != 1:
            ans.append(i)
            n = n // i

        if n == 1:
            return i           
    # return i

n = int(input())
print(PrimeFact(n))
