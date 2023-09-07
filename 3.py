
string=str(input("enter the string:"))

def func(string):
    word=string.split(" ")
    req_string=" "
    for i in word:
        for j in range(len(i)):
            if j==0:
                if ord(i[0])>=97 and ord(i[0])<=122:
                    req_string+=(chr(ord(i[0])-32))
            else:
                req_string+=i[j]
        req_string+=" "     
    return req_string
print(func(string))      
                
                