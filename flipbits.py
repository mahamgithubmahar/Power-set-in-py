def flips(num1, num2):
    flip=0
    while(num1>0 or num2>0):
        t1=num1&1
        t2=num2&1

        if(t1!=t2):
            flip+=1

        num1>>=1
        num2>>=1
    
    return flip

num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))

print("The number of flips needed to make the numbers equal is",flips(num1, num2))