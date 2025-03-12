from app import db  # Importez db depuis votre fichier d'initialisation
from .base_model import BaseModel
import uuid
from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(BaseModel, db.Model):
    __tablename__ = 'users'

    # UUID stocké comme chaîne (TEXT) pour compatibilité avec SQLite
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(128), nullable=False)

    # Modification : Utilisation d'Integer pour is_admin (SQLite ne supporte pas directement Boolean)
    is_admin = Column(Integer, default=0)  # 0 pour False, 1 pour True

    def __init__(self, first_name, last_name, email, password, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = int(is_admin)  # Conversion explicite en entier pour SQLite
        self.hash_password(password)  # Hache le mot de passe avant de le stocker
        self.validate()

    def hash_password(self, password):
        from app import bcrypt  # Import différé pour éviter les imports circulaires
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        from app import bcrypt  # Import différé pour éviter les imports circulaires
        return bcrypt.check_password_hash(self.password, password)

    def validate(self):
        if not self.first_name or len(self.first_name) > 50:
            raise ValueError("First name must be between 1 and 50 characters")
        if not self.last_name or len(self.last_name) > 50:
            raise ValueError("Last name must be between 1 and 50 characters")
        if not self.is_valid_email(self.email):
            raise ValueError("Invalid email format")

    @staticmethod
    def is_valid_email(email):
        import re
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None
