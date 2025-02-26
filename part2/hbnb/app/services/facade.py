from app.persistence.repository import InMemoryRepository
from app.models.user import User

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()  # Stockage des utilisateurs

    def create_user(self, user_data):
        """Créer un nouvel utilisateur et vérifier l'unicité de l'email"""
        existing_user = self.user_repo.get_by_attribute("email", user_data["email"])
        if existing_user:
            return None  # Email déjà utilisé
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """Récupérer un utilisateur par son ID"""
        return self.user_repo.get(user_id)

    def get_all_users(self):
        """Récupérer tous les utilisateurs"""
        return self.user_repo.get_all()  # Cette ligne était manquante !
