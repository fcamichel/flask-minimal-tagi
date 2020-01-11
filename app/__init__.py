from flask import Flask


app = Flask(__name__)

from app import routes, filters

app.run(host='0.0.0.0')