# # Day 18 - Functions(def, return)


# def greet():
#     print("Hello python Learners")
#     print("Learning Function")
# greet()

# def welcome(name):
#     print("Welcome",name)

# welcome("Nitesh")


# def add(a,b):
#     print("a+b :",a+b)
# add(20,33)


# def add(a,b):
#     return a + b
# sum = add (10,33)
# print(sum)


# def clean_text(value):
#     return value.strip().title()
# output = clean_text("    muMbai    ")
# print(output)

# def fix_city(city):
#     city = city.lower().strip()
#     city = city.replace("mombai","mumbai")
#     city = city.replace("kolkatta","kolkata")
#     return city.title()
# print(fix_city("  mombai  "))


# def get_year(code):
#     return code[-4:]

# print(get_year("Laptop-2024"))

# def is_valid_email(email):
#     return "@" in email and "." in email

# print(is_valid_email("test@gmail.com"))


# def total_salary (basic,bonus):
#     return basic + bonus
# print(total_salary(20000,500))


# def stats(nums):
#     return min(nums),max(nums), sum(nums)/len(nums)
# print(stats([10,20,30]))



# def clean_list(values):
#     cleaned = []
#     for v in values:
#         cleaned.append(v.strip().title())
#     return cleaned
# print(clean_list(["delhi"," MUMBAI", "pUne"]))