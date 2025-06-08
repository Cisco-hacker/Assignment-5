dict = {"Alice": 25,
        "Bob": 25,
        "Charlie": 25,
        "David": 25,
        "Eve": 25, }

try:
    name = input("Enter the student's name: ").strip().capitalize()
    print(name)
    print(name, "'s marks: ", dict[name], sep ='')

except KeyError:
    print("Student not found")