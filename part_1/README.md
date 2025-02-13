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


# Diag sequence

![alt text](<Capture d'écran 2025-02-13 104216-1.png>)

## Lexicon
### Participants
* Boxes at the top: Represent actors, objects, or systems involved in the interaction
### Lifelines
* Vertical dashed lines: Extend from each participant, representing their existence over time
### Messages
* Horizontal arrows: Show communication between participants
* Solid arrows: Synchronous messages (sender waits for response)
* Dashed arrows: Asynchronous messages (sender doesn't wait)
### Activations
* Thin rectangles on lifelines: Indicate when a participant is active or processing


# HBnB General Lexicon

## Core Concepts
* Layered Architecture: An architectural pattern that organizes an application into distinct layers (Presentation, Business Logic, Persistence), each with specific responsibilities.
* Facade Pattern: A design pattern that provides a simplified, unified interface to a set of interfaces in a subsystem, promoting loose coupling between layers.
* UML (Unified Modeling Language): A standardized modeling language used to create diagrams representing the structure and behavior of software systems.
* API (Application Programming Interface): A set of protocols and tools for building software applications, specifying how software components should interact.
* CRUD Operations: Basic data operations (Create, Read, Update, Delete) performed on entities within the system.
## Key Entities
* User: Represents an application user, with attributes like first_name, last_name, email, and password.
* Place: Represents a property or accommodation listing, with attributes like title, description, price, latitude, and longitude.
* Review: Represents a user's review of a place, including a rating and comment.
* Amenity: Represents a feature or service offered at a place, with attributes like name and description.
* BaseModel: A base class providing common attributes (id, created_at, updated_at) and methods for all entities.
## Layers
* Presentation Layer: Handles user interaction, including services and API endpoints. Often interacts with the Business Logic Layer.
* Business Logic Layer: Contains the core logic and models representing entities. Enforces business rules and interacts with the Persistence Layer.
* Persistence Layer: Manages data storage and retrieval, interacting directly with the database.
## Diagram Types
* Package Diagram: A high-level diagram showing the organization of the application into packages (layers) and dependencies between them.
* Class Diagram: A detailed diagram representing the structure of classes, their attributes, methods, and relationships (inheritance, association, composition).
* Sequence Diagram: A diagram illustrating the interaction between objects over time, showing the sequence of messages exchanged during a specific use case or API call.
## Common Attributes & Methods
* id (UUID): A universally unique identifier for each entity.
* created_at: Timestamp indicating when the entity was created.
* updated_at: Timestamp indicating when the entity was last updated.
* create(): Method to create a new entity.
* update(): Method to update an existing entity.
* delete(): Method to remove an entity.
* list(): Method to retrieve a list of entities.
## UML Symbols
* '<<Interface>>' : Stereotype indicating an interface.
* '+' : Indicates public visibility of attributes or methods.
* '-->' : Association relationship between classes.
* '--|>' : Inheritance relationship (generalization).
* 'o--' : Composition relationship.
## General Terms
* Repository: A component in the Persistence Layer responsible for data access and management.
* DTO (Data Transfer Object): An object used to transfer data between layers or components.
* ORM (Object-Relational Mapping): A technique that maps objects to database tables, simplifying data access.
* Endpoint: A specific URL in an API that handles a particular request.
### This lexicon should help in understanding the terminology used throughout the HBnB Evolution project documentation and provide a clear reference point for developers and stakeholders.
