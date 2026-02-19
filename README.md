Django Todo Application

A simple and secure Todo application built using Django that allows users to register, log in, and manage their daily tasks efficiently.

Features

User Registration & Login
Secure Authentication System
Create Tasks
View Task List
Update Tasks
Delete Tasks
User-specific Todos (each user sees only their tasks)
Logout functionality

Technologies Used

Python

Django

SQLite (default database)

HTML & CSS

Bootstrap 

Project Structure
todo_project/
│
├── todo_project/
│   ├── settings.py
│   ├── urls.py
│
├── todo/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│── templates/
│
├── db.sqlite3
├── manage.py
└── README.md

Installation & Setup

1.Clone the repository
git clone https://github.com/yourusername/todo-app.git
cd todo-app

2.Create virtual environment
python -m venv venv


Activate it:
Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

3.Install dependencies
pip install django

4.Apply migrations

python manage.py makemigrations
python manage.py migrate

5.Create superuser 
python manage.py createsuperuser

6.Run the server
python manage.py runserver