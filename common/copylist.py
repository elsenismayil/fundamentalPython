#copied list
b = [2, 3, 4, 5, 6, 7, 8]
for x in b[:]:
    b.remove(x)
print(b)
#************************************
#reverse loop
b = [2, 3, 4, 5, 6, 7, 8]
for t in range(len(b)-1,-1,-1):
    b.remove(b[t])
print(b)
