rev=0
num=int(input("enter number"))
t=num
while num!=0:
    d=num%10
    rev=rev*10+d
    num=num//10
if rev==t:
   print(t,"is palindrome")
else:
   print(t,"not palindrome") 
