
# grup adi : PyCorei5

# grup olnlar :

SIDAHMED MOUHAMED BEWBE

MUHAMMED ÇİLENK

BURHAN KARA

MUHAMMED ALİ KUMRU

TUĞÇE KOMESU

# Proje adi : # Ders-yonetim-system 

# proje amacı:

Bu platform, dersleri sadece rakamlarla değil, cümlelerle takip etmenizi sağlar. Öğretmen ve öğrencinin birlikte yazdığı dijital bir gelişim günlüğüdür.

Öğrenciler İçin: "Bugün ne öğrendim?" sorusunun cevabını kendi cümlelerinle kaydettiğin, gelişimini adım adım izlediğin bir alan.

Öğretmenler İçin: Her öğrencinin öğrenme yolculuğuna eşlik ettiğin, ders notlarının ötesinde gerçek gelişimi gördüğün bir rehber.

Notlar bir gün unutulur, ama tutulan bu günlükler kalıcı bir başarı arşivi oluşturur.

# grup üyesi hangi app den sorumlugu olanları:

SIDAHMED MOUHAMED BEWBE  accounts ve DersYonetimsystemi uygulamalar

MUHAMMED ÇİLENK management uygulaması 

BURHAN KARA anasayfa , iletişim , hakkımızda 

MUHAMMED ALİ KUMRU app uygulaması 

TUĞÇE KOMESU abonelik ve planları

# Ders-yonetim-system

  # Özellikler
- Kullanıcı kimlik doğrulaması (Yönetici, Öğretmen, Öğrenci rolleri)
- Kurs oluşturma ve yönetimi
- Öğrenci kaydı ve takibi
- Devam ve notlandırma sistemi
- Bootstrap/Tailwind ile duyarlı kullanıcı arayüzü
- Entegrasyon için REST API uç noktaları

 $ Tech Stack
 
- Backend:Django (Python)
- Database:SQLite (default)
- Frontend: HTML, CSS, Bootstrap/Tailwind

---

 # Kurulum

# 1. Depoyu klonlayın

git clone https://github.com/sidi96056/Ders-yonetim-system.git

cd Ders-yonetim-system

# 2. Sanal ortam oluşturun ve etkinleştirin

python -m venv venv
source venv/bin/activate # Linux/Mac'te
venv\Scripts\activate # Windows'ta

# 3. Migrasyonları çalıştırın

python manage.py makemigrations
python manage.py migrate

# 5. Süper kullanıcı oluşturun

python manage.py createssuperuser

# 6. Geliştirme sunucusunu başlatın

python manage.py runserver

#  Proje Yapısı

Ders-yonetim-system/
│── ders_yonetim/ # Ana Django uygulaması
│── templates/ # HTML şablonları
│── static/ # CSS, JS, resimler
│── manage.py # Django yönetim betiği
└── README.md # Proje dokümantasyonu

---
