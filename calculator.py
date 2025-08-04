import time
print("PY Calculator")

i = 0
while i < 50:
    opt = input("Enter a option: '+' '-' '*' '/' : ")

    def add():
        print("add")
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter the next number: "))
        sum = num1 + num2
        print("Answer = " + str(sum))
        time.sleep(5)
        

    def substract():
        print("substract")
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter the next number: "))
        sum = num1 - num2
        print("Answer = " + str(sum))
        time.sleep(5)
       

    def multiply():
        print("multiply")
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter the next number: "))
        sum = num1 * num2
        print("Answer = " + str(sum))
        time.sleep(5)
       

    def devide():
        print("devide")
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter the next number: "))
        sum = num1 / num2
        print("Answer = " + str(sum))
        time.sleep(5)
        
    
    if opt == "+":
        add()
        i=i+1
    elif opt == "-":
        substract()
        i=i+1
    elif opt == "*":
        multiply()
        i=i+1
    elif opt == "/":
        devide()
        i=i+1
    else :
        print("Invalid Option! ")
        time.sleep(2)
        print(" " * 70)
        i = i+1
