
a=[0,1,1,2]
for i in range(10):
    if i==0 or i==1 or i ==2 or i==3:
        continue
    else:
        a.append(a[i-1]+a[i-2])

for k in a:
    print(k)



num = [0, 1]

for t in range(8):
    num.append(num[-1] + num[-2])

for z in num:
    print(z)