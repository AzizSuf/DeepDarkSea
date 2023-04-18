from flask import Flask, render_template, request
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(32)

# Import all declared routes here
import auth


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/find_player")
def find_player():
    return render_template("find_player.html")


@app.route("/choose_the_door")
def choose_the_door():
    return render_template("choose_the_door.html")


@app.route("/bot/van_darkholme")
def play_van():
    return render_template("van_darkholme.html")


@app.route("/bot/steve_rambo")
def play_steve():
    return "<h1>Тут будет игра против выбранного бота.</h1>"


@app.route("/bot/billy_herrington")
def play_billy():
    return "<h1>Тут будет игра против выбранного бота.</h1>"


@app.route("/bot/uncle_bogdan")
def play_uncle():
    return "<h1>Тут будет игра против выбранного бота.</h1>"


@app.route("/play_human")
def play_human():
    return "<h1>Тут будет игра против игрока.</h1>"


@app.route("/my-endpoint", methods=["POST"])
def handle_post_request():
    print(request.form)
    return "OK"


if __name__ == '__main__':
    app.run(debug=True)
