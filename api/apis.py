import requests
from twilio.rest import TwilioRestClient
import pyrebase

key="AIzaSyA2Tz2CziRNMG-DaKDHBf2F_QsQHtW2kd8"
dataURL="https://bot-emergencia.firebaseio.com/"
authDomain= "bot-emergencia.firebaseapp.com"
storage= "bot-emergenia.appspot.com"
apiKey="AIzaSyCZbIGwT1yeZxj3LxnmgVtpGZQGu7nXBWA"
config = {"apiKey":apiKey,"authDomain":authDomain,"databaseURL":dataURL,"storageBucket":storage}
firebase = pyrebase.initialize_app(config)
auth=firebase.auth()
db=firebase.database()
account_sid = "ACe1a53fc2c6ea19685bd06a504ed0a266"
auth_token = "5b98e604ad2ba89c63b155f23a0fd173"
client = TwilioRestClient(account_sid, auth_token)

def mapa():
    Ubicacion=requests.post("https://www.googleapis.com/geolocation/v1/geolocate?",params={"key":apiKey}).json()
    latitud = (Ubicacion["location"]["lat"])
    longitud = (Ubicacion["location"]["lng"])
    parameters = {"latlng":str(latitud) + ", " + str(longitud), "key":key}
    resultado = requests.get("https://maps.googleapis.com/maps/api/geocode/json?", params=parameters).json()
    listado = resultado["results"][0]
    direccion = listado["formatted_address"]
    return (direccion)

def mandaMensaje(user):
    direccion=mapa()
    correo=user['email']
    correo=correo.replace("@", "")
    correo=correo.replace(".", "")
    a=[1,2,3,4,5]
    for x in a:
        x=str(x)
        tel=("tel"+x)
        telefonos = db.child(correo).child("telefonos").child(tel).get(user['idToken'])   
        telefonos = str ("+52"+telefonos.val())
        if len (telefonos)==13:
            message=client.sms.messages.create(body = "¡Ayuda!, estoy en "+direccion,to = telefonos ,from_= "+13346414058")

def registro(email, password):
    usuario=auth.create_user_with_email_and_password(email, password)
    
def ingreso(email, password):
    usuario=auth.sign_in_with_email_and_password(email, password)
    return usuario

def telefonosUrgencias(usuario, telefonos):
    correo=usuario['email']
    correo=correo.replace("@", "")
    correo=correo.replace(".", "")
    data = {correo: {"telefonos": telefonos}}
    db.update(data,usuario['idToken'])
