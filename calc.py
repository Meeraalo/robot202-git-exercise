def do(a,b,o):
    if o=="+":
        return a+b
    if o=="-":
        return a-b
    if o=="*":
        return a*b
    if o=="/":
        if b==0:
            print("Zero division")
            return 0
        return a/b
    if o=="+":
 	    return a+b
    else:
        print("Invaild input") 
        return
print("CALCULATOR") 
print("Please Enter") 
x=input("1st number")
y=input("2nd number")
z=input("choose an operation: + , - , * , /")
print("Answer is:",  do(int(x),int(y),z))