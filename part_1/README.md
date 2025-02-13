# Diagram Package

![Capture d'écran 2025-02-12 143721](https://github.com/user-attachments/assets/43651cd9-d91c-4612-bee2-91298e425f71)


# Lexicon

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

