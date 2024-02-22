score1, score2 = map(int, input().split())
score3, score4 = map(int, input().split())
if score1 > score3:
    print("A")
elif score1 < score3:
    print("B")
elif score2 > score4:
    print("A")
else:
    print("B")