arr = []
for i in range(210, 231):
    interval.append(i)

res = [sub for sub in interval if len(set(str(sub))) == len(str(sub))]

print(str(res))