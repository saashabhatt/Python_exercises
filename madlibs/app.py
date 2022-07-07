from flask import Flask, request, render_template
from random import randint, choice, sample
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)

@app.route('/')
def homepage():
    words = story.prompts
    return render_template("form3.html", words=words)

@app.route('/story')
def show_story:
    text = story.generate(request.args)
    return render_template("story.html", text=text)