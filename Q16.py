import time as time
n = int(input())
initial = time.time()
arr = list(map(int, list(str(pow(2, n)))))
print(pow(2, n))
print(sum(arr))
print(time.time() - initial)
