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
            date = row["created_at"]
            name = row["name"]

            if date not in students:
                students[date] = {}

            if name not in students[date]:
                students[date][name] = {}

            subject = row["subject"]
            score = row["score"]

            students[date][name][subject] = score

        #for row in info:            just for learning transform the row into object directly
        #    name = row["name"]

        #    if name not in students:             we do this cause the info always return a name
        #        students[name] = Student(name)    cause if not it will run the loop again line = 32 for reference

        #   students[name].add_subject(row["subject"], row["score"])

        return students


def get_top_students(conn, limit=3):
    # table aliases:
    # s.name = students.name
    # sub.score = subjects.score
    # AVG(sub.score) calculates the student's average score, avg_score name of that colum

    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, AVG(sub.score) AS avg_score
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        GROUP BY s.id
        ORDER BY avg_score DESC
        LIMIT ?
    """, (limit,))

    return cursor.fetchall()
