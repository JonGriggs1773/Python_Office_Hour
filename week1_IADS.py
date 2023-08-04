

#! Primitive Data Types or our building blocks

#String 
#? Represented by the use of quotation marks
str_example = "This is a 'string' !@#$$%^&&*()"

#Boolean
#? Either True or False
#? Like a lightswitch
bool_example = True
bool_example = False

#Whole Numbers
#? It is a number
# Correct
num_example = 1
num_example = 10
num_example = 15
num_example = 20

# Incorrect
num_example = "20"














#! Complex Data Types == Data Structures
#? Basic List
names = ["John", "Jacob", "Jingle", "Heimer", "Smith", 12, 14, True, False]



count = 0

#todo Build a "for in" loop
def to_iterate(num):
    for anything in names:
        num += 1
        print("Each Item: ", anything, num)

# to_iterate(count)
# print(count)





#todo Build an "in range" for loop
# for i in range(0, len(names)):
#     if i % 2 == 0:
#         print(i)
#         print(names[i])
























#? Tuple
#! Immutable or "Read Only"
same_names = ("John", "Jacob", "Jingle", "Heimer", "Smith", 12, 14, True, False)




# for i in range(0, len(same_names)):
#     print(i)
#     print(same_names[i])


























#? Dictionary
jon = {
    "first_name": "Jon",
    "last_name": "Griggs",
    "social_security_number": 123456789,
    "password": "This_Is_Not_My_Password_123",
    "is_cool": True
}


# for key in jon.keys():
#     print(key)



























#? List of Dictionaries
users = [
    {
        "first_name": "Jon",
        "last_name": "Griggs",
        "social_security_number": 123456789,
        "password": "This_Is_Not_My_Password_123",
        "is_cool": True
    },
    {
        "first_name": "Paul",
        "name": "Jonathen",
        "last_name": "Soteropulos",
        "social_security_number": 2345678910,
        "password": "password456",
        "is_cool": False
    },
    jon
]


# for dictionary in users:
#     print(dictionary)


# print(users[0]['social_security_number'])

# for key, val in users[0].items():
#     print(key, val)

























#? Now we are getting complicated, sorry
fruit_by_category = [
    {
        "berries": ["blueberries", "rasberries", "blackberries", "strawberry", "pumpkin?"],
        "gourds": ["squash", "pumpkin_for_sure?!", "bottle_gourd"]
    },
    "ApParently everything is everything else. Melons are gourds, tomatos are fruits, and pumpkins are berries",
    ["This", "is", "our", "meta", "list"]
]


# print(fruit_by_category[1])
# print(fruit_by_category[1][2])

empty_string = ""
for word in fruit_by_category[2]:
    empty_string = empty_string + f" This is my string {word}"
print(empty_string)








