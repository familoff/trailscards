import random
from flask import Flask, render_template, request, session

app = Flask(__name__)
global cards, history
cards = ["Пустыня", "Пустыня", "Пустыня", "Пустыня", "Пустыня", "Пустыня", "Пустыня", "Пустыня",
         "Лес", "Лес", "Лес", "Лес", "Лес", "Лес", "Лес", "Гора", "Гора", "Гора", "Гора", "Гора", "Гора",
         "Вода", "Вода", "Вода", "Вода", "Любой ландшафт", "Любой ландшафт", ]
[random.shuffle(cards) for i in range(7)]
play = 'Начать игру'

cardimg = {'Пустыня': 'static/sand.png', 'Лес': 'static/wood.png', 'Гора': 'static/mount.png',
           'Вода': 'static/water.png', 'Любой ландшафт': 'static/all.png', 'Back': 'static/back.png'}
cardimg1 = ""
cardimg2 = ""

history = []
history_count = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    if len(cards) >= 26:
        history.clear()
    if request.method != 'POST':
        play = 'Начать игру'
        card1 = ""
        card2 = ""
        cardimg1 = cardimg.get("Back")
        cardimg2 = cardimg.get("Back")
    if request.method == 'POST':
        play = 'Следующие карты'
        card1 = cards[0]
        card2 = cards[1]
        cardimg1 = cardimg.get(card1)
        cardimg2 = cardimg.get(card2)
        history.append(cardimg1)
        history.append(cardimg2)
        cards.pop(0)
        cards.pop(0)
    if len(cards) <= 1:
        play = 'Начать новую игру'
        cardsadd()

    return render_template('index.html', cards=cards, card1=card1, card2=card2, play=play, cardimg1=cardimg1, cardimg2=cardimg2, history=history)

def cardsadd():
    global cards
    cards = ["Пустыня", "Пустыня", "Пустыня", "Пустыня", "Пустыня", "Пустыня", "Пустыня", "Пустыня",
             "Лес", "Лес", "Лес", "Лес", "Лес", "Лес", "Лес", "Гора", "Гора", "Гора", "Гора", "Гора", "Гора",
             "Вода", "Вода", "Вода", "Вода", "Любой ландшафт", "Любой ландшафт", ]
    [random.shuffle(cards) for i in range(7)]
    return cards

if __name__ == '__main__':
    app.run()