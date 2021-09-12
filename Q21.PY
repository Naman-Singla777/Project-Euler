import math as ma
def main(n):
    arr = [1]
    for i in range(2, int(ma.sqrt(n)) + 1):
        if n % i == 0:
            arr.append(i)
            x = n//i
            if i != x:
                arr.append(x)

    return sum(arr)

n = int(input())
print(main(n))
