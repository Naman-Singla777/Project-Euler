# n = int(input())
n = 20
mat = []
for _ in range(n):
    arr = list(map(int, input().split()))
    mat.append(arr)

hor = 0

for i in range(n):
    curr = 1
    for j in range(n-3):
        curr = mat[i][j]*mat[i][j+1]*mat[i][j+2]*mat[i][j+3]
        if curr > hor:
            hor = curr
         
ver = 0

for i in range(n):
    for j in range(n-3):
        curr = mat[j][i]*mat[j+1][i]*mat[j+2][i]*mat[j+3][i]
        if curr > ver:
            ver = curr

right_dia = 0

for i in range(n-3):
    for j in range(n-3):
        curr = mat[i][j]*mat[i+1][j+1]*mat[i+2][j+2]*mat[i+3][j+3]
        if curr > right_dia:
            right_dia = curr

left_dia = 0

for i in range(n-3):
    for j in range(n-3):
        curr = mat[i][j+3]*mat[i+1][j+2]*mat[i+2][j+1]*mat[i+3][j]
        if curr > left_dia:
            left_dia = curr

print(max(hor, ver, right_dia, left_dia))
