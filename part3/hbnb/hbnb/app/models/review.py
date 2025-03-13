# app/models/review.py

from app import db
from .base_model import BaseModel
from .place import Place  # On ne crée pas de relation DB, on garde juste l'import
from .user import User    # Idem, pas de relation
from sqlalchemy import Column, Integer, String

class Review(BaseModel, db.Model):
    """
    Mapping de l'entité Review en SQLAlchemy, sans relation.
    On conserve la logique Python existante (place, user),
    mais sans clé étrangère et sans association.
    """
    __tablename__ = 'reviews'

    # Colonnes imposées : id (int), text (string), rating (int).
    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)

    # On stocke place_id / user_id en simple champ, sans relation.
    place_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)

    def __init__(self, text, rating, place=None, user=None):
        super().__init__()
        self.text = text
        self.rating = rating

        # Références Python internes (pas de relation DB)
        self._place = None
        self._user = None

        # Si on fournit un place
        if place:
            self._place = place
            self.place_id = getattr(place, "id", None)

        # Si on fournit un user
        if user:
            self._user = user
            self.user_id = getattr(user, "id", None)

        self.validate_attributes()

    def validate_attributes(self):
        if not isinstance(self.text, str) or not self.text.strip():
            raise ValueError("Text must be a non-empty string")
        if not isinstance(self.rating, int) or not (1 <= self.rating <= 5):
            raise ValueError("Rating must be an integer between 1 and 5")
        if self._place and not isinstance(self._place, Place):
            raise ValueError("place must be an instance of Place")
        if self._user and not isinstance(self._user, User):
            raise ValueError("user must be an instance of User")

    @property
    def place(self):
        """Accès au place en Python, non relié en base."""
        return self._place

    @place.setter
    def place(self, value):
        if value and not isinstance(value, Place):
            raise ValueError("place must be a Place instance")
        self._place = value
        self.place_id = getattr(value, "id", None)

    @property
    def user(self):
        """Accès au user en Python, non relié en base."""
        return self._user

    @user.setter
    def user(self, value):
        if value and not isinstance(value, User):
            raise ValueError("user must be a User instance")
        self._user = value
        self.user_id = getattr(value, "id", None)

    def __repr__(self):
        return f"<Review id={self.id} rating={self.rating}>"
