# dictionary examples 

# my_dict = {"name": "Kiran", "age":30, "city": "Cape town "}
# print(my_dict["name"])



my_dict ={}
my_dict["name"] = "kiran"

print(my_dict)


def updateDictionary(value, prop):
    my_dict[prop] = value


updateDictionary("Wayne", "name")
updateDictionary(25, "age")
updateDictionary("Jozi", "city")
updateDictionary("some value", "anything")

print(my_dict)