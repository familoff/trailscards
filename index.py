import random
from flask import Flask, render_template, request

app = Flask(__name__)

play = 0
cards = ["Пустыня", "Пустыня", "Пустыня", "Пустыня", "Пустыня", "Пустыня", "Пустыня", "Пустыня",
         "Лес", "Лес", "Лес", "Лес", "Лес", "Лес", "Лес", "Гора", "Гора", "Гора", "Гора", "Гора", "Гора",
         "Вода", "Вода", "Вода", "Вода", "Любой ландшафт", "Любой ландшафт", ]
[random.shuffle(cards) for i in range(7)]
def Round():
    card1 = cards[0]
    cards.pop(0)
    card2 = cards[0]
    cards.pop(0)

@app.route('/', methods=['POST', 'GET'])
def index():
    while play == (request.form['play']):
        Round()
    return render_template('index.html', cards=cards)
