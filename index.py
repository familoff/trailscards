from flask import Flask, render_template

app = Flask(__name__)

@app.route('/templates')
def index():
    hello = "Получилось"
    return render_template('index.html', hello=hello)
