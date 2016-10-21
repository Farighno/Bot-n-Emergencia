from BotPan import app
from flask import render_template, redirect
from api.apis import mandaMensaje, registro, ingreso, telefonosUrgencias
from forms.forms import identificacion, regTelefonosUrgencias

@app.route("/")
def intro():
    return render_template("index.html")

@app.route("/reg", methods=('GET','POST'))
def registrarse():
    miForm = identificacion()
    if miForm.validate_on_submit():
        registro(miForm.nombres.data, miForm.identificadores.data)
        return redirect ("/tels") 
    else:
        return render_template("register.html", form = miForm)

@app.route("/ingreso", methods=('GET','POST'))
def ingresar():
    miForm = identificacion()
    if miForm.validate_on_submit():
        global nom, ident, users  
        nom=(miForm.nombres.data)
        ident=(miForm.identificadores.data)
        users=ingreso(nom,ident)
        return redirect ("/main")
    else:
       return render_template("login.html", form = miForm)

@app.route("/tels", methods=('GET','POST'))
def telef():
    miForm = regTelefonosUrgencias()
    if miForm.validate_on_submit():
       global users
       telefonosUrgencias(users, miForm.data)
       return redirect ("/main")
    else:
       return render_template("telefonos.html", form = miForm)
    
@app.route("/main")
def main():
    return render_template("switch.html")

@app.route("/alerta")
def alerta():
    global users
    mandaMensaje(users)
    return redirect ("/main")
