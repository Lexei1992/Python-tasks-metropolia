from flask import Flask, request, Response, jsonify, render_template
import json
import mysql.connector
app = Flask(__name__)

@app.route('/kentta/<koodi>')
def kentta(koodi):
    try:
        sql = f"SELECT name, municipality FROM airport WHERE ident = '{koodi}'"
        print(sql)
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        if kursori.rowcount > 0:
            for rivi in tulos:
                print(f"Lentokentän nimi: {rivi[0]}. Lentokentän sijainti: {rivi[1]}")
        vastaus = {
            "ICAO": koodi,
            "Lentokentan nimi:": rivi[0],
            "Lentokentan sijainti:": rivi[1]
        }
    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen yhteenlaskettava"
        }

    return jsonify(vastaus)

@app.errorhandler(404)
def page_not_found(virhe):
    vastaus = {
        "status": virhe.code,
        "teksti": virhe.description
    }
    return jsonify(vastaus), virhe.code

# Pääohjelma
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='aleksi',
         password='localallu',
         autocommit=True
         )

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

