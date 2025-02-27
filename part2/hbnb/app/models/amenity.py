from .base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.validate()

    def validate(self):
        """Validate amenity attributes"""
        if not hasattr(self, 'name') or not self.name or not self.name.strip():
            raise ValueError("Name is required and cannot be empty")
        if len(self.name) > 50:
            raise ValueError("Name must be 50 characters or less")

    def to_dict(self):
        """Convert the amenity object to a dictionary"""
        amenity_dict = super().to_dict()
        amenity_dict.update({
            'name': self.name
        })
        return amenity_dict

    # Remove the update method to use the one from BaseModel
