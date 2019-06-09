t = list(map(int, input().split()))
t1, t2 = [], []

for i in t:
    if i > 5:
        t1.append(i)
    elif i <= 2:
        t2.append(i)

print(*t1)
print(*t2)