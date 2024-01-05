# api/index.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Render and Flask!'

if __name__ == '__main__':
    app.run(debug=True)
