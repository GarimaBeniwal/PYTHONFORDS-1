list1=[]
n1=int(input(" enter size of list1 "))
print("enter elements of list1")
for i in range(0,n1):
    element=int(input())
    list1.append(element)
    
print(list1)
def func(a,b):
        del list1[a:b]
        print(list1)
y=input("Do You want o delete or Insert:")
if(y=="delete"):
    z=input("You Want to delete by value or index or slice of elements:")
    if(z=="value"):
        a=int(input("Please Enter Element to delete: "))
        list1.remove(a)
        print(list1)
    elif(z=="index"):
        a=int(input("Please Enter Index to delete: "))
        list1.pop(a)
        print(list1)
    elif(z=="slice of elements"):
        p=int(input("index of 1st element to be removed"))
        q=int(input("index of last element to be removed"))
        print(func(p,q))
if(y=="insert"):
    a=int(input("enter element to be added"))  
    list1.append(a)
    print(list1)      



