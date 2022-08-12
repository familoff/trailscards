from flask import Flask

app = Flask(__name__)

@app.route('/')
def result():
   return render_template('index.html')

