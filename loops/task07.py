numbers = [5, -3, 8, -1, 0, 7]
positive=[]
negative=[]
for i in numbers:
    if i>0:
        positive.append(i)
    elif i<0:
        negative.append(i)
print("Positive numbers:", positive)
print("Negative numbers:", negative)