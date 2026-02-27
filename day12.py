# # Day 12 - While Loop

# # 1 Basic while loop

# i=1
# while i<=10:
#     print(i)
#     i+=1


# # 2 Countdown
# n=10
# while n>0:
#     print(n)
#     n-=1


# # 3 Ask user until valid input
# num = ""
# while not num.isnumeric():
#     num = input("Enter any value:")
# print("Number accepted:", num)

# # 4 Loop through list using while
# items = ["Apple", "Banana", "Grapes"]
# i = 0
# while i < len(items):
#     print(items[i])
#     i+=1    



# # 5 Using break
# x = 1
# while x <= 10:
#     print(x)
#     if x == 5:
#         break
#     x+=1



# # 6 Using continue
# x = 0
# while x < 10:
#     x+=1
#     if x%2 == 0:
#         continue
#     print(x)



# # 7 Password System (Advanced)
# password = ""
# attempts = 0
# while password != "admin123" and attempts < 3:
#     password = input("Enter the password:") 
#     attempts += 1
#     if password == "admin123": 
#         print("Access granted!")
#     else:
#         print("Incorrect password. Try again, Attempts left:", 3 - attempts)
# else:
#     print("Too many failed attempts. Access denied.")



