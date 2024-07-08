def project_caesar(msg,key,mode):
    Letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    translated=''
    key %= 26
    msg=msg.upper()
    
    for i in msg:
        temp=Letters.find(i)
        if mode==1:
            temp+=key
        elif mode==2:
            temp-=key
        
        if temp >=len(Letters):
            temp-=len(Letters)
        elif temp < 0:
            temp+=len(Letters)
            
        translated+=Letters[temp]
    return translated

a=input("Enter the Message : ")
b=int(input("Enter the Key value : "))
print()
print("Enter '1' for Encryption  OR  Enter '2' for Decryption")
c=int(input("Enter your choice : "))

print(project_caesar(a,b,c))