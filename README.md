# Phone Register App
A phone register application built with **Django, Django REST Framework (DRF), PostgreSQL, Djoser, Authentication**, and managed with **Poetry**.
The app allows you to store and manage information about various phones, including details like brand, model, price, screen size, and more. Also have filtering logic for filter cell phones by brand, made-in and nationality.

## Features

- **CRUD APIs**: Create, Read, Update, Delete phone entries via RESTful APIs.
- **PostgreSQL Database**: A PostgreSQL database to store phone details.
- **Django Admin**: Manage the phones via the Django admin interface.

## Improvement needed
- Adding quantity of phones.
- Creating the date filed when phones are registered.
- Uploading image for phones.

## Installation

### - Clone the Repository
```bash
Copy code
git clone https://github.com/vahid-nasiri/DRF-Phones-Register.git
cd DRF-Phones-Register.git
```
### - Install Dependencies 
Use Dependency Management tools to install dependencies from `requirements.txt`

### - Create `.env` file and set up the attributes

### - Setting Up PostgreSQL Database
Make sure you have PostgreSQL installed and running. Create a database and user for the project:
```bash
psql -U postgres
CREATE USER 'your_db_user' WITH PASSWORD 'your_db_password';
CREATE DATABASE 'your_db_name' WITH OWNER 'your_db_user' ENCODING 'UTF8';
GRANT ALL PRIVILEGES ON DATABASE phone_storage_db TO your_db_user;
```

### - API Endpoints:
    GET /phones/: List and Create phones.
    GET /phones/{id}/: Retrieve a specific phone.
    PUT /phones/{id}/: Update a phone entry.
    DELETE /phones/{id}/: Delete a phone entry.

