# Diagram Package































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