import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    cards = ["Пустыня", "Пустыня", "Пустыня", "Пустыня", "Пустыня", "Пустыня", "Пустыня", "Пустыня",
             "Лес", "Лес", "Лес", "Лес", "Лес", "Лес", "Лес", "Гора", "Гора", "Гора", "Гора", "Гора", "Гора",
             "Вода", "Вода", "Вода", "Вода", "Любой ландшафт", "Любой ландшафт",]
    [cards.shuffle() for i in cards]
    return render_template('index.html', cards=cards)
