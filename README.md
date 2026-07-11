# 🤝 Personalized Networking Assistant

## 📌 Project Overview

The Personalized Networking Assistant is a web application developed using **FastAPI** and **Streamlit**. It helps users prepare for networking events by generating conversation starters based on event descriptions. The application also includes a Fact Checker, Conversation History, and Feedback System to improve user interaction and networking experience.

---

## 🎯 Objectives

- Help users start meaningful conversations at networking events.
- Generate conversation starters based on event descriptions.
- Provide quick facts about selected topics.
- Store conversation history.
- Collect user feedback for improving recommendations.

---

## ✨ Features

- ✅ Event Theme Analysis
- ✅ Conversation Starter Generation
- ✅ Fact Checker
- ✅ Conversation History
- ✅ Feedback Collection
- ✅ FastAPI Backend
- ✅ Streamlit Frontend
- ✅ API Testing using Pytest

---

## 🛠️ Technologies Used

- Python
- FastAPI
- Streamlit
- Requests
- Pytest
- Uvicorn
- Git
- GitHub

---

## 📂 Project Structure

```text
Personalized-Networking-Assistant/
│
├── backend/
│   ├── database.py
│   ├── event_analyzer.py
│   ├── fact_checker.py
│   ├── feedback_logger.py
│   ├── history_logger.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   └── topic_generator.py
│
├── frontend/
│   └── app.py
│
├── tests/
│   └── test_api.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/rajukataru/Personalized-Networking-Assistant.git
```

### 2. Install Required Packages

```bash
pip install -r requirements.txt
```

### 3. Run the FastAPI Backend

```bash
uvicorn backend.main:app --reload
```

The backend will run at:

```
http://127.0.0.1:8000
```

### 4. Run the Streamlit Frontend

```bash
streamlit run frontend/app.py
```

The frontend will open at:

```
http://localhost:8501
```

---

## 🚀 How to Use

1. Start the FastAPI backend.
2. Start the Streamlit frontend.
3. Enter an event description.
4. Click **Generate Conversation Starters**.
5. View generated themes and conversation starters.
6. Use the **Fact Checker** to verify topics.
7. Submit feedback.
8. View conversation history.
9. View feedback history.

---

## 🧪 Testing

Run the project tests using:

```bash
pytest
```

---

## 📸 Application Modules

### Event Analyzer
Extracts important themes from the event description.

### Topic Generator
Generates conversation starter questions.

### Fact Checker
Provides useful facts related to the selected topic.

### Conversation History
Displays previously generated conversations.

### Feedback System
Collects user feedback for generated conversation starters.

---

## 🔮 Future Enhancements

- User Login Authentication
- Database Storage using SQLite/MySQL
- AI Integration using OpenAI or Gemini API
- Cloud Deployment
- Improved User Interface

---

## 👨‍💻 Author

**Kataru Venkata Thirumala Raju**

GitHub Profile:
https://github.com/rajukataru

---

## 📄 License

This project is developed for educational and internship purposes only.

---

## 🙏 Acknowledgement

This project was developed as part of the **SmartBridge Internship Program** to enhance practical knowledge in Python, FastAPI, Streamlit, Git, GitHub, and API development.