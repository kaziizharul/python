#Enter any three number and find out the large number.

First=int(input("Enter your first number="))
Second=int(input("Enter your second number="))
Third=int(input("Enter your third number="))

if First>Second and First>Third:
    print("First number is large.")

elif Second>First and Second>Third:
    print("Second number is large.")

else:
    print("Third number is large.")
