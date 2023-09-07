
 
upper=lower=number=special = 0

string=str(input("enter the string"))
for i in range(len(string)):
    if ord(string[i]) in range(97,123):     
        lower+=1
    elif ord(string[i]) in range(65,91):
        upper+=1
    elif ord(string[i]) in range(48,58):
        number+=1
    else:
        special+=1  
         

print("No of alphabets:",upper+lower)
print("No of digits:",number)
print("No os symbols:",special)
print("No of uppercase alphabets:",upper)
print("No of lowercase alphabets:",lower)


 

          
         
    
 
    