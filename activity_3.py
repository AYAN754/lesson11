def add(a,b):
    return a+b
    # print(input("enter number one: "))
    # print(input("enter number two: "))

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

print("please select the opration")
print("a.add")
print("b.sub")
print("c.mul")
print("d.div")
cho= input("please enter choise ,a,b,c,d")
num1= int(input("enter number 1: "))
num2= int(input("enter number 2: "))
if (cho == "a"):
    print(num1,"+", num2,"=", add(num1,num2))
elif(cho == "b"):
    print(num1,"-", num2,"=", sub(num1,num2))
elif(cho == "c"):
    print(num1,"*", num2,"=", mul(num1,num2))
elif(cho == "d"):
    print(num1,"/", num2,"=", div(num1,num2))
else:
    print("please enter a valid number")