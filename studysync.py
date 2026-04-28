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
if choice == "1":
    task = input("Enter assignment: ").strip()

    if task == "":
        print("Cannot add empty assignment")
    else:
        assignments.append(task)
        print("Added!")
if choice == "1":
    task = input("Enter assignment: ").strip()

    if task == "":
        print("Cannot add empty assignment")

    elif task in assignments:
        print("Assignment already exists")

    else:
        assignments.append(task)
        print("Added!")
