# Diagram Package

![Capture d'écran 2025-02-12 143721](https://github.com/user-attachments/assets/43651cd9-d91c-4612-bee2-91298e425f71)


## Lexicon

### PresentationLayer : Manages the user interface and interactions
* UserController = Handles operations related to users
* PlaceController = Handles operations related to places
* ReviewController = Handles operations related to reviews
* AmenityController = Handles operations related to amenities

### BusinessLogicLayer : Contains the main logic of the application
* ApplicationFacade = Simplified interface for the presentation layer

### Services : Provides specific services for each entity
* UserService = Manages business logic for users
* PlaceService = Manages business logic for places
* ReviewService = Manages business logic for reviews
* AmenityService = Manages business logic for amenities

### PersistenceLayer : Manages data storage and retrieval
* UserRepository = Handles access to user data
* PlaceRepository = Handles access to place data
* ReviewRepository = Handles access to review data
* AmenityRepository = Handles access to amenity data


# Diagram class

![Capture d'écran 2025-02-13 095033](https://github.com/user-attachments/assets/033d9c3a-ecbb-4b64-9904-c5d5f7272077)

## Lexicon

### Classes
* BaseModel: Parent class for all entities
* User: Represents application users
* Place: Represents accommodations
* Review: Represents user reviews for places
* Amenity: Represents features or services of places
### Attributes
* Characteristics of each class (e.g., first_name, price, rating)
* Denoted by + for public visibility
### Methods
* Operations that can be performed on class instances (e.g., register(), update())
* Also denoted by + for public visibility
### Relationships
* Inheritance: Shown by an arrow from child to parent (e.g., User to BaseModel)
* Association: Shown by a line between classes (e.g., User to Place)
* Multiplicity: Numbers or symbols near line ends (e.g., "1" and "*")


