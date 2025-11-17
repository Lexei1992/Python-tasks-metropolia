from flask import Flask, request, Response, jsonify, render_template
import json
app = Flask(__name__)

@app.route("/")
def moikka():
    return "Terve maailma"

# http://127.0.0.1:3000/summa?luku1=13&luku2=28




@app.route('/kaiku/<teksti>/<kertaa>')
def kaiku(teksti, kertaa):
    print(teksti, kertaa)
    tulos = ""
    for i in range(int(kertaa)):
        tulos += teksti + " "
    vastaus = {
        "kaiku": tulos
    }

    return vastaus


@app.route('/summa/<luku1>/<luku2>')
def summa(luku1, luku2):
    try:
        luku1 = float(luku1)
        luku2 = float(luku2)
        summa = luku1 + luku2

        tilakoodi = 200
        vastaus = {
            "status": tilakoodi,
            "luku1": luku1,
            "luku2": luku2,
            "summa": summa
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen yhteenlaskettava"
        }

    json_vastaus = json.dumps(vastaus)
    #return Response(response=json_vastaus, status=tilakoodi, mimetype="application/json")
    return jsonify(vastaus), tilakoodi

@app.errorhandler(404)
def page_not_found(virhe):
    vastaus = {
        "status": virhe.code,
        "teksti": virhe.description
    }
    jsonvast = json.dumps(vastaus)
    #return Response(response=jsonvast, status=404, mimetype="application/json")
    #return jsonify(vastaus), virhe.code
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)