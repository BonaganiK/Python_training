# variable=value
# a=10
# print(a)

# a = 9
# b = 1.25
# c = "Kiran bonagani"
# d = 'Kumar'
# e = True

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)


# a,b,c=1,2,3
# print(a,b,c)

# my_first_name = "Kiran"
# my_last_name = "Bonagani"

# print(my_first_name,my_last_name)

# # Printing text and veriables in print by separting with comma
# a = 10
# print("The value stored in the variable a is: ",a)


# c=1,2,3
# print(c)

# c=v=x=22
# print(c,v,x)


# def greet(name):
#     print("Hello, " + name + "!")
# greet("Alice") 



# def add(a, b):
#     return a + b

# result = add(3, 5)
# print(result) 




class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)

    def display_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

if __name__ == "__main__":
    todo_list = TodoList()

    while True:
        print("\n=== To-Do List ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)
            print("Task added successfully!")
        elif choice == "2":
            print("\n=== Tasks ===")
            todo_list.display_tasks()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
