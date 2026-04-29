import os
def save_to_file(assignments):
    file = open("assignments.txt", "w")

    for item in assignments:
        file.write(item + "\n")

    file.close()
    def load_from_file():
    assignments = []

    if os.path.exists("assignments.txt"):
        file = open("assignments.txt", "r")

        for line in file:
            assignments.append(line.strip())

        file.close()

    return assignments
print("Welcome to StudySync")

assignments = load_from_file()

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
    save_to_file(assignments)
    print("Saved. Goodbye")
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
elif choice == "2":
    print("Assignments:")

    for i, item in enumerate(assignments, start=1):
        print(i, "-", item)
