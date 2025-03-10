from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "<strong>Server running</strong>"

def main():
    app.run(port = os.getenv('PORT'))

if __name__ == '__main__':
    main()