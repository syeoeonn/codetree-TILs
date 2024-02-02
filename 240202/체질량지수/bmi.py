h, w = map(int, input().split())
h /= 100
print(int(w//h**2))
if w/h**2 >= 25:
    print("Obesity")