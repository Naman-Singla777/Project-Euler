import math as ma
def SieveOfEratosthenes(n):
    nums = {}
    s = 0
    for i in range(2, n+1):
        nums[i] = 1

    for i in range(2, int(ma.sqrt(n) + 1)):

        if nums[i] == 1:
        
            k = 2
            m = k*i
            while m <= n:
                k+=1
                nums[m] = 0
                m = k*i

    # ans = []
    for k in nums:

        if nums[k] == 1:
            s+=k
    #         ans.append(k)
    
    return s

n = int(input())
print(SieveOfEratosthenes(n))
