medical_cause=input("Student do you have a medical issue write Y or N")
if medical_cause=="Y":
   print("you are allowed to attend the exam")
else:
    atten=int(input(" attendance percentage write number"))

    if atten>=75:

        print("Allowed")
    else:
        print("Not Allowed")

   

