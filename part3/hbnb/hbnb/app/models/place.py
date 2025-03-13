# app/models/place.py

from app import db
from .base_model import BaseModel
from .user import User  # On ne définit pas de relation, mais on conserve l'import
from sqlalchemy import Column, Integer, String, Float

class Place(BaseModel, db.Model):
    """
    Mapping de l'entité Place en SQLAlchemy, SANS relation.
    On conserve le code existant (owner, reviews, amenities)
    mais sans créer de clé étrangère ni table d'association.
    """
    __tablename__ = 'places'

    # Colonnes exigées par la consigne (id, title, description, price, latitude, longitude)
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, default=0.0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    # Le code contient owner_id : on en fait une simple colonne, SANS relation SQL
    owner_id = Column(String, nullable=True)

    def __init__(self, title, description, price, latitude, longitude, owner_id=None, owner=None):
        super().__init__()  # Appel du constructeur BaseModel
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude

        # On conserve le mécanisme owner / owner_id
        self._owner = None
        self.owner_id = owner_id
        if owner:
            self._owner = owner
            self.owner_id = owner.id

        # On conserve les listes 'reviews' et 'amenities'
        self.reviews = []
        self.amenities = []

        # Validation interne
        self.validate_attributes()

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, User):
            raise ValueError("Owner must be an instance of User")
        self._owner = value
        self.owner_id = value.id

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
        """Add a review to the place (non relié à la BDD)."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place (non relié à la BDD)."""
        self.amenities.append(amenity)

    def __repr__(self):
        return f"<Place title='{self.title}' price={self.price}>"
