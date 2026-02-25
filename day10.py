# Assignment Set 1- Multi-Level Varification System
'''ASSIGNMENT SET 1 — Multi-Level
Verification System

• You are working for a company that wants to verify visitors before giving
them access to a confidential meeting room.
•
You have to write a Python program that checks three conditions in
sequence:

Conditions:

Condition 1:
Ask the user to enter a security code.
If the security code is correct (5566) → move to Condition 2
If the code is wrong → print "Invalid security code." and stop.
Condition 2:
Ask the user to enter their employee department.
If the department is "Finance" → move to Condition 3
If not Finance → print "Access denied: Department not allowed." and stop.
Condition 3:
Ask the user for their access level.
If the access level is 5 or above → print "Access Granted: Welcome to the meeting room."
If access level is less than 5 → print "Insufficient access level."'''


# security_code = int(input("Enter the security code: "))
# if security_code == 5566:
#     department = input("Enter your department: ")
#     if department.lower() == "finance":
#         access_level = int(input("Enter your access level: "))
#         if access_level >= 5:
#             print("Access Granted: Welcome to the meeting room.")
#         else:
#             print("Insufficient access level.")
#     else:
#         print("Access denied: Department not allowed.")
# else:
#     print("Invalid security code.")



'''ASSIGNMENT SET 2 — Online Exam
Login

• Create a program for an online exam system:
• Ask the user for a registration number.
• If reg no = 1221, go ahead
• Else: “Registration failed.”
• Ask for exam subject.
• If subject is Python, continue
• Else: “Subject not available.”
• Ask for password.
• If password = 8888, print “Login successful! Start your exam.”
• Else: “Wrong password.”'''


# registration_number = int(input("Enter your registration number: "))    
# if registration_number == 1221:
#     subject = input("Enter the exam subject: ")

#     if subject.lower() == "python":
#         password = int(input("Enter your password: "))

#         if password == 8888:
#             print("Login successful! Start your exam.")
#         else:
#             print("Wrong password.")
#     else:
#         print("Subject not available.")
# else:

#     print("Registration failed.")
