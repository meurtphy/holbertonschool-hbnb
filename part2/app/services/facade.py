from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()

    def create_user(self, user_data):
        user = User(**user_data)
        user.validate()  # Appel de la méthode de validation
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def get_all_users(self):
        """Retrieve all users from the repository"""
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        """Update user with new data"""
        user = self.get_user(user_id)
        if user:
            self.user_repo.update(user_id, user_data)
            return user
        return None


    def create_amenity(self, amenity_data):
        """Create a new amenity"""
        if len(amenity_data['name']) > 50:
            raise ValueError("Amenity name must be 50 characters or less")
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        """Get an amenity by ID"""
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        """Get all amenities"""
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        """Update an amenity"""
        if 'name' in amenity_data and len(amenity_data['name']) > 50:
            raise ValueError("Amenity name must be 50 characters or less")
        amenity = self.get_amenity(amenity_id)
        if amenity:
            self.amenity_repo.update(amenity_id, amenity_data)
            return amenity
        return None

    def create_place(self, place_data):
        if len(place_data['title']) > 100:
            raise ValueError("Title must be 100 characters or less")
        if place_data['price'] < 0:
            raise ValueError("Price must be a non-negative number")
        if not (-90 <= place_data['latitude'] <= 90):
            raise ValueError("Latitude must be between -90 and 90")
        if not (-180 <= place_data['longitude'] <= 180):
            raise ValueError("Longitude must be between -180 and 180")
        owner = self.get_user(place_data['owner_id'])
        if not owner:
            raise ValueError("Owner not found")
        place = Place(
            title=place_data['title'],
            description=place_data.get('description', ''),
            price=place_data['price'],
            latitude=place_data['latitude'],
            longitude=place_data['longitude'],
            owner=owner
        )
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.place_repo.get(place_id)
        if place:
            if 'title' in place_data and len(place_data['title']) > 100:
                raise ValueError("Title must be 100 characters or less")
            if 'price' in place_data and place_data['price'] < 0:
                raise ValueError("Price must be a non-negative number")
            if 'latitude' in place_data and not (-90 <= place_data['latitude'] <= 90):
                raise ValueError("Latitude must be between -90 and 90")
            if 'longitude' in place_data and not (-180 <= place_data['longitude'] <= 180):
                raise ValueError("Longitude must be between -180 and 180")
            self.place_repo.update(place_id, place_data)
        return place

    def create_review(self, review_data):
        if not (1 <= review_data['rating'] <= 5):
            raise ValueError("Rating must be between 1 and 5")
        user = self.get_user(review_data['user_id'])
        if not user:
            raise ValueError("User not found")
        place = self.get_place(review_data['place_id'])
        if not place:
            raise ValueError("Place not found")
        review = Review(
            text=review_data['text'],
            rating=review_data['rating'],
            place=place,
            user=user
        )
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        place = self.get_place(place_id)
        if not place:
            raise ValueError("Place not found")
        return [review for review in self.review_repo.get_all() if review.place.id == place_id]

    def update_review(self, review_id, review_data):
        review = self.review_repo.get(review_id)
        if review:
            if 'rating' in review_data and not (1 <= review_data['rating'] <= 5):
                raise ValueError("Rating must be between 1 and 5")
            self.review_repo.update(review_id, review_data)
            return review
        return None

    def delete_review(self, review_id):
        review = self.review_repo.get(review_id)
        if review:
            self.review_repo.delete(review_id)
            return True
        return False

    def is_valid_email(self, email):
        """Validate email format"""
        import re
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None