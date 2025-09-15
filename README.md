---

# CodeApti – Quiz Application 

A quiz web application built using **Django**, **HTML**, and **Tailwind CSS**.
Users can select a domain, take quizzes, and view their results with detailed feedback.

---

##  Features

*  Choose from multiple domains (Web Development, Programming, DevOps, Databases).
*  Attempt domain-based quizzes with multiple-choice questions.
*  Get detailed results with correct and wrong answers highlighted.
*  Clean UI built with **Tailwind CSS** for responsiveness.
*  Secure navigation – domain quizzes are only accessible through the home page.

---

## Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, Tailwind CSS
* **Database:** SQLite (default Django DB, can be swapped)

---

##  Screenshots

###  Home Page

Users can choose a domain to start their quiz.
<img width="2560" height="1440" alt="image" src="https://github.com/user-attachments/assets/0def2c78-966a-4c27-9893-71cf9a5098ce" />

---

###  Quiz Page 

Displays domain-based multiple-choice questions.
<img width="2560" height="1440" alt="image" src="https://github.com/user-attachments/assets/5d2a8528-aeeb-4817-b3d3-9b5f7e58c544" />
<img width="2560" height="1440" alt="image" src="https://github.com/user-attachments/assets/11495f41-c720-4fb4-9bc4-d9a8997aaf1b" />

---

###  Results Page 

Shows score, correct answers, and user responses.
<img width="2560" height="1440" alt="image" src="https://github.com/user-attachments/assets/cc92b58d-ec11-498b-826a-e05b0fcdc576" />
<img width="2560" height="1440" alt="image" src="https://github.com/user-attachments/assets/beb28911-697f-42de-9f3b-9765eb1e7008" />

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

##  Project Structure

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

## Future Improvements

* Add authentication (login/signup).
* Track user quiz history.
* Add timer-based quizzes.
* Improve UI with animations.

