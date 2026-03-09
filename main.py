from DATA.class_methods import Student
from DATA.user_input import get_student
from DATA.SQL_FILE import creation_connection, creation_tables, insert_data

from LOGIC.calculations import (
    class_averages,
    pass_fail_students,
    below_above_class_average,
    top_low_students,
    subjects_per_student,
    valid_invalid_subjects
)

from LOGIC.tools import search_tool, get_top_students


def run_analysis(students):

    print("\n===== CLASS ANALYSIS =====")

    averages = Student.students_averages(students)

    if averages:
        print("average per student :")
        for name,average in averages.items():
            print(f"{name} average {average}")

    result = class_averages(students)
    if result:
        avg, number = result
        print(f"\nClass average: {avg}")
        print(f"Number of students: {number}")

    fail, success, n_fail, n_success = pass_fail_students(students)

    print("\n--- Pass / Fail ---")
    print("Failed:", fail)
    print("Success:", success)
    print(f"Number failed: {n_fail}")
    print(f"Number success: {n_success}")

    below, above, n_below, n_above = below_above_class_average(students)

    print("\n--- Below / Above Class Average ---")
    print("Below:", below)
    print("Above:", above)
    print(f"Below count: {n_below}")
    print(f"Above count: {n_above}")

    top, low, top_score, low_score = top_low_students(students)

    if top:
        print("\n--- Top / Lowest Student ---")
        print(f"Top student: {top} ({top_score})")
        print(f"Lowest student: {low} ({low_score})")

    print("\n--- Subjects per Student ---")
    counts = subjects_per_student(students)
    for name, count in counts.items():
        print(f"{name}: {count}")

    valid, invalid = valid_invalid_subjects(students)

    print("\n--- Valid Subjects ---")
    print(valid)

    print("\n--- Invalid Subjects ---")
    print(invalid)


def main():

    conn = creation_connection()
    creation_tables(conn)

    while True:

        print("\n===== STUDENT SYSTEM =====")
        print("1. Add students and analyze")
        print("2. Search student")
        print("3. Top 3 students")
        print("0. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":

            students = get_student()

            if not students:
                print("No students entered.")
                continue

            run_analysis(students)

            save = input("\nSave students to database? (y/n): ").lower()

            if save == "y":
                insert_data(conn, students)
                print("Students saved to database.")

        elif choice == "2":

            result = search_tool(conn)

            if result:
                print("\nStudent found:")
                print(result)

        elif choice == "3":

            results = get_top_students(conn)

            if not results:
                print("No students in database.")
                continue

            print("\nTop Students:")
            for row in results:
                print(f"{row['name']} - {round(row['avg_score'],2)}")

        elif choice == "0":

            print("Goodbye!")
            conn.close()
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()