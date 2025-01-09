def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
cal_dictionary={"+":add,
               "-":subtract,
               "*":multiply,
               "/":divide}
done=False
while not done:
    num1=float(input("Enter the first number: "))
    finish=False
    while not finish:
        op=input("Pick an operation:\n'+'\n'-'\n'*'\n'/'\n")
        num2=float(input("Enter the second number: "))
        result=cal_dictionary[op](num1,num2)
        print(f"{num1} {op} {num2} = {result}")
        conti=input("Do you want to continue? yes or no : ")
        if conti=="yes":
            rep=input("Do you want to continue with the result or new number? r or n : ")
            if rep=="r":
                num1=result
            elif rep=='n':
                finish=True
        elif conti=="no":
            finish=True
            done=True
        
