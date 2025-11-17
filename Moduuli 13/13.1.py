from flask import Flask, request, Response, jsonify, render_template
import json
app = Flask(__name__)

@app.route('/alkuluku/<number>')
def alkuluku(number):
    try:
        while True:
            luku = number
            if luku == "":
                break
            luku = int(luku)

            if luku < 2:
                print("Ei ole alkuluku!")
            else:
                on_alkuluku = True
                for i in range(2, luku):
                    if luku % i == 0:
                        on_alkuluku = False
                        break

                if on_alkuluku:
                    print("On alkuluku!")
                else:
                    print("Ei ole alkuluku!")

            tilakoodi = 200
            vastaus = {
                "status": tilakoodi,
                "luku": luku,
            }


if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)