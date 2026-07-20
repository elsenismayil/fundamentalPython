nums = int(input("enter num"))
for i in range(1,(nums+1)):
    if i == 1 or i ==nums:
       continue
    elif nums%i==0:
        print(f"{nums} is no primary num")
        break
    else:
        print(f"{nums} is primary num")
        break
    
a =int(input("enter num"))
prime = True
for z in range(2,a):
    if a%z==0:
        prime=False
        break
if prime is True:
    print("primary")
else:
    print("no primary")


    


