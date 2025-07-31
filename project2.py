def get_number(number):
    while True:
        operand=input("Enter"+ str(number)+ " :")   
        try:
            return float(operand)
        except:
            print("Invalid number , try again.")
   
operand=get_number(1)
operand2=get_number(2)
# while True:
#     operand2=input("Enter Second number:")   
#     try:
#         operand2=float(operand2)
#         break
#     except:
#         print("Invalid number , try again.")


sign=input("Sign: ")
# valid=False
# try:
#     operand=float(operand)
#     operand2=float(operand2)
#     valid=True

# except:
#     print("! Enter valid numbers !")

# if valid:
result=0
if sign=="+":
    result=operand+operand2
elif sign=="-":
    result=operand-operand2
elif sign=="*":
    result=operand-operand2
elif sign=="/":
    if operand2!=0:
        result=operand/operand2
    else:
        print("number two is zero ")
else:   
    print("Invalid Sign ")    


print(result)        