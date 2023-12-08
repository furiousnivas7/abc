def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiple(a,b):
    return a*b
def divide(a,b):
    return a/b
def power(a,b):
    return a**b
def reminder(a,b):
    return a%b
def invalid_syntex(a,b):
    return "# is a invalaid syntex"

def select_choise(choise):
    if (choise== "#"):
        print(invalid_syntex(a,b))
    elif(choise=="+"):
        print(add(a,b))
    elif(choise=="-"):
        print(subtract(a,b))
    elif(choise=="*"):
        print(multiple(a,b))
    elif(choise=="/"):
        print(divide(a,b))
    elif(choise=="**"):
        print(power(a,b))
    else:
        print(reminder(a,b))
    
while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ** ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
    choise=input("please enter your arithmetic operator : ")
    if(choise=="#"):
       break
    elif(choise=="$"):
        continue
    else:
        a=int(input("please enter number 1 : "))
        b=int(input("please enter number 2 : "))
        select_choise(choise)
