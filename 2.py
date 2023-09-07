list1=[]
list2=[]
n1=int(input('size1:'))
n2=int(input('size2:'))
print("enter elements for list 1")
for i in range(0,n1):
    
    element1=int(input())
    list1.append(element1)
print("enter elements for list 2")
for i in range(0,n2):
    
    element2=int(input())
    list2.append(element2)
for i in list2:
    list1.append(i)
print (list1)        
    

