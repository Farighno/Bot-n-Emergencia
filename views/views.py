from BotPan import app
from flask import render_template, redirect
from api.apis import mandaMensaje, registro, ingreso, telefonosUrgencias
from forms.forms import identificacion, regTelefonosUrgencias
import json

@app.route("/reg", methods=('GET','POST'))
def registrarse():
    miForm = identificacion()
    if miForm.validate_on_submit():
        registro(miForm.nombres.data, miForm.identificadores.data)
        return redirect ("/ingreso") 
    else:
        return render_template("registro.html", form = miForm)

@app.route("/ingreso", methods=('GET','POST'))
def ingresar():
    miForm = identificacion()
    if miForm.validate_on_submit():
       global nom, ident, user
       nom=(miForm.nombres.data)
       ident=(miForm.identificadores.data)
       user=ingreso(nom,ident)
       return redirect ("/main")
    else:
       return render_template("ingreso.html", form = miForm)

@app.route("/tels", methods=('GET','POST'))
def telef():
    miForm = regTelefonosUrgencias()
    if miForm.validate_on_submit():
       global user
       telefonosUrgencias(user, miForm.data)
       return redirect ("/main")
    else:
       return render_template("telefonos.html", form = miForm)
    
@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/alerta")
def alerta():
    global user
    mandaMensaje(user)
    return render_template("alerta.html")
