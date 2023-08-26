from sqlalchemy import create_engine, MetaData, Table, select
import sqlalchemy as db

engine = db.create_engine(
    "sqlite:///tasks.db"
)  # Указываем правильный URL для SQLite базы данных

connection = engine.connect()

metadata = db.MetaData()

students = db.Table(
    "students",
    metadata,
    db.Column("student_id", db.Integer, primary_key=True),
    db.Column("name", db.Text),
    db.Column("age", db.Integer),
)

subjects = db.Table(
    "subjects",
    metadata,
    db.Column("subject_id", db.Integer, primary_key=True),
    db.Column("subject_name", db.Text),
)

student_subject = db.Table(
    "student_subject",
    metadata,
    db.Column("student_subject_id", db.Integer, primary_key=True),
    db.Column("student_id", db.Integer, db.ForeignKey("students.student_id")),
    db.Column("subject_id", db.Text, db.ForeignKey("subjects.subject_id")),
)

metadata.create_all(engine)

insertion_query_students = students.insert().values(
    [
        {"name": "Bae", "age": 18},
        {"name": "Eddy", "age": 21},
        {"name": "Lily", "age": 22},
        {"name": "Jenny", "age": 19},
    ]
)

insertion_query_subjects = subjects.insert().values(
    [
        {"subject_name": "English"},
        {"subject_name": "Spain"},
        {"subject_name": "Chinese"},
        {"subject_name": "Math"},
    ]
)

insertion_query = student_subject.insert().values(
    [
        {"student_id": 1, "subject_id": 1},
        {"student_id": 1, "subject_id": 2},
        {"student_id": 2, "subject_id": 3},
        {"student_id": 3, "subject_id": 1},
        {"student_id": 4, "subject_id": 4},
    ]
)

query = (
    select(students.c.name)
    .select_from(student_subject.join(students).join(subjects))
    .where(subjects.c.subject_name == "English")
)

result = connection.execute(query)
english_students = result.fetchall()

for student in english_students:
    print(student.name)
