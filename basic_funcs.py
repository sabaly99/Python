def greetings():
    name = input("what is your name dear mortal: ")
    return f"Hello dear {name},Welcome to our new pyhton code"


def room_allocation():
    course = input("Input the course you offer mortal !: ")
    Age = input("Mortal , how many years have you been in this accursed world: ")
    qualification_point = float(input("Type here your Qualification Points: "))
    if course == "Engineering":
        print("YOU've been assigned to Katanga Hall ")
    elif course == "Social Science":
        print('''you've been assigned to Queen's Hall''')
    elif course == "Sciences":
        print("You've assigned to Independence Hall")
    else :
        print("You've been assigned to Continental Hall")

message = greetings()
print(message)

room = room_allocation()
print(room)


