
a=input("enter string of numbers seperated by spabe:")
list1=a.split()
list2=[]
for i in list1:
    list2.append(int(i))
n1=len(list2)
def sort(list):
    
    for i in range(0,n1-1):
        min_pos=i
        for j in range(i+1,n1):
            if list[j]<list[min_pos]:
                min_pos=j
        list[i],list[min_pos]=list[min_pos],list[i] 
    print(list)
print(sort(list2))               