# # Day 19  String, List & Number Function (Set 2)

# # String Functions
# text = "banana"
# print(text.count("a"))

# print("hello.py".endswith(".py"))
# print("Sales_Report.csv".startswith("Saes"))

# print("123".isdigit())
# print("456".isalpha())
# print("A1B2".isalnum())


# print("Line1\nLine2\n")
# print("Line1\nLine2\n".splitlines())


# #List Function
# nums =[5,2,7,1]
# nums.sort()
# print(nums)

# fruits = ["Banana","apple","Mango"]
# print(sorted(fruits))

# marks = [10,20,30]
# print(min(marks),max(marks),sum(marks))


# mylist = [1,2,1,3,2,5,2]
# print(mylist.count(2))
# print(mylist.index(2))


# a = [1,2]
# b = [3,4]
# a.extend(b)
# print(a)


# # Number Function
# print(round (3.7457,2))
# print(abs(-50))
# print(pow(3,2))
# print(divmod(10,3))
# print(sum([5,5,5],5))

# # Practical Examples
# products = [" mobile","Laptop","  TABLET"]
# clean = [p.strip().title() for p in products]
# clean.sort()
# print(clean)

# emails = ["rohit@gmail.com","sneaha@yahoo.com"]
# domains = [mail[mail.find("@")+1:] for mail in emails]
# print(domains)


mobiles = ["1728947198","l87597209438","847933849"]
valid = [m for m in mobiles if m.isdigit() and len(m) ==10]
print(valid)