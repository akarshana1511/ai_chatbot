from flask import Flask, request, jsonify, render_template_string
import sqlite3
from datetime import datetime
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download once
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

app = Flask(__name__)

# ======================================
# DATABASE INITIALIZATION
# ======================================

def init_db():

    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chat_logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_message TEXT,
        bot_response TEXT,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

# ======================================
# KNOWLEDGE BASE
# ======================================

knowledge_base = {
    "hello": "Hello! How can I help you?",
    "course": "We offer AI, Python and Data Science courses.",
    "python": "Python is widely used in AI and backend development.",
    "fees": "Please contact support for fee details.",
    "timing": "Working hours are 9 AM to 6 PM.",
    "bye": "Goodbye! Have a great day!"
}

# ======================================
# NLP PREPROCESSING
# ======================================

def preprocess_text(text):

    tokens = word_tokenize(text.lower())

    stop_words = set(stopwords.words('english'))

    filtered_tokens = [
        word for word in tokens
        if word.isalnum() and word not in stop_words
    ]

    return filtered_tokens

# ======================================
# CHATBOT RESPONSE ENGINE
# ======================================

def generate_response(user_message):

    processed_words = preprocess_text(user_message)

    for word in processed_words:

        if word in knowledge_base:
            return knowledge_base[word]

    return "Sorry, I couldn't understand your question."

# ======================================
# SAVE CHAT LOGS
# ======================================

def save_chat(user_message, bot_response):

    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO chat_logs(user_message, bot_response, created_at)
    VALUES (?, ?, ?)
    """, (user_message, bot_response, str(datetime.now())))

    conn.commit()
    conn.close()

# ======================================
# HOME PAGE
# ======================================

@app.route('/')
def home():

    return render_template_string("""

    <!DOCTYPE html>
    <html>

    <head>

        <title>AI Chatbot</title>

        <style>

            body{
                font-family: Arial;
                background:#f2f2f2;
            }

            .container{
                width:500px;
                margin:auto;
                margin-top:50px;
                background:white;
                padding:20px;
                border-radius:10px;
            }

            #chat-box{
                height:300px;
                overflow-y:scroll;
                border:1px solid gray;
                padding:10px;
                margin-bottom:20px;
            }

            input{
                width:75%;
                padding:10px;
            }

            button{
                padding:10px;
            }

        </style>

    </head>

    <body>

        <div class="container">

            <h2>AI Chatbot</h2>

            <div id="chat-box"></div>

            <input type="text" id="message">

            <button onclick="sendMessage()">
                Send
            </button>

        </div>

        <script>

            async function sendMessage(){

                let message =
                document.getElementById("message").value;

                let chatBox =
                document.getElementById("chat-box");

                chatBox.innerHTML +=
                `<p><b>You:</b> ${message}</p>`;

                let response = await fetch('/chat',{

                    method:'POST',

                    headers:{
                        'Content-Type':'application/json'
                    },

                    body:JSON.stringify({
                        message:message
                    })

                });

                let data = await response.json();

                chatBox.innerHTML +=
                `<p><b>Bot:</b> ${data.response}</p>`;

                document.getElementById("message").value = "";

            }

        </script>

    </body>

    </html>

    """)

# ======================================
# CHAT API
# ======================================

@app.route('/chat', methods=['POST'])
def chat():

    data = request.get_json()

    user_message = data.get('message')

    bot_response = generate_response(user_message)

    save_chat(user_message, bot_response)

    return jsonify({
        "response": bot_response
    })

# ======================================
# VIEW LOGS
# ======================================

@app.route('/logs')
def logs():

    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM chat_logs")

    rows = cursor.fetchall()

    conn.close()

    output = ""

    for row in rows:

        output += f"""
        <p>
        <b>User:</b> {row[1]}
        <br>
        <b>Bot:</b> {row[2]}
        <br>
        <b>Time:</b> {row[3]}
        </p>
        <hr>
        """

    return output

# ======================================
# RUN SERVER
# ======================================

if __name__ == "__main__":
    app.run(debug=True)