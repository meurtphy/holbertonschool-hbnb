from flask_restx import Namespace, Resource, fields
<<<<<<< HEAD
from app.services import facade

# Création de l'espace de noms pour les utilisateurs
api = Namespace('users', description='User operations')

# Définition du modèle de données pour valider l'entrée utilisateur et documenter l'API
=======
from app.services.facade import facade

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
>>>>>>> origin/main
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user')
})

<<<<<<< HEAD
"""
    explication :
    - Crée un utilisateur (POST) et retourne un statut 201 si réussi.
    - Vérifie si l'email est déjà enregistré (400 si oui).
    - Retourne une erreur 400 si les données sont invalides.
"""
=======
>>>>>>> origin/main
@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        user_data = api.payload

<<<<<<< HEAD
        # Vérifie si l'email est déjà utilisé
=======
        # Check if email is already registered
>>>>>>> origin/main
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

<<<<<<< HEAD
        # Création et retour du nouvel utilisateur
        new_user = facade.create_user(user_data)
        return {'id': new_user.id, 'first_name': new_user.first_name, 'last_name': new_user.last_name, 'email': new_user.email}, 201

    @api.response(200, 'List of users retrieved successfully')
    def get(self):
        """ Get all users"""
        users = facade.get_all_users()
        return [{'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email} for user in users], 200

"""
    explication :
    - Récupère les détails d'un utilisateur (GET) et retourne 200 si trouvé.
    - Retourne 404 si l'utilisateur n'existe pas.
"""
=======
        try:
            new_user = facade.create_user(user_data)
            return {'id': new_user.id, 'first_name': new_user.first_name, 'last_name': new_user.last_name, 'email': new_user.email}, 201
        except ValueError as e:
            return {'error': str(e)}, 400

    @api.response(200, 'List of users retrieved successfully')
    def get(self):
        """Get all users"""
        users = facade.get_all_users()
        return [{'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email} for user in users], 200

>>>>>>> origin/main
@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
<<<<<<< HEAD

        # Retourne les informations de l'utilisateur trouvé
        return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}, 200

=======
        return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}, 200

    @api.expect(user_model, validate=True)
    @api.response(200, 'User successfully updated')
    @api.response(404, 'User not found')
    @api.response(400, 'Invalid input data')
    def put(self, user_id):
        """Update user details"""
        user_data = api.payload
        updated_user = facade.update_user(user_id, user_data)
        if not updated_user:
            return {'error': 'User not found'}, 404
        return {'id': updated_user.id, 'first_name': updated_user.first_name, 'last_name': updated_user.last_name, 'email': updated_user.email}, 200
>>>>>>> origin/main
