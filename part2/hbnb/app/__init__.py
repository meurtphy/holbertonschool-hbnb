from flask import Flask
from flask_restx import Api
<<<<<<< HEAD
=======
from .api.v1.users import api as users_ns
from .api.v1.amenities import api as amenities_ns
from .api.v1.places import api as places_ns
from .api.v1.reviews import api as reviews_ns
>>>>>>> origin/main

def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API', doc='/api/v1/')

<<<<<<< HEAD
=======
    # Register the users namespace
    api.add_namespace(users_ns, path='/api/v1/users')

    # Register the amenities namespace
    api.add_namespace(amenities_ns, path='/api/v1/amenities')

    # Register the places namespace
    api.add_namespace(places_ns, path='/api/v1/places')

    # Register the reviews namespace
    api.add_namespace(reviews_ns, path='/api/v1/reviews')

>>>>>>> origin/main
    return app
