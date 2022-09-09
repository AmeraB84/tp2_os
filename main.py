from flask import Flask,render_template,request,send_file,redirect,url_for,Response,redirect
from chooseMonstre import *

app = Flask(__name__)

import sys
import os


@app.route('/',methods=['GET','POST'])

def Menu():
    if request.form :
       pseudo = request.form.get('name')
       liste_monstres = []
       nbre_monstre = 4

       for i in range(nbre_monstre):
           nom_monstre = chooseMonstre(liste_nom)
           liste_monstres.append(nom_monstre)
       

       liste_pseudo = [pseudo,nbre_monstre]
       return render_template('index.html',pseudo=pseudo,nbre_monstre=nbre_monstre,liste_pseudo=liste_pseudo,liste_monstres=liste_monstres)
    else:
       return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8001)
