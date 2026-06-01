# AI-Powered Chatbot

An intelligent chatbot application built using Flask, NLP techniques, and SQLite.
The project is designed to simulate customer support and FAQ assistance with contextual responses and interaction logging.

---

## Overview

This chatbot processes user queries, performs basic Natural Language Processing, and returns relevant responses dynamically.

The system also stores conversation history in a SQLite database for analysis and tracking.

---

## Features

* Interactive chatbot interface
* NLP preprocessing using NLTK
* Context-aware response handling
* Chat history logging
* SQLite database integration
* REST API communication
* Dynamic frontend interaction using JavaScript
* Lightweight Flask backend

---

## Technology Stack

### Backend

* Python
* Flask

### NLP

* NLTK

### Database

* SQLite3

### Frontend

* HTML
* CSS
* JavaScript

---

## Project Structure

```text
chatbot/
│
├── app.py
├── chatbot.db
├── requirements.txt
├── templates/
├── static/
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <repository-link>
```

### Navigate to Project

```bash
cd chatbot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Required Libraries

```bash
pip install flask nltk
```

---

## Run Application

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

## Database

The chatbot uses SQLite for storing user conversations.

Database file:

```text
chatbot.db
```

Stored information:

* User messages
* Bot responses
* Timestamps

---

## NLP Processing

The chatbot performs:

* Tokenization
* Stopword removal
* Basic intent matching

NLTK resources used:

* punkt
* punkt_tab
* stopwords

---

## Future Enhancements

* Transformer-based responses
* Voice assistant integration
* User authentication
* Multi-language support
* Sentiment analysis
* AI memory/context handling
* Deployment on cloud platforms

---

## Learning Outcomes

This project demonstrates:

* Backend development with Flask
* NLP preprocessing
* Database integration
* API handling
* Chatbot architecture
* Full-stack AI application workflow

---

## Author

Developed as a Python and NLP-based internship project.
