
primelist =[]
minprime=3
while True:
    prime =True
    for i in range(2,minprime):
        if minprime%i==0:
            prime=False
            break
    if prime:
        primelist.append(minprime)
    minprime+=1
    if len(primelist)==1000:
        break
mynums = []
for startEnd in primelist:
    if str(startEnd)[0]=="3" and str(startEnd)[-1]=="7":
        mynums.append(startEnd)
        print(startEnd)
print(mynums)


        
    
             
        