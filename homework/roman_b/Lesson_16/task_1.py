import mysql.connector as mysql
import csv
import os
import dotenv


dotenv.load_dotenv(override=True)

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
lesson_path = os.path.join(homework_path, 'eugene_okulik')
file_path = os.path.join(lesson_path, 'Lesson_16', 'hw_data', 'data.csv')

query = '''
SELECT
s.name as 'NAME',
s.second_name as 'SECOND_NAME',
g.title AS 'GROUP_TITLE',
b.title as 'BOOK_TITLE',
sub.title as 'SUBJECT_TITLE',
l.title as 'LESSON_TITLE',
m.value as 'MARK_VALUE'
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON s.id = m.student_id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjets sub ON sub.id = l.subject_id
WHERE s.name = %s AND s.second_name = %s AND g.title = %s AND b.title = %s 
AND sub.title = %s AND l.title = %s AND  m.value = %s
'''

missing_students = []

with open(file_path, newline='') as csvfile:
    file_data = csv.DictReader(csvfile, delimiter=",")
    for row in file_data:
        data = [v for v in row.values()]
        cursor.execute(query, tuple(data))
        if not cursor.fetchall():
            missing_students.append(row)

print("Missing:", *missing_students, sep='\n' if missing_students else "No data missing")

db.close()
