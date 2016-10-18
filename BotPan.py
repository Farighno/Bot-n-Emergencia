from flask import Flask

app = Flask(__name__)
app.secret_key = "b07p4n1c"

import views.views
