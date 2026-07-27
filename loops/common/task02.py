umi = []
count=3
while True: 
    prime = True
    for i in range(2,count):
       if count%i==0:
           prime=False
           break
    if prime is True:
        umi.append(count)
    if int(umi[-1])>=10000:
       break
    count +=1
print(umi)




       

    
        