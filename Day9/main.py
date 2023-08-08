#  Dictionaries

# pd = {
#        "bug": "Hello bug",
#        "function": "hello function",
#     }

# print(pd)

# print(pd["bug"])

# pd["loop"] = "hello loop"

# print(pd)

# for key in pd:
#     print(key)
#     print(pd[key])


    #  Student Grades

# student_scores = {
#         "Mouli": 78,
#         "Dinesh": 56,
#         "Sandeep": 67,
#         "Hardik": 98,
#         "King": 87
#     }

# student_grades = {}

# for key in student_scores:
#     if student_scores[key] > 90:
#         student_grades[key] = "Outstanding"   
#     elif student_scores[key] > 80:
#         student_grades[key] = "Exceeds Expectations"   
#     elif student_scores[key] > 70:
#         student_grades[key] = "Acceptable"   
#     else:
#         student_grades[key] = "Fail"  


# print(student_grades)      


#  Nesting

# x = {
#     'math': {'a' : [123]},
#     "mouli": {"b": [12,12,34,5,6,78]}
# }

# y = [
#     {
#         'name':'moul',
#         'age':  22,
#         'gender':'male'
#     },
#     {
#         'name': 'Vishnu',
#         'age':  22,
#         'gender':'male'
#     }
# ]
# print(x)
# print(y)


#  Travel Vlog

travel_vlog = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["paris", "lillie", "Djon"] 
    },
    {
        "country": "India",
        "visits": 16,
        "cities": ["Vizag", "Delhi", "Bangalore"] 
    }
]


def add_city(cont,vist,city):
    new_item ={}
    new_item["country"] = cont
    new_item["visits"] = vist
    new_item["cities"] = city
    travel_vlog.append(new_item)
    print(travel_vlog)

add_city("Japan",14,["Mouli", "Dinesh"])    


