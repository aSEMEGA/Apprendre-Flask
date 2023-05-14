from flask import *
import datetime



app = Flask(__name__)

@app.route("/")
def bonjour():
    return render_template("index.html")

listes_eleves = [
    {'nom': 'Diallo', 'prenom': 'Abba', 'classe': 'l3GL'},
    {'nom': 'Traore', 'prenom': 'Abou', 'classe': 'l2AP'},
    {'nom': 'Malle', 'prenom': 'Seydou', 'classe': 'l1IG'},
    {'nom': 'Keita', 'prenom': 'Bakary', 'classe': 'm1GI'}
]

@app.route("/eleve")
def eleve():
    classe = request.args
    return render_template("eleve.html", eleves = listes_eleves)
    
if __name__ == '__main__':
    app.run(debug=True)


    

