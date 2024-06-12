from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/steps')
def steps():
    steps = [
        {"text": "Step 1: Preheat your oven to 375°F (190°C).", "underline": ["Preheat"], "gif": "https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif"},
        {"text": "Step 2: Mix the ingredients in a bowl.", "underline": ["Mix"], "gif": "https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif"},
        {"text": "Step 3: Place the mixture into a baking dish.", "underline": ["Place"], "gif": "https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif"},
        {"text": "Step 4: Bake for 25-30 minutes.", "underline": ["Bake"], "gif": "https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif"},
        {"text": "Step 5: Preheat your oven to 375°F (190°C).", "underline": ["Preheat"], "gif": "https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif"},
        {"text": "Step 6: Mix the ingredients in a bowl.", "underline": ["Mix"], "gif": "https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif"},
        {"text": "Step 7: Place the mixture into a baking dish.", "underline": ["Place"], "gif": "https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif"},
        {"text": "Step 8: Bake for 25-30 minutes.", "underline": ["Bake"], "gif": "https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif"}
    ]
    return render_template("index.html", steps = steps)


