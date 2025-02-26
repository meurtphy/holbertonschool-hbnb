from app.models.base_model import BaseModel
from app.models.user import User
from app.models.place import Place

class Review(BaseModel):
    """Représente un avis sur un lieu"""

    def __init__(self, text, rating, place: Place, user: User):
        super().__init__()
        self.text = text
        self.rating = rating  # Doit être entre 1 et 5
        self.place = place
        self.user = user
