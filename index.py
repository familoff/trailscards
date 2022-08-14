import datetime
import random
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f769951c2b0e491f0119cbab581aeb69de9b6e72'
app.permanent_session_lifetime = datetime.timedelta(days=2)

global cards, history, info
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

@app.route('/', methods=['GET', 'POST'])
def index():
    session.permanent = True
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
    if 'cards' not in session:
        session['cards'] = cards
        session['card1'] = card1
        session['card1'] = card2
        session['play'] = play
        session['cardimg1'] = cardimg1
        session['cardimg2'] = cardimg2
        session['history'] = history
    info = len(cards)

    return render_template('index.html', cards=cards, card1=card1, card2=card2, play=play, cardimg1=cardimg1, cardimg2=cardimg2, history=history, info=info)

def cardsadd():
    global cards
    cards = ["Пустыня", "Пустыня", "Пустыня", "Пустыня", "Пустыня", "Пустыня", "Пустыня", "Пустыня",
             "Лес", "Лес", "Лес", "Лес", "Лес", "Лес", "Лес", "Гора", "Гора", "Гора", "Гора", "Гора", "Гора",
             "Вода", "Вода", "Вода", "Вода", "Любой ландшафт", "Любой ландшафт", ]
    [random.shuffle(cards) for i in range(7)]
    return cards


@app.route('/background_process_test')
def background_process_test():
    print("Hello")
    return "nothing"

if __name__ == '__main__':
    app.run()