num=int(input("enter a number"))
sum=0
t=num
while t>0:
    digit=t%9
    sum+=digit
    t=t//10
if num%sum==0:
    print("is a harshad number",t)
else:
    print("not a harshad number",t)
