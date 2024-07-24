# Expense-Tracker-Backend
Description
A personal expense tracker built with Django and React. It includes user authentication, expense management.
Setup Instructions
Backend (Django)
1.	Create a virtual environment and activate it:
2.	  python -m venv venv
  source venv/bin/activate
3.	Initialize the django project:
4.	 django-admin startproject expense_tracker
 cd expense_tracker
5.	Create the django apps
6.	 python manage.py startapp users
7.	 python manage.py startapp expenses
8.	 python manage.py startapp contact form
 python manage.py startapp utils
9.	Install dependencies ```bash pip install  django-cors-headers
10.	Make migration and create superuser
  python manage.py migrate
  python manage.py createsuperuser

