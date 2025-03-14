# app/models/review.py

from app import db
from .base_model import BaseModel
from .place import Place   # On conserve, sans supprimer
from .user import User     # On conserve, sans supprimer
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Review(BaseModel, db.Model):
    """
    Modèle Review en SQLAlchemy,
    ajout de la relation One-to-Many avec Place (place_id -> places.id).
    On ne supprime rien d'existant (place/user, _place/_user, etc.).
    """
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)

    # Conserve place_id / user_id mais on ajoute la ForeignKey pour place_id
    place_id = Column(Integer, ForeignKey('places.id'), nullable=True)
    user_id = Column(Integer, nullable=True)  # On laisse tel quel (étape suivante pour User)

    # Relation SQLAlchemy avec Place
    # NOTE : pour éviter le conflit avec la propriété `place` existante,
    # nous appelons cette relation `sql_place`.
    sql_place = relationship("Place", back_populates="reviews", lazy=True)

    def __init__(self, text, rating, place=None, user=None):
        super().__init__()
        self.text = text
        self.rating = rating

        self._place = None
        self._user = None

        # Si on fournit un place, on synchronise la partie Python + place_id
        if place:
            self._place = place
            self.place_id = getattr(place, "id", None)
            self.sql_place = place  # On renseigne aussi la relation ORM

        # Si on fournit un user, on ne touche pas encore au code ici (étape suivante)
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
        """Accès Python non relié à la BDD, on ne touche pas."""
        return self._place

    @place.setter
    def place(self, value):
        if value and not isinstance(value, Place):
            raise ValueError("place must be a Place instance")
        self._place = value
        self.place_id = getattr(value, "id", None)
        self.sql_place = value  # Synchronisation avec la relation ORM

    @property
    def user(self):
        """Accès Python non relié à la BDD, on ne touche pas (étape suivante)."""
        return self._user

    @user.setter
    def user(self, value):
        if value and not isinstance(value, User):
            raise ValueError("user must be a User instance")
        self._user = value
        self.user_id = getattr(value, "id", None)
        # La relation avec User sera ajoutée à l'étape suivante

    def __repr__(self):
        return f"<Review id={self.id} rating={self.rating}>"
