from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index():
    hello = "Получилось"
    return render_template('/templates/index.html', hello=hello)

