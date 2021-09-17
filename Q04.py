# import time
# initial = time.time()

arr = []

for i in range(100, 1000):
    s = str(i) + str(i)[::-1]
    arr.append(int(s))

arr = arr[::-1]

def main(arr):

    for x in arr:
        i = 999
        while i > 99:
        # for i in range(100, 1000):
            k = x/i
            if k == int(k) and k < 1000:
                print(i, k)
                return x
            i-=1
                

print(main(arr))
# print(time.time() - initial)
