import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)


@app.route("/")
def aplicacao():

    cont = 1
    voltas = 1
    num = 3

    primos = "2 -- "

    while voltas < 100:
        n_primo = True
        for i in range(2, num):
            if num % i == 0:
                n_primo = False
                break
        if n_primo:
            primos = primos + str(num) + " -- "
            voltas += 1

        num += 1

    return primos


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
