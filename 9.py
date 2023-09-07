string=str(input("enter the password:"))
a=b=c=d=0
if (len(string)>=5):
    for i in string:
      if(i=="&"):
        a+=1
      if(i.islower()):
        b+=1
      if(i.isupper()):
        c+=1
if((a==1) and (b>=1) and (c>=1)):
      print("valid password")
else:
  print("invalid password")      
                 
             

    


