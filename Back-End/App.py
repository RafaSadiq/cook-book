# This tells your python backend that your using Flask
from flask import Flask 
# Initializing application
from database.db import initialize_db
# Interface with import Api for backend
from flask_restful import Api
# Initializing routes
from flask_cors import CORS 

from resources.routes import initialize_routes

app = Flask(__name__)
api = Api(app)
CORS(app)

app.config['MONGODB_SETTINGS'] = {


    'host': 'mongodb://localhost/cook-book'

}

initialize_db(app)
initialize_routes(api)

app.run(debug=True)

