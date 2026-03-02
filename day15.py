# # day 15 - Dictionaries

# student = {"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
# print(student)


# # Accessing values
# print(student["name"])
# print(student["age"])


# # Adding and Updating

# student["phone"] = "555-5555"  
# student["age"] = 26  
# print(student)



# # Removing items

# student.pop("phone") 
# print(student)

# # Dictionary methods
# print(student.keys())
# print(student.values())
# print(student.items())
# print(student.get("name"))

# # Looping

# for k in student:
#     print(k, student[k])



# # Nested dictionaries
# students = {
#     "student1": {"name": "John", "age": 25},
#     "student2": {"name": "Alice", "age": 30}
# }
# print(students["student2"]["name"])


# # Mapping wrong -> correct
# mapper = {
#     "mombai": "Mumbai",
#     "kokatta": "Kolkata",
#     "delhi": "Delhi"
# }
# print(mapper["mombai"])
