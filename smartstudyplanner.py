import csv
import matplotlib.pyplot as plt

file_name = "study_data.csv"

def add_record():
    date = input("Enter date (DD-MM-YYYY): ")
    subject = input("Enter subject: ")
    hours = float(input("Enter study hours: "))

    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, subject, hours])

    print("Record added successfully\n")


def view_records():
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            print("\nDate\t\tSubject\t\tHours")
            print("----------------------------------")
            for row in reader:
                print(row[0], "\t", row[1], "\t", row[2])
    except FileNotFoundError:
        print("No records found\n")


def total_hours():
    total = 0
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[2])
        print("Total Study Hours:", total)
    except FileNotFoundError:
        print("No records found")


def subject_analysis():
    subjects = {}

    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                subject = row[1]
                hours = float(row[2])

                if subject in subjects:
                    subjects[subject] += hours
                else:
                    subjects[subject] = hours

        print("\nSubject-wise Study Hours")
        print("------------------------")
        for sub, hrs in subjects.items():
            print(sub, ":", hrs, "hours")

    except FileNotFoundError:
        print("No data found")


def productivity_score():
    total = 0
    days = 0

    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[2])
                days += 1

        if days > 0:
            score = total / days
            print("Productivity Score (avg hours/day):", round(score, 2))
        else:
            print("No data available")

    except FileNotFoundError:
        print("No records found")


def show_graph():
    subjects = {}

    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                subject = row[1]
                hours = float(row[2])

                if subject in subjects:
                    subjects[subject] += hours
                else:
                    subjects[subject] = hours

        plt.bar(subjects.keys(), subjects.values())
        plt.xlabel("Subjects")
        plt.ylabel("Study Hours")
        plt.title("Study Hours Analysis")
        plt.show()

    except FileNotFoundError:
        print("No data available")


while True:

    print("\n===== Smart Study Planner =====")
    print("1. Add Study Record")
    print("2. View Records")
    print("3. Total Study Hours")
    print("4. Subject-wise Analysis")
    print("5. Productivity Score")
    print("6. Show Graph")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_record()

    elif choice == "2":
        view_records()

    elif choice == "3":
        total_hours()

    elif choice == "4":
        subject_analysis()

    elif choice == "5":
        productivity_score()

    elif choice == "6":
        show_graph()

    elif choice == "7":
        break

    else:
        print("Invalid choice")