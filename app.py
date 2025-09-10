from flask import Flask, render_template, request, jsonify, session
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
# We need a secret key to use sessions
app.secret_key = os.urandom(24)

# Configure the Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_chat_model():
    """Initializes and returns the Gemini Pro model."""
    return genai.GenerativeModel('gemini-1.5-flash')

@app.route("/")
def index():
    # Clear chat history when the user first visits the page
    session.pop('chat_history', None)
    return render_template("index.html")

@app.route("/send_message", methods=["POST"])
def send_message():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    model = get_chat_model()
    
    # Retrieve chat history from session or start a new one
    chat_history = session.get('chat_history', [])
    
    chat = model.start_chat(history=chat_history)

    try:
        print(user_message)
        response = chat.send_message(user_message)
        print(response.text)
        
        
        # Update the chat history in the session
        # The history object from the library is not directly JSON serializable,
        # so we convert it to a list of dictionaries.
        session['chat_history'] = [
            {'role': msg.role, 'parts': [part.text for part in msg.parts]} 
            for msg in chat.history
        ]
        
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
