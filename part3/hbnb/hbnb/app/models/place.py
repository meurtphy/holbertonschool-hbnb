# app/models/place.py

from app import db
from .base_model import BaseModel
from .user import User
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Place(BaseModel, db.Model):
    """
    Modèle Place en SQLAlchemy avec la relation One-to-Many avec User,
    et (nouvelle) relation One-to-Many avec Review (sans supprimer l'existant).
    """
    __tablename__ = 'places'

    # Colonnes imposées
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, default=0.0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    # Lien avec User
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    user = relationship('User', back_populates='places', lazy=True)

    # Relation ORM explicite (nouvelle) avec Review
    # On NE supprime pas self.reviews (liste Python), donc on utilise un autre nom "reviews_orm"
    reviews_orm = relationship('Review', back_populates='place_orm', lazy=True)

    def __init__(self, title, description, price, latitude, longitude, owner_id=None, owner=None):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude

        # On conserve le mécanisme existant
        self._owner = None
        self.owner_id = owner_id
        if owner:
            self._owner = owner
            self.owner_id = owner.id
            self.user = owner  # Synchronise la relation ORM

        # On conserve les listes 'reviews' et 'amenities'
        self.reviews = []
        self.amenities = []

        self.validate_attributes()

    @property
    def owner(self):
        """
        Propriété existante, on la garde.
        On ne supprime rien comme demandé.
        """
        return self._owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, User):
            raise ValueError("Owner must be an instance of User")
        self._owner = value
        self.owner_id = value.id
        self.user = value  # Synchronisation avec la relation ORM

    def validate_attributes(self):
        if not isinstance(self.title, str) or not self.title.strip():
            raise ValueError("Title must be a non-empty string")
        if not isinstance(self.description, str):
            raise ValueError("Description must be a string")
        if not isinstance(self.price, (int, float)) or self.price < 0:
            raise ValueError("Price must be a non-negative number")
        if not isinstance(self.latitude, (int, float)) or not (-90 <= self.latitude <= 90):
            raise ValueError("Latitude must be a number between -90 and 90")
        if not isinstance(self.longitude, (int, float)) or not (-180 <= self.longitude <= 180):
            raise ValueError("Longitude must be a number between -180 and 180")

    def add_review(self, review):
        """
        On conserve la logique existante, non reliée à la BDD.
        (reviews_orm est la relation ORM, reviews est la liste Python).
        """
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """On conserve la logique existante, non reliée à la BDD."""
        self.amenities.append(amenity)

    def __repr__(self):
        return f"<Place title='{self.title}' price={self.price}>"
