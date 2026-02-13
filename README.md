🧑‍💻 User Management System (CLI Version)

A simple Command Line Interface (CLI) based User Management System built with Python.
This project demonstrates backend development fundamentals including data modeling, business logic separation, and session simulation.

-------------------------------------

🚀 Features

User Registration

Duplicate Email Validation

User Login

Profile Viewing

Profile Update

Account Deletion

Auto-increment User ID system

Session simulation using current_user


-------------------------
🏗 Architecture Overview

This project follows basic backend design principles:

🔹 Data Layer

User Class

id (auto-increment integer)

username

email

password

🔹 Logic Layer

UserManager Class

register()

login()

view_profile()

update_profile()

delete_user()

🔹 Control Layer

Main menu loop handles user interaction and routes actions.

This structure mimics real backend systems where:

Models represent data

Managers handle business logic

Controllers manage flow


---------------------------

🚀 Planned Improvements

Password hashing (bcrypt)

JSON or database persistence

REST API conversion (FastAPI)

PostgreSQL integration

JWT authentication

Role-based authorization

Unit testing implementation