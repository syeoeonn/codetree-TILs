a_p, a_t = input().split()
b_p, b_t = input().split()
c_p, c_t = input().split()
a_t, b_t, c_t = int(a_t), int(b_t), int(c_t)
if a_p == "Y" and a_t >= 37:
    a = "A"
else:
    a = "N"
if b_p == "Y" and b_t >= 37:
    b = "A"
else:
    b = "N"
if c_p == "Y" and c_t >= 37:
    c = "A"
else:
    c = "N"

if a == "A":
    if b == "A" or c == "A":
        print("E")
    else:
        print("N")
elif b == "A" and c == "A":
    print("E")
else:
    print("N")