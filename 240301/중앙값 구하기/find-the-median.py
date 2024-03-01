a, b, c = map(int, input().split())
if a > b:
    if b > c:
        print(b)
    elif c > a:
        print(a)
    else:
        print(c)
else: 
    if c > b:
        print(b)
    elif c > a:
        print(c)
    else:
        print(a)