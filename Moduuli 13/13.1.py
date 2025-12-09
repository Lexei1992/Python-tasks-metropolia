from flask import Flask, request, Response, jsonify, render_template
import json
app = Flask(__name__)

@app.route('/alkuluku/<number>')
def alkuluku(number):
    try:
            luku = number
            luku = int(luku)

            if luku < 2:
                print("Ei ole alkuluku!")
            else:
                on_alkuluku = True
                for i in range(2, luku):
                    if luku % i == 0:
                        on_alkuluku = False

                if on_alkuluku:
                    print("On alkuluku!")
                else:
                    print("Ei ole alkuluku!")

            vastaus = {
                "luku": luku,
                "on_alkuluku": on_alkuluku
            }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen yhteenlaskettava"
        }

    return jsonify(vastaus)

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)