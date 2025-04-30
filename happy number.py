a=int(input("Enter Number:"))
sum=0
dig=0
t=a
k=11
while k>=10:
    while a!=0:
        dig=a%10
        sum=dig**2+sum
        a=a//10
    k=sum
    a=sum
    sum=0
    
if k==1:
    print("It is Happy Number")
else:
    print("It is Not Happy Number")
