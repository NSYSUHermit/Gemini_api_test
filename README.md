# Gemini Chat Web Application

This is a simple web application that provides a chat interface to interact with Google's Gemini Pro model. It's built with Flask for the backend and simple HTML, CSS, and JavaScript for the frontend.

## Project Structure

```
/
├── .env                # Stores environment variables like your API key
├── app.py              # The main Flask application file
├── requirements.txt    # Python dependencies
├── static/               # Contains CSS and JavaScript files
│   ├── style.css
│   └── script.js
└── templates/            # Contains HTML templates
    └── index.html
```

- **`app.py`**: The core of the application. It's a Flask server that handles two main routes:
  - `/`: Renders the main chat page (`index.html`).
  - `/send_message`: An API endpoint that receives user messages, communicates with the Gemini API, and returns the model's response. It uses Flask sessions to maintain a separate conversation history for each user.
- **`templates/index.html`**: The main HTML file for the user interface.
- **`static/`**: Contains the CSS for styling the chat interface and the JavaScript for handling user input and communication with the backend.
- **`.env`**: A file to securely store your Gemini API key. You will need to create this file.
- **`requirements.txt`**: Lists all the Python packages required to run the project.

## Setup and Installation

Follow these steps to get the application running on your local machine.

### 1. Create a `.env` file

Create a new file named `.env` in the root of the project directory and add your Gemini API key like this:

```
GEMINI_API_KEY="YOUR_API_KEY_HERE"
```

Replace `"YOUR_API_KEY_HERE"` with your actual key.

### 2. Install Dependencies

It is recommended to use a virtual environment to keep dependencies isolated.

```bash
# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install the required packages
pip install -r requirements.txt
```

## Running the Application

Once the setup is complete, you can run the application with a single command:

```bash
python app.py
```

After running the command, you will see output indicating that the server is running, similar to this:

```
 * Running on http://127.0.0.1:5000
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: ...
```

Now, open your web browser and navigate to:

[http://127.0.0.1:5000](http://127.0.0.1:5000)

You should see the chat interface and can start a conversation with Gemini.

![image](https://github.com/NSYSUHermit/Gemini_api_test/demo.png)

