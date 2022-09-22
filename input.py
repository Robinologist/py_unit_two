import math

value1=input("What is value 1?\n")
value2=input("What is value 2?\n")
operator=input("What operator?\n")
output = ""

if operator == "+":
    output = float(value1) ++ float(value2)
else:
    if operator == "-":
        output = float(value1) - float(value2)
    else:
        if operator == "*":
            output = float(value1) * float(value2)
        else:
            if operator == "/":
                output = float(value1) / float(value2)
            else:
                print("error")
print(output)