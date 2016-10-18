from flask_wtf import Form
from wtforms import StringField, validators

class identificacion(Form):
    nombres = StringField('Nombre', [validators.DataRequired()])
    identificadores = StringField('identificadores', [validators.DataRequired()])

class regTelefonosUrgencias(Form):
    tel1 = StringField('Teléfono 1', [validators.Length(min=10, max=10),validators.DataRequired()])
    tel2 = StringField('Teléfono 2')
    tel3 = StringField('Teléfono 3')
    tel4 = StringField('Teléfono 4')
    tel5 = StringField('Teléfono 5')
