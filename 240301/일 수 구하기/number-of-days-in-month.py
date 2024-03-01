m = int(input())
if m == 2:
    print("28")
elif m <= 7 and m % 2 == 0:
    print("30")
elif m <= 7 and m % 2 != 0:
    print("31")
elif m % 2 == 0:
    print("31")
else: 
    print("30")