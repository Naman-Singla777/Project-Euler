n = list(input())
n = list(map(int, n))
mx = 0
for i in range(len(n)-12):
    curr = 1
    for j in range(13):
        curr = curr*n[i+j]
    # curr = n[i]*n[i+1]*n[i+2]*n[i+3]
    if curr > mx:
        mx = curr
print(mx)
