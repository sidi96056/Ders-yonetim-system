
grup adi : PyCorei5
grup olnlar :
SIDAHMED MOUHAMED BEWBE
Proje adi : # Ders-yonetim-system

# Ders-yonetim-system

📚 Ders Yönetim System

Yöneticilerin, öğretmenlerin ve öğrencilerin dersleri, programları ve akademik kayıtları verimli bir şekilde yönetmelerini sağlayan Django tabanlı bir ders yönetim sistemi.

---

  Özellikler
- Kullanıcı kimlik doğrulaması (Yönetici, Öğretmen, Öğrenci rolleri)
- Kurs oluşturma ve yönetimi
- Öğrenci kaydı ve takibi
- Devam ve notlandırma sistemi
- Bootstrap/Tailwind ile duyarlı kullanıcı arayüzü
- Entegrasyon için REST API uç noktaları

 Tech Stack
- Backend:Django (Python)
- Database:SQLite (default) or PostgreSQL/MySQL
- Frontend: HTML, CSS, Bootstrap/Tailwind
- Other: Django REST Framework (if API enabled)

---

 Kurulum

1. Depoyu klonlayın

git clone https://github.com/sidi96056/Ders-yonetim-system.git

cd Ders-yonetim-system

2. Sanal ortam oluşturun ve etkinleştirin

python -m venv venv
source venv/bin/activate # Linux/Mac'te
venv\Scripts\activate # Windows'ta

3. Migrasyonları çalıştırın

python manage.py makemigrations
python manage.py migrate

5. Süper kullanıcı oluşturun

python manage.py createssuperuser

6. Geliştirme sunucusunu başlatın

python manage.py runserver

📂 Proje Yapısı

Ders-yonetim-system/
│── ders_yonetim/ # Ana Django uygulaması
│── templates/ # HTML şablonları
│── static/ # CSS, JS, resimler
│── manage.py # Django yönetim betiği
└── README.md # Proje dokümantasyonu

---
