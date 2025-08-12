# HandyHub - Backend API ⚙️🐍

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)  
![Django](https://img.shields.io/badge/Django-4.x-green?logo=django&logoColor=white)  
![DRF](https://img.shields.io/badge/Django%20REST%20Framework-3.x-red?logo=django&logoColor=white)  
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey?logo=sqlite&logoColor=white)  

---

## 📌Project Overview  
This repository contains the backend API for **HandyHub**, my capstone project that connects users with verified local artisans and home service providers.  
The backend is built with Django and Django REST Framework to provide a robust, scalable, and secure API for the frontend application.  

The backend handles **data management, authentication, and API endpoints** that power the HandyHub platform.  

---

## Features Completed 🔥  
The following backend features have been implemented so far:  

- **Project Setup**: Fully configured Django project with virtual environment and dependencies.  
- **Admin Panel Setup**: Enabled Django Admin for easy database management.  
- **Service Categories**: Added initial service category entries for classification of services.  
- **Locations**: Added multiple locations (cities) to the database for service area mapping.  

---

## Tech Stack 👩‍💻 

- 🐍 **Python** — Main programming language.  
- 🌐 **Django** — Python web framework.  
- 🔗 **Django REST Framework (DRF)** — For building RESTful APIs.  
- 🗄️ **SQLite** — Default database (to be upgraded in production).  

---

## Screenshots 🖼️ 
<img src="https://github.com/gemgeek/gems-digital-journal/blob/main/assets/Django%20Admin%20Panel.jpeg" alt="DAP" width="400">

---

## Future Plans 🔮 
- **API Endpoints**: Build endpoints for services, locations, and user management.  
- **Authentication**: Implement JWT-based authentication for secure login and signup.  
- **Frontend Integration**: Connect API to the HandyHub frontend to handle real user data.  
- **Database Upgrade**: Move from SQLite to PostgreSQL in production.  
- **Testing**: Add automated unit and integration tests for API reliability.  

---

## Getting Started 🔰 

To run the HandyHub backend locally:  

**1. Clone the repository:**  
```bash  
git clone https://github.com/your-username/HandyHub-backend.git  
cd HandyHub-backend  
```  

**2. Create and activate a virtual environment:**  
```bash  
python -m venv venv  
source venv/bin/activate  # Mac/Linux  
venv\Scripts\activate     # Windows  
```  

**3. Install dependencies:**  
```bash  
pip install -r requirements.txt  
```  

**4. Apply migrations:**  
```bash  
python manage.py migrate  
```  

**5. Create a superuser:**  
```bash  
python manage.py createsuperuser  
```  

**6. Run the development server:**  
```bash  
python manage.py runserver  
```  

The backend API will be available at:  
[http://localhost:8000](http://localhost:8000)  

---  
