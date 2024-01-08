from flask import Flask
from random import randint

app = Flask(__name__)
random_number = randint(0, 9)


@app.route("/")
def home():
    return ("<h1 style='text-align:center;color:blue'>Guess a number between 0 and 9</h1>"
            "<img style='display: block; margin: 0 auto;' width=400 height=400 "
            "src='https://media2.giphy.com/media/Rs2QPsshsFI9zeT4Kn/200w.webp?cid"
            "=ecf05e476ftsjftj294zsfeywrci4rrv6ptruhesi28iilps&ep=v1_gifs_search&rid=200w.webp&ct=g' />")


@app.route("/<int:number>")
def guess_number(number):
    if number == random_number:
        return ("<h1 style='text-align:center;color:green'>You found me!</h1>"
                "<img style='display: block; margin: 0 auto;' width=400 height=400 "
                "src='https://media1.giphy.com/media/JKcneNkriqxQbE8e49/200w.webp?cid"
                "=ecf05e47qkbiegfo5nhg60d1l5qsgrpk3ow94ee0ovwgyggb&ep=v1_gifs_search&rid=200w.webp&ct=g'/>")
    elif number < random_number:
        return ("<h1 style='text-align:center;color:blue'>Too low, try again!</h1>"
                "<img style='display: block; margin: 0 auto;' width=400 height=400 "
                "src='https://media4.giphy.com/media/TgmiJ4AZ3HSiIqpOj6/200w.webp?cid"
                "=ecf05e47467oty4i2arklh4t6u1h1hn9srtcwodd69s9y1pf&ep=v1_gifs_search&rid=200w.webp&ct=g'/>")
    else:
        return ("<h1 style='text-align:center;color:red'>Too high, try again!</h1>"
                "<img style='display: block; margin: 0 auto;' width=400 height=400 "
                "src='https://media3.giphy.com/media/UFRtykmfyBA8F7qPh9/200.webp?cid"
                "=ecf05e47olw99mz9nvru6r1x6n119zdqit37s0ydnxedivak&ep=v1_gifs_search&rid=200.webp&ct=g'/>")


if __name__ == "__main__":
    app.run(debug=True)
