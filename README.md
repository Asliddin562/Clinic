# 🏥 Clinic - Shifoxona Boshqaruv Loyihasi

Bu loyiha Django REST Framework asosida yaratilgan shifokor va klinika boshqaruvi tizimidir. Admin foydalanuvchilar klinika xodimlari, shifokorlar jadvali, bemorlar va uchrashuvlarni (appointments) boshqarishlari mumkin.

---

## 📌 Loyihaning imkoniyatlari

- 🩺 Shifokorlarni ro‘yxatdan o‘tkazish va profil yuritish
- 🗓️ Har bir shifokor uchun haftalik ish jadvali
- 🧑‍⚕️ Doktor bandligini kalendarda ko‘rsatish (bandlik foizi va ranglar)
- 👨‍💻 Admin CRUD (create, read, update, delete) imkoniyatlari
- 🔐 JWT orqali autentifikatsiya (login/ro'yxatdan o‘tish)
- 📱 Telefon raqam orqali OTP yuborish va tasdiqlash
- 📅 Appointment’larni yaratish va ko‘rish

---

## 🚀 Texnologiyalar

- Python 3.11+
- Django 4.x
- Django REST Framework
- djoser (JWT uchun)
- PostgreSQL (yoki SQLite test uchun)

---

## ⚙️ O‘rnatish

```bash
git clone https://github.com/USERNAME/Clinic.git
cd Clinic
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
