n = int(input())
p = 1
c = 2
s = 0
while c < n+1:
    if c % 2 == 0:
        s+=c
    temp = c
    c+=p
    p = temp
    
print(s)
