num1 = input("Enter first number  :  ")
num2 = input("Enter second number :  ")
op      = input("\nEnter Operator ( + , - , / , * ) :  ")

sum = int(num1) + int(num2)
dif = int(num1) - int(num2)
quo = int(num1) / int(num2)
pro = int(num1) * int(num2)

if op == "+" :
    print( "\nResult :  " , num1 , " + " , num2 , " = " , sum )
    
elif op == "-" :
    print( "\nResult :  " , num1 , " - " , num2 , " = " , dif )
    
elif op == "/" :
    print( "\nResult :  " , num1 , " / " , num2 , " = " , quo )
    
elif op == "*" :
    print( "\nResult :  " , num1 , " * " , num2 , " = " , pro )