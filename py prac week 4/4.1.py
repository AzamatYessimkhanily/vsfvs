n=int(input('row:'))
m=int(input('column:'))
a=[]
for i in range(n):
    b=[]
    for j in range(n):
        print(' [',i,',',j,'] ')
        b.append(int(input()))
    a.append(b)

for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
s=[]
for i in range(len(a)):
    s.append(sum(a[i]))
print(a[s.index(max(s))],'largest sum:',max(s),a[s.index(min(s))],'smallest sum:',min(s))
