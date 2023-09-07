n=int(input("enter a number"))
str=[]
while(n>0):
    a=n%2
    str.append(a)
    n=n//2
str.reverse()
print("binary equivalent is")
for i in str:
    print(i,end=" ")    
    