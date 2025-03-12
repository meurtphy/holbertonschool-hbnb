from flask import Flask
from flask_restx import Api
from app.persistence.repository import db
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.places import api as places_ns
from app.api.v1.reviews import api as reviews_ns
from app.extensions import db, bcrypt, jwt
from app.api.v1.auth import api as auth_ns
from app.api.v1.protector import api as protected_ns



def create_app(config_class="config.DevelopmentConfig"):
    """Create and configure the Flask application"""
    app = Flask(__name__)
    
    # Load the configuration
    app.config.from_object(config_class)

    app.config['JWT_SECRET_KEY'] = 'your-secret-key'
    
    # Initialize the database
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    with app.app_context():
        db.create_all()
    
    # Initialize Flask-RESTX API
    api = Api(
        app, 
        version='1.0', 
        title='HBnB API', 
        description='HBnB Application API', 
        doc='/api/v1/'
    )

    # Register the namespaces
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(places_ns, path='/api/v1/places')
    api.add_namespace(reviews_ns, path='/api/v1/reviews')
    api.add_namespace(auth_ns, path='/api/v1/auth')
    api.add_namespace(protected_ns, path='/api/v1/protector')

    jwt.init_app(app)

    return app