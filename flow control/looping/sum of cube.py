num=int(input("enter the number:"))
sum=0
digit=0
while(num!=0):
    digit=num%10
    sum+=digit*digit*digit
    num=num//10
print(sum)