a, b, c = map(int, input().split())
if a > b:
    if a >= c:
        print(a)
    else:
        print(c)
elif a > c:
    if a >= b:
        print(a)
    else:
        print(b)
else:
    if b >= c:
        print(b)
    else:
        print(c)