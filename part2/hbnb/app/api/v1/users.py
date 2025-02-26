from flask_restx import Namespace, Resource, fields
from app.services import facade

# Création de l'espace de noms pour les utilisateurs
api = Namespace('users', description='User operations')

# Définition du modèle de données pour valider l'entrée utilisateur et documenter l'API
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user')
})

"""
    explication :
    - Crée un utilisateur (POST) et retourne un statut 201 si réussi.
    - Vérifie si l'email est déjà enregistré (400 si oui).
    - Retourne une erreur 400 si les données sont invalides.
"""
@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        user_data = api.payload

        # Vérifie si l'email est déjà utilisé
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

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
@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        # Retourne les informations de l'utilisateur trouvé
        return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}, 200

