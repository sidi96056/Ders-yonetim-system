# Ders-yonetim-system

📚 Ders Yönetim System

A Django-based course management system that allows administrators, teachers, and students to manage lessons, schedules, and academic records efficiently.

---

 🚀 Features
- User authentication (Admin, Teacher, Student roles)
- Course creation and management
- Student enrollment and tracking
- Attendance and grading system
- Responsive UI with Bootstrap/Tailwind (if used)
- REST API endpoints for integration (optional)

---

 🛠️ Tech Stack
- Backend:Django (Python)
- Database:SQLite (default) or PostgreSQL/MySQL
- Frontend: HTML, CSS, Bootstrap/Tailwind
- Other: Django REST Framework (if API enabled)

---

📦 Installation

1.Clone the repository
   
   git clone https://github.com/sidi96056/Ders-yonetim-system.git
   cd Ders-yonetim-system
   

2. Create and activate virtual environment

   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows


3. Run migrations

   python manage.py makemigrations
   python manage.py migrate
  

5.Create superuser
   python manage.py createsuperuser

6.Start development server
   
   python manage.py runserver
  

📂 Project Structure

Ders-yonetim-system/
│── ders_yonetim/        # Main Django app
│── templates/           # HTML templates
│── static/              # CSS, JS, images
│── manage.py            # Django management script
└── README.md            # Project documentation


---


