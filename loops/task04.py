numbers = [12, 5, 78, 34, 2, 90]

for k in numbers:
    big = numbers[0]
    if k>big:
        big = k
print(big)
print(max(numbers))