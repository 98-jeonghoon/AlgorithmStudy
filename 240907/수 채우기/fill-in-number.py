cost = int(input())
cnt = 0
while (cost > 0):
    if ((cost - 5) > 0 and (cost - 5) % 2 == 0 or cost % 5 == 0):
        cost -= 5
        cnt += 1
    else:
        cost -=2
        cnt += 1
    if (cost == 1):
        cnt = -1
        break
print(cnt)