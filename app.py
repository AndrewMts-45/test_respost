from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "primeira aplicacao no Git"

if __name__ == '__main__':
    app.run(debug=True)
