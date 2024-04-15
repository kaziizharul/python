#A student does not allow which attendence is less then 75%.

attend=int(input("Enter how many classes you attend="))
held=int(input("Enter the number how many class is held="))


present=(attend/held)*100
if present>=75:
        print("You are selected for the exam.")

else:
    print("SORRY ! You are not selected for the exam.")