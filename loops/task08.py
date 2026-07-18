a =11223345
b =list(str(a))
c =[]
print(b)
for k in b:
    if k in c:
        print(f"{k} is repeated")
    else:
        c.append(k)
