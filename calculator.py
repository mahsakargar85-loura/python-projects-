def calculator ():
    print("choose amaliyat: + - * / ")
    op= input ("amalgar")
    a=float (input("adad aval:"))
    b=float(input("adad du:"))

    if op== "+":
        print("natije:", a+b)
    elif op=="-" :
        print("natije:", a-b)   
    elif op == ("*") : 
        print("natije :" , a*b)  
    elif op == ("/"):
       if b!=0:
        print("natije:", a/b)
       else:
          print("mojaz nist")
    else :
       print("namotabar!")

calculator()      
    
