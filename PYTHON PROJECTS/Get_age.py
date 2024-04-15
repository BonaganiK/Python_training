
def get_age(person):
    # If person is not provided, return 0
    if person is None:
        return 0
    
    # If person does not have an 'age' key in the dictionary, return -1
    if 'age' not in person:
        return -1
    
    # If person has an 'age' key in the dictionary, return the person's age
    return person['age']

# Example usage:
person_without_age = {"name": "Kiran","age": 18 }
print(get_age(person_without_age))  






    