nums = [1,3,5,2,9,6,]
newNums = []
for a in range(len(nums)):
    newNums.append(min(nums))
    nums.remove(min(nums))
nums=newNums
print(nums)

#**********************************************

numbers = [1, 3, 5, 2, 9, 6]
n = len(nums)
length = len(numbers)
for t in range(length):
    for j in range(length - 1 - t):
        if numbers[j] > numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp
print(numbers)

    
   
