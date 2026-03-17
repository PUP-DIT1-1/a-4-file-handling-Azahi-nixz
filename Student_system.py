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