print("Welcome to StudySync")

assignments = []

while True:
    print("\n1. Add Assignment")
    print("2. View Assignments")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter assignment: ")
        assignments.append(task)
        print("Added!")

    elif choice == "2":
        print("Assignments:")
        for item in assignments:
            print("-", item)

    elif choice == "3":
        print("Goodbye")
        break

    else:
        print("Invalid choice")
