from DATA.class_methods import Student


def search_tool(conn):
    students = {}


    cursor = conn.cursor()

    while True:

        user = input("Enter a student name or 'exit' to quit: ").strip()

        if user.lower() == "exit":
            print("Goodbye, return to the main menu!")
            break

        cursor.execute("""
            SELECT students.created_at,
                   students.name,
                   subjects.subject,
                   subjects.score
            FROM students
            JOIN subjects
                ON students.id = subjects.student_id
            WHERE students.name = ?
            ORDER BY students.created_at
        """, (user.capitalize(),))

        info = cursor.fetchall()

        if not info:
            print("Sorry, cannot find the student")
            continue

        for row in info:
            date = row["date"]
            name = row["name"]

            if date not in students:
                students[date] = {}

            if name not in students[date]:
                students[date][name] = {}

            subject = row["subject"]
            score = row["score"]

            students[date][name][subject] = score

        return students

