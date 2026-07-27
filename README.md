# 🤖 AI Customer Support Assistant

An intelligent AI-powered Customer Support Assistant built using **Python**, **LangChain**, and **Google Gemini**. The assistant understands customer queries, classifies their intent, retrieves relevant information from a predefined knowledge base, and generates accurate, professional responses using a Large Language Model (LLM).

This project was developed as part of the **Week 2 AI Internship Assignment**, following a clean, modular software architecture and best development practices.

---

# 📌 Project Overview

Customer support is one of the most common applications of Artificial Intelligence. This project demonstrates how Large Language Models can be integrated with a structured knowledge base to automate customer interactions.

The assistant can:

* Understand natural language customer queries.
* Classify customer intent.
* Retrieve relevant information from a knowledge base.
* Generate professional responses using Google Gemini.
* Maintain a conversational interface until the user exits.
* Handle common runtime errors gracefully.
* Secure API keys using environment variables.

---

# ✨ Features

* 🤖 AI-powered customer support assistant
* 🧠 Intent classification
* 📚 JSON-based knowledge base
* 💬 Conversational terminal interface
* 🔗 LangChain integration
* ⚡ Google Gemini LLM
* 🔒 Secure API key management using `.env`
* 📦 Modular and maintainable project structure
* ❌ Error handling for invalid input, missing files, and API-related issues

---

# 🛠️ Technologies Used

| Category              | Technology    |
| --------------------- | ------------- |
| Language              | Python 3.x    |
| LLM                   | Google Gemini |
| Framework             | LangChain     |
| Environment Variables | python-dotenv |
| Console UI            | Rich          |
| Knowledge Base        | JSON          |
| Version Control       | Git & GitHub  |

---

# 📂 Project Structure

```text
AI-Customer-Support-Assistant/
│
├── knowledge/
│   └── customer_data.json
│
├── screenshots/
│
├── main.py
├── chat.py
├── llm.py
├── intent_classifier.py
├── knowledge_base.py
├── prompts.py
├── utils.py
│
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
└── .env
```

---

# ⚙️ How It Works

```
Customer Query
       │
       ▼
Intent Classification
       │
       ▼
Knowledge Base Retrieval
       │
       ▼
Prompt Construction
       │
       ▼
Google Gemini (LLM)
       │
       ▼
AI Response
```

---

# 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/nikhilkanbarkar/AI-Customer-Support-Assistant.git
```

---

### 2. Navigate to the project folder

```bash
cd AI-Customer-Support-Assistant
```

---

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Configure your API Key

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

### 6. Run the project

```bash
python main.py
```

---

# 💬 Sample Conversation

```text
🤖 AI Customer Support Assistant

You:
Where is my order?

Detected Intent:
Order Status

Assistant:
Orders are generally delivered within 3–5 business days.
You can track your order using your Order ID.
```

---


# 📖 Key Concepts Demonstrated

* Object-Oriented Programming (OOP)
* Modular Python Programming
* Prompt Engineering
* LangChain Integration
* Google Gemini API
* Environment Variable Management
* JSON Data Handling
* Exception Handling
* Terminal-Based User Interface

---

# 📈 Future Improvements

* Web interface using Streamlit or Flask
* Persistent conversation history
* Database integration for real order tracking
* Retrieval-Augmented Generation (RAG)
* Multi-language customer support
* Voice-based interaction
* Admin dashboard and analytics

---

# 🎯 Learning Outcomes

Through this project, I gained hands-on experience with:

* Building AI-powered applications
* Working with Large Language Models (LLMs)
* Integrating LangChain with Google Gemini
* Designing modular Python applications
* Managing API keys securely
* Creating structured prompt templates
* Developing knowledge-based AI assistants

---

# 👨‍💻 Author

**Nikhil Kanbarkar**

Electronics and Communication Engineering Student

Aspiring **Machine Learning Engineer | AI Engineer | Data Scientist**

---

# 📄 License

This project is created for educational and internship purposes.

---

# ⭐ Support

If you found this project useful or interesting, consider giving the repository a **Star ⭐** on GitHub.

---

## Thank You!

Thank you for visiting this project. Feedback and suggestions are always welcome as I continue learning and building AI-powered applications.
