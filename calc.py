def do(a,b,o):
    if o=="add":
        return a+b
    if o=="sub":
        return a-b
    if o=="mult":
        return a*b
    if o=="div":
        if b==0:
            print("error divion by zero") 
            return None
        
    return a/b
    if o=="plus":
 	    return a+b
    else:
        print("wut?") 
        return
print("CALCULATOR") 
print("Do math ok!!") 
x=input("1st number")
y=input("2nd number")
z=input("do wut")
print("Answer is:",  do(int(x),int(y),z))