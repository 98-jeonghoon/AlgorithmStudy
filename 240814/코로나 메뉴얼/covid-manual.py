f = input().strip().split()
s = input().strip().split()
t = input().strip().split()

c1, tem1 = f[0], int(f[1])
c2, tem2 = s[0], int(s[1])
c3, tem3 = t[0], int(t[1])

def classify(cold, temp):
    if cold == "Y":
        if temp >= 37:
            return "A"
        else:
            return "C"
    else:
        if temp >= 37:
            return "B"
        else:
            return "D"

F = classify(c1, tem1)
S = classify(c2, tem2)
T = classify(c3, tem3)

count_A = [F, S, T].count("A")

if count_A >= 2:
    print("E")
else:
    print("N")