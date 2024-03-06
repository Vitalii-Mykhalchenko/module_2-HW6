from faker import Faker
import sqlite3
import random


class My_db:
    def __init__(self) -> None:
        self.db = sqlite3.connect('database.db')

    def created_table(self):

        sql_create_students = """
    CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    group_id INT,
    FOREIGN KEY (group_id) REFERENCES groups(group_id)
);
"""
        sql_create_groups = """
    CREATE TABLE IF NOT EXISTS groups (
    group_id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name VARCHAR(50)
);
"""
        sql_create_teacher = """
        CREATE TABLE IF NOT EXISTS teachers (
    teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);
"""
        sql_create_subject = """
    CREATE TABLE IF NOT EXISTS subjects (
    subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name VARCHAR(100)
);
"""
        sql_create_teacher_subject = """
    CREATE TABLE IF NOT EXISTS subjects_teachers
    (subject_id INTEGER, teacher_id INTEGER,
    FOREIGN KEY(subject_id) REFERENCES subjects(subject_id),
    FOREIGN KEY(teacher_id) REFERENCES teachers(teacher_id),
    PRIMARY KEY(subject_id, teacher_id));
"""

        sql_create_grade = """
    CREATE TABLE IF NOT EXISTS grades (
    grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INT,
    subject_id INT,
    grade FLOAT,
    grade_date INTEGER TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);

"""
        try:
            cursor = self.db.cursor()
            cursor.execute(sql_create_students)
            cursor.execute(sql_create_groups)
            cursor.execute(sql_create_teacher)
            cursor.execute(sql_create_subject)
            cursor.execute(sql_create_teacher_subject)
            cursor.execute(sql_create_grade)

            self.db.commit()
        except sqlite3.Error as e:
            print(e)

    def look(self):
        cursor = self.db.cursor()

        # Виконуємо запит для вилучення даних із таблиці Students
        cursor.execute("SELECT * FROM Students;")
        students = cursor.fetchall()

        # Виводимо дані студентів
        for student in students:
            print(student)

        # Закриваємо з'єднання з базою даних
        # self.db.close()

    def fill(self):
        fake = Faker('uk_UA')
        # for table groups
        for _ in range(3):  # Цикл для створення трьох груп
            group_name = fake.company()  # Генеруємо випадкове ім'я групи
            cursor = self.db.cursor()
            cursor.execute(
                "INSERT INTO groups (group_name) VALUES (?)", (group_name,))
            self.db.commit()

        # for tabke students
        cursor.execute("SELECT group_id FROM groups")
        group_ids = [row[0] for row in cursor.fetchall()]
        for _ in range(50):
            group_id = random.choice(group_ids)
            # Генеруємо випадкові дані для кожного студента
            first_name = fake.first_name()
            last_name = fake.last_name()
            # Вставляємо згенеровані дані до бази даних
            cursor = self.db.cursor()
            cursor.execute(
                "INSERT INTO Students (first_name, last_name, group_id) VALUES (?,?,?)", (first_name, last_name, group_id))
            self.db.commit()

        # for teacher
        for _ in range(5):
            first_name = fake.first_name()
            last_name = fake.last_name()

            cursor = self.db.cursor()
            cursor.execute(
                "INSERT INTO teachers (first_name, last_name) VALUES (?, ?)",
                (first_name, last_name)
            )
            self.db.commit()

        # for subjects

        for subj in ["Математичний аналіз", "Фізика", "English",
                     "Програмування", "Інженерна графіка", "Електротехніка", "Механіка", "Електротехніка"]:
            cursor = self.db.cursor()
            cursor.execute(
                "INSERT INTO subjects (subject_name) VALUES (?)",
                (subj,)
            )
            self.db.commit()

        # # for subject_teacher
        cursor.execute("SELECT subject_id FROM subjects")
        subject_ids = [row[0] for row in cursor.fetchall()]

        cursor.execute("SELECT teacher_id FROM teachers")
        teacher_ids = [row[0] for row in cursor.fetchall()]

        for teacher_id in teacher_ids:
            # Випадково обираємо кілька предметів, які викладає кожен вчитель
            subjects_taught = random.sample(
                subject_ids, random.randint(1, len(subject_ids)))

            # Вставляємо записи про предмети, які викладає кожен вчитель
            for subject_id in subjects_taught:
                cursor = self.db.cursor()
                cursor.execute(
                    "INSERT INTO subjects_teachers (teacher_id, subject_id) VALUES (?, ?)",
                    (teacher_id, subject_id)
                )
                self.db.commit()

            # створюємо оцінки для учнів
            cursor.execute("SELECT student_id FROM students")
            student_ids = [row[0] for row in cursor.fetchall()]

            cursor.execute("SELECT subject_id FROM subjects")
            subject_ids = [row[0] for row in cursor.fetchall()]

            for student_id in student_ids:
                for subject_id in subject_ids:
                    grade = random.randint(1, 12)
                    cursor.execute("INSERT INTO grades (grade, student_id, subject_id) VALUES (?, ?, ?)",
                                   (grade, student_id, subject_id))
                    self.db.commit()


class DatabaseQuery:
    def __init__(self, file_number):
        self.file_number = file_number
        self.file_name = f'query/query_{self.file_number}.sql'
        self.connection = sqlite3.connect('database.db')

    def execute_query(self):
        with open(self.file_name, 'r') as f:
            sql = f.read()

        with self.connection:
            cur = self.connection.cursor()
            cur.executescript(sql)
            cur.execute(sql)
            result = cur.fetchall()
            for row in result:
                print(row)


# a = My_db()
# a.created_table()
# a.fill()
# # a.look()

db_query = DatabaseQuery(11)
db_query.execute_query()
