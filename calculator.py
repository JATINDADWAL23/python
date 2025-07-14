print("What do you want to do " \
"\n Add,Sub,Mul,Divide")

a=input().lower()

if a not in ["add", "sub", "mul", "divide"]:
    print("Error  Please choose from Add, Sub, Mul, Divide.")
    exit()

print("Enter first value:")
b=int(input())
print("Enter second value:")
c=int(input())
def add(b,c):
    return b+c
def sub(b,c):
    return b-c
def mul(b,c):
    return b*c
def divide(b,c):
    if c == 0:
        return "Cannot divide by zero"
    else:
        return b/c
if a == "add":
    print("Result:",add(b,c))

elif a == "sub":
    print("Result:",sub(b,c))
elif a == "mul":
    print("Result:",mul(b,c))
elif a == "divide":
    print("Result:",divide(b,c))
