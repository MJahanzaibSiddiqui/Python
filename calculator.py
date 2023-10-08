def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def power(x, y):
    return x ** y
def percentage(x, y):
    return (x * y) / 100

print("Select operation")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")
print("5. POWER")
print("6. PERCENTAGE")

while True:
    choice=input("Enter choice (1/2/3/4/5/6):")
    if choice in ('1','2','3','4','5','6'):
        num1=float(input("Enter first number"))
        num2=float(input("Enter Second number"))
        
        if choice =='1':
            print (num1,"+",num2,"=", add(num1,num2))
        elif choice =='2':
              print (num1,"-",num2,"=", sub(num1,num2))
        elif choice=='3':
              print (num1,"x",num2,"=", multiply(num1,num2))
        elif choice=='4':
              print (num1,"/",num2,"=", divide(num1,num2))
        elif choice == '5':
            print(num1, "power", num2, "=", power(num1, num2))   
        elif choice == '6':
            print(num2, "percent of", num1, "=", percentage(num1, num2))       
        else:
            print("Invalid operation")      
        next_calculation=input("Do you want to perform one more calculation? (yes/no):")
        if next_calculation=="no":
            break      
       
                
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              