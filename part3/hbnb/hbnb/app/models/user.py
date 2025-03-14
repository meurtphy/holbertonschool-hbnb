# app/models/user.py

from app import db, bcrypt  # Import unique et centralisé
from .base_model import BaseModel
import re
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import validates, relationship  # ← On ajoute relationship
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# On ne supprime rien d'existant, on se contente d'ajouter relationship()

class User(BaseModel, db.Model):  # ← On indique explicitement db.Model pour les relations
    __tablename__ = 'users'

    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    is_admin = Column(Boolean, default=False)

    # Relation One-to-Many : Un User peut créer plusieurs Places
    # On ne touche pas au reste du code
    places = relationship('Place', back_populates='user', cascade='all, delete-orphan')

    def __init__(self, *args, **kwargs):
        """Constructeur hybride"""
        super().__init__(*args, **kwargs)
        if 'password' in kwargs:
            self.hash_password(kwargs['password'])
        self.validate()

    @validates('email')
    def validate_email(self, key, email):
        if not re.match(r'^[\\w\\.-]+@[\\w-]+\\.[\\w]{2,3}$', email):
            raise ValueError("Email invalide")
        return email

    def hash_password(self, password):
        """Votre méthode gardée avec amélioration"""
        if not password.strip():
            raise ValueError("Mot de passe vide")
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Vérification conservée avec contrôle de nullité"""
        if not self.password:
            return False
        return bcrypt.check_password_hash(self.password, password)

    def validate(self):
        """Méthode de validation manuelle conservée"""
        if not self.first_name or len(self.first_name) > 50:
            raise ValueError("First name must be between 1 and 50 characters")
        if not self.last_name or len(self.last_name) > 50:
            raise ValueError("Last name must be between 1 and 50 characters")
        if not self.is_valid_email(self.email):
            raise ValueError("Invalid email format")

    @staticmethod
    def is_valid_email(email):
        """Méthode statique conservée"""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def __repr__(self):
        return f"<User {self.email}>"
