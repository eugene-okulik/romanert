import mysql.connector as mysql
from homework.roman_b.Lesson_15 import mysql_creds

db = mysql.connect(
    user=mysql_creds.user,
    passwd=mysql_creds.passwd,
    host=mysql_creds.host,
    port=mysql_creds.port,
    database=mysql_creds.database
)

cursor = db.cursor()

insert_student = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
student_name = 'Jan'
student_second_name = 'Cousteau'
cursor.execute(insert_student, (student_name, student_second_name))
student_id = cursor.lastrowid

insert_book = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
book_1 = 'Indistractable'
book_2 = 'The Intelligent Investor'
book_3 = 'The Great Gatsby'
cursor.executemany(insert_book,
                   [(book_1, student_id), (book_2, student_id), (book_3, student_id)]
                   )

insert_group = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
group_title = 'The Champions'
start_date = 'july 2024'
end_date = 'sept 2024'
cursor.execute(insert_group, (group_title, start_date, end_date))
group_id = cursor.lastrowid

cursor.execute(f"UPDATE students SET group_id = {group_id} WHERE id = {student_id}")

insert_subject = "INSERT INTO subjets (title) VALUES (%s)"
subject_1 = 'The Science of Superheroes'
subject_2 = 'Zombies on TV'
cursor.execute(insert_subject, (subject_1, ))
subject_1_id = cursor.lastrowid
cursor.execute(insert_subject, (subject_2, ))
subject_2_id = cursor.lastrowid

insert_lesson = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
lesson_1 = 'Monday'
lesson_2 = 'Wednesday'
lesson_3 = 'Tuesday'
lesson_4 = 'Thursday'
cursor.execute(insert_lesson, (lesson_1, subject_1_id))
lesson_1_id = cursor.lastrowid
cursor.execute(insert_lesson, (lesson_2, subject_1_id))
lesson_2_id = cursor.lastrowid
cursor.execute(insert_lesson, (lesson_3, subject_2_id))
lesson_3_id = cursor.lastrowid
cursor.execute(insert_lesson, (lesson_4, subject_2_id))
lesson_4_id = cursor.lastrowid


insert_mark = "INSERT INTO marks (value, student_id, lesson_id) VALUES (%s, %s, %s)"
mark_1 = 'Great'
mark_2 = 'Good'
mark_3 = 'Excellent'
mark_4 = 'Great+'
cursor.execute(insert_mark, (mark_1, student_id, lesson_1_id))
mark_1_id = cursor.lastrowid
cursor.execute(insert_mark, (mark_2, student_id, lesson_2_id))
mark_2_id = cursor.lastrowid
cursor.execute(insert_mark, (mark_3, student_id, lesson_3_id))
mark_3_id = cursor.lastrowid
cursor.execute(insert_mark, (mark_4, student_id, lesson_4_id))
mark_4_id = cursor.lastrowid

query_marks = "SELECT value FROM marks WHERE student_id = %s"
cursor.execute(query_marks, (student_id, ))
print(cursor.fetchall())

query_books = "SELECT title FROM books WHERE taken_by_student_id = %s"
cursor.execute(query_books, (student_id, ))
print(cursor.fetchall())

query = '''
SELECT
g.title AS 'GROUP_NAME',
s.id as 'STUDENT_ID',
s.name as 'NAME',
s.second_name as 'SECOND_NAME',
b.title as 'BOOK_TITLE',
sub.title as 'SUBJECT_TITLE',
l.title as 'LESSON_TITLE',
m.value as 'MARKS'
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON s.id = m.student_id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjets sub ON sub.id = l.subject_id
WHERE s.id = %s
'''
cursor.execute(query, (student_id, ))
print(cursor.fetchall())

db.commit()
db.close()
