a_n, a_s = input().split()
b_n, b_s = input().split()
a_n, b_n = int(a_n), int(b_n)
if (a_n >= 19 and a_s == 'M') or (b_n >= 19 and b_s == 'M'):
    print(1)
else:
    print(0)