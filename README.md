Perfect 👍 You’ve given me the **3 screenshots** (Home → Quiz → Result). I’ll create a **README.md** file for your Django + HTML + Tailwind CSS project that explains setup, usage, and includes those images for documentation.

Here’s the README:

---

# CodeApti – Quiz Application 🎯

A quiz web application built using **Django**, **HTML**, and **Tailwind CSS**.
Users can select a domain, take quizzes, and view their results with detailed feedback.

---

## 🚀 Features

* ✅ Choose from multiple domains (Web Development, Programming, DevOps, Databases).
* ✅ Attempt domain-based quizzes with multiple-choice questions.
* ✅ Get detailed results with correct and wrong answers highlighted.
* ✅ Clean UI built with **Tailwind CSS** for responsiveness.
* ✅ Secure navigation – domain quizzes are only accessible through the home page.

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, Tailwind CSS
* **Database:** SQLite (default Django DB, can be swapped)

---

## 📸 Screenshots

### 🏠 Home Page – Domain Selection

Users can choose a domain to start their quiz.
<img width="2560" height="1440" alt="image" src="https://github.com/user-attachments/assets/322a7f51-9e7a-492b-aa97-013bfcbdb5aa" />

---

### 📝 Quiz Page – Attempt Questions

Displays domain-based multiple-choice questions.
<img width="2560" height="1440" alt="image" src="https://github.com/user-attachments/assets/e94993f8-7a92-4e2a-8452-b4263f7a9b1b" />

---

### 📊 Results Page – Detailed Feedback

Shows score, correct answers, and user responses.
<img width="2560" height="1440" alt="image" src="https://github.com/user-attachments/assets/c7a904c6-e98e-455a-9c08-a1a35191ae1f" />

---

## ⚙️ Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/codeapti.git
   cd codeapti
   ```

2. **Create virtual environment & install dependencies**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows

   pip install -r requirements.txt
   ```

3. **Run database migrations**

   ```bash
   python manage.py migrate
   ```

4. **Start development server**

   ```bash
   python manage.py runserver
   ```

5. **Visit the app in browser**

   ```
   http://127.0.0.1:8000/
   ```

---

## 📂 Project Structure

```
codeapti/
│── quiz/               # Main app
│   ├── templates/      # HTML Templates
│   ├── static/         # Tailwind CSS, JS
│   ├── views.py        # App logic
│   ├── models.py       # Quiz & Question models
│── codeapti/           # Django project config
│── manage.py
│── requirements.txt
│── README.md
```

---

## 🎯 Future Improvements

* Add authentication (login/signup).
* Track user quiz history.
* Add timer-based quizzes.
* Improve UI with animations.

