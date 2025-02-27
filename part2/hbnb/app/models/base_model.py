import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update the attributes of the object based on the provided dictionary"""
        # Create a shallow copy of the current object's dictionary
        temp_dict = self.__dict__.copy()
        
        # Update the temporary dictionary
        temp_dict.update(data)
        
        # Create a temporary object with the updated data
        temp_obj = type(self)(**temp_dict)
        
        # Validate the temporary object
        temp_obj.validate()
        
        # If validation passes, update the actual object
        self.__dict__.update(data)
        
        self.save()  # Update the updated_at timestamp

    def validate(self):
        """Validate the object's attributes"""
        # This method should be overridden by subclasses
        pass

    def to_dict(self):
        """Convert the object to a dictionary"""
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
