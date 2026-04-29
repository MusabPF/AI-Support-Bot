# 🤖 AI Customer Support Bot

A simple AI-powered customer support chatbot built with **FastAPI (backend)** and **HTML/JavaScript (frontend)**.  
It answers FAQs using similarity matching and also handles basic small talk like greetings and thank-yous.

---

## 🚀 Features

- 💬 FAQ-based question answering
- 🧠 Smart similarity matching (no ML model required)
- 👋 Small talk handling (hi, bye, thanks)
- ⚡ FastAPI backend API
- 🌐 Simple web frontend (HTML + JS)
- 🔁 CORS enabled for frontend-backend communication

---

## 📁 Project Structure

project/
│
├── data/
│ └── faqs.json # FAQ dataset
│
├── main.py # FastAPI backend
├── index.html # Frontend UI
└── README.md

## 📸 Screenshot

![Chatbot UI](assetschatbot(1).png)
![Chatbot UI](assetschatbot(2).png)

---

## 📦 Installation

#Clone the project
```bash
git clone https://github.com/your-username/ai-support-bot.git
cd ai-support-bot

#Install dependencies
pip install fastapi uvicorn

#Run the Backend
uvicorn main:app --reload --port 8001

#Backend runs at:
http://127.0.0.1:8001

#Run Frontend
Open:
index.html

#API Endpoint
#POST /ask

Request:
{
  "query": "How can I reset my password?"
}

Response:
{
  "answer": "You can reset your password by clicking on 'Forgot Password' on the login page.",
  "type": "faq",
  "confidence": 0.86
}


## 👨‍💻 Author
This project was built as a learning project using FastAPI and vanilla JavaScript.

Feel free to contribute or improve it.