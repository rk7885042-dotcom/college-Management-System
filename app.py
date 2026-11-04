
from flask import Flask, render_template, request
import sqlite3
from database import create_database

app = Flask(__name__)

create_database()


# Home Page
@app.route('/')
def home():
    return render_template('index.html')


# About Page
@app.route('/about')
def about():
    return render_template('about.html')


# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        return f"Welcome, {username}! Login form submitted!"

    return render_template('login.html')


# Student Registration
@app.route('/student', methods=['GET', 'POST'])
def student():
    if request.method == 'POST':
        name = request.form.get('name')
        rollno = request.form.get('rollno')
        course = request.form.get('course')
        semester = request.form.get('semester')
        email = request.form.get('email')

        conn = sqlite3.connect('college.db')
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO students
            (name, roll_no, rollno, course, semester, email)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, rollno, rollno, course, semester, email))

        conn.commit()
        conn.close()

        return "Student Registration Saved Successfully!"

    return render_template('student.html')


# Notices Page
@app.route('/notices')
def notices():
    return render_template('notices.html')


# Student Records
@app.route('/records')
def records():
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, roll_no, rollno, course, semester, email
        FROM students
    """)

    students = cursor.fetchall()
    conn.close()

    return render_template('records.html', students=students)


if __name__ == '__main__':
    app.run(debug=True)
