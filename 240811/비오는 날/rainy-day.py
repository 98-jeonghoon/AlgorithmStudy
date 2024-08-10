n = int(input())
cloud = []

for _ in range(n):
    aa = list(input().split())
    date_parts = list(map(int, aa[0].split("-")))
    date_parts.append(aa[1])  
    date_parts.append(aa[2])  
    cloud.append(date_parts)

rainy_days = [entry for entry in cloud if entry[4] == "Rain"]


rainy_days.sort(key=lambda x: (x[0], x[1], x[2]))


nearest_rainy_day = rainy_days[0]
print(f"{nearest_rainy_day[0]:04}-{nearest_rainy_day[1]:02}-{nearest_rainy_day[2]:02} {nearest_rainy_day[3]} {nearest_rainy_day[4]}")