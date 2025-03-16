from flask import Flask
from home import main as home  # Importing the main function from home.py and renaming it to home
from chat import main as chat  # Importing the main function from chat.py and renaming it to chat
from app1 import main as text  # Importing the main function from app1.py and renaming it to text

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return home()  # Calls the home() function (which is the main() function from home.py)

# Route for the chat page
@app.route('/chat')
def chat_route():
    return chat()  # Calls the chat() function (which is the main() function from chat.py)

# Route for the text page
@app.route('/text')
def text_route():
    return text()  # Calls the text() function (which is the main() function from app1.py)

if __name__ == '__main__':
    app.run(debug=True)