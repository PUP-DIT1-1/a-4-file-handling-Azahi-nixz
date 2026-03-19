import os

FILE_NAME = "students.txt"
SUBJECTS = ["math", "science", "pe", "history", "english"]
MAX_STUDENTS = 10


# -------- FILE HANDLING -------- #

def load_data():
    students = {}

    if not os.path.exists(FILE_NAME):
        return students

    with open(FILE_NAME, "r") as f:
        for line in f:
            data = line.strip().split(",")

            if len(data) != 6:
                continue

            name = data[0].lower()

            try:
                grades = list(map(float, data[1:]))
            except ValueError:
                continue

            students[name] = dict(zip(SUBJECTS, grades))

    return students


def save_data(students):
    with open(FILE_NAME, "w") as f:
        for name, grades in students.items():

            line = name

            for subject in SUBJECTS:
                line += "," + str(grades.get(subject, 0))

            f.write(line + "\n")


# -------- INPUT VALIDATION -------- #

def get_grade(subject):

    while True:
        try:
            grade = float(input(f"Enter grade for {subject}: "))

            if 0 <= grade <= 100:
                return grade

            print("Grade must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Enter a number.")


def get_name(prompt):

    name = input(prompt).strip().lower()

    if not name:
        print("Name cannot be empty.")
        return None

    return name


# -------- FUNCTIONS -------- #

def add_student(students):

    if len(students) >= MAX_STUDENTS:
        print("Maximum student limit reached.")
        return

    name = get_name("Enter student name: ")

    if not name:
        return

    if name in students:
        print("Student already exists.")
        return

    grades = {}

    for subject in SUBJECTS:
        grades[subject] = get_grade(subject)

    students[name] = grades
    save_data(students)

    print("Student added successfully.")


def remove_student(students):

    name = get_name("Enter student name to remove: ")

    if not name:
        return

    if name not in students:
        print("Student not found.")
        return

    del students[name]
    save_data(students)

    print("Student removed.")


def edit_grades(students):

    name = get_name("Enter student name: ")

    if not name:
        return

    if name not in students:
        print("Student not found.")
        return

    for subject in SUBJECTS:
        students[name][subject] = get_grade(subject)

    save_data(students)

    print("Grades updated.")


def view_rankings(students):

    if not students:
        print("No students available.")
        return

    ranking = []

    for name, grades in students.items():
        avg = sum(grades.values()) / len(SUBJECTS)
        ranking.append((name, avg))

    ranking.sort(key=lambda x: x[1], reverse=True)

    print("\n--- STUDENT RANKINGS ---")

    for i, (name, avg) in enumerate(ranking, 1):
        print(f"{i}. {name.title()} - Average: {avg:.2f}")


def search_student(students):

    name = get_name("Enter student name: ")

    if not name:
        return

    if name not in students:
        print("Student not found.")
        return

    print("\nStudent:", name.title())

    for subject in SUBJECTS:
        print(f"{subject.title()}: {students[name][subject]}")

    avg = sum(students[name].values()) / len(SUBJECTS)

    print("Average:", round(avg, 2))


# -------- MENU -------- #

def menu():

    print("""
1. Add Student
2. Remove Student
3. Edit Grades
4. View Rankings
5. Search Student
6. Exit
""")

    return input("Select option: ").strip()


# -------- MAIN -------- #

def main():

    students = load_data()

    while True:

        choice = menu()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            remove_student(students)

        elif choice == "3":
            edit_grades(students)

        elif choice == "4":
            view_rankings(students)

        elif choice == "5":
            search_student(students)

        elif choice == "6":
            print("Program closed.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
