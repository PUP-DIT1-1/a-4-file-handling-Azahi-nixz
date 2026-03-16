import os

FILE_NAME = "students.txt"
subjects = ["math", "science", "pe", "history", "english"]


# -------- FILE HANDLING -------- #

def load_data():
    students = {}

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            for line in f:
                data = line.strip().split(",")

                name = data[0]
                grades = list(map(float, data[1:]))

                students[name] = dict(zip(subjects, grades))

    return students


def save_data(students):
    with open(FILE_NAME, "w") as f:
        for name, grades in students.items():

            line = name

            for subject in subjects:
                line += "," + str(grades[subject])

            f.write(line + "\n")
