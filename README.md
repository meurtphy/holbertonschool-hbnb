# 🏠 HBnB Application

Welcome to HBnB (HolbertonBnB), an AirBnB clone application that provides a RESTful API for managing users, places, reviews, and amenities. This project demonstrates the implementation of a robust backend system using Python and Flask.

## 📑 Table of Contents

- [🏠 HBnB Application](#-hbnb-application)
  - [📑 Table of Contents](#-table-of-contents)
  - [🎯 Project Overview](#-project-overview)
  - [✨ Features](#-features)
  - [📁 Project Structure](#-project-structure)
    - [📚 Directory and File Descriptions](#-directory-and-file-descriptions)
  - [🛠️ Implementation Details](#️-implementation-details)
  - [🚀 Installation and Setup](#-installation-and-setup)
  - [▶️ Running the Application](#️-running-the-application)
  - [🧪 Running Tests](#-running-tests)
  - [📖 API Documentation](#-api-documentation)
  - [🔌 API Endpoints](#-api-endpoints)
  - [🧠 Business Logic Layer](#-business-logic-layer)
    - [Entities](#entities)
    - [Validation](#validation)
    - [Unit Tests](#unit-tests)
  - [🤝 Contributing](#-contributing)
  - [📄 License](#-license)
  - [👥 Authors](#-authors)

## 🎯 Project Overview

This project is part of a larger initiative to build a full-fledged AirBnB clone. The current phase (Part 2) focuses on implementing the core business logic and API endpoints. The main objectives of this phase are:

1. Set up a modular project structure following best practices for Python and Flask applications.
2. Implement the business logic layer, including core entities and their relationships.
3. Build RESTful API endpoints for managing users, places, reviews, and amenities.
4. Implement data validation and error handling.
5. Create comprehensive tests to ensure the reliability of the application.

## ✨ Features

- RESTful API for managing users, places, reviews, and amenities
- Robust business logic layer with comprehensive validation
- In-memory data persistence using the Repository pattern (to be replaced with a database in future phases)
- Comprehensive unit tests for all models
- Modular and scalable architecture using the Facade pattern
- Swagger documentation for easy API exploration

## 📁 Project Structure

```
hbnb/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │       ├── __init__.py
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       ├── amenities.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base_model.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   ├── amenity.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── facade.py
│   ├── persistence/
│       ├── __init__.py
│       ├── repository.py
├── tests/
│   ├── test_user.py
│   ├── test_place.py
│   ├── test_review.py
│   ├── test_amenity.py
│   ├── run_tests.py
├── run.py
├── config.py
├── requirements.txt
├── README.md
```

### 📚 Directory and File Descriptions

- `app/`: Contains the core application code.
- `app/api/`: Houses the API endpoints, organized by version.
- `app/models/`: Contains the business logic classes.
- `app/services/`: Implements the Facade pattern for communication between layers.
- `app/persistence/`: Implements the in-memory repository.
- `tests/`: Contains unit tests for the models.
- `run.py`: Entry point for running the Flask application.
- `config.py`: Configuration for environment variables and application settings.
- `requirements.txt`: Lists all Python packages needed for the project.

## 🛠️ Implementation Details

The project is implemented in several stages:

1. **Project Setup and Package Initialization**: Setting up the project structure, implementing the in-memory repository, and preparing the Facade pattern.

2. **Core Business Logic Classes**: Implementing the User, Place, Review, and Amenity classes with their attributes, methods, and relationships.

3. **User Endpoints**: Implementing CRUD operations for users (except DELETE).

4. **Amenity Endpoints**: Implementing CRUD operations for amenities (except DELETE).

5. **Place Endpoints**: Implementing CRUD operations for places (except DELETE), handling relationships with users and amenities.

6. **Review Endpoints**: Implementing CRUD operations for reviews, including DELETE operation.

7. **Testing and Validation**: Implementing validation checks, performing black-box testing, and creating a detailed testing report.

## 🚀 Installation and Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd holbertonschool-hbnb
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Running the Application

To run the application, use the following command:

```bash
python run.py
```

The application will start, and you can access the API at `http://localhost:5000`.

## 🧪 Running Tests

To run the unit tests, use the following command:

```bash
python -m unittest discover tests
```

## 📖 API Documentation

API documentation will be available at `http://localhost:5000/api/v1/` when the application is running. This Swagger documentation provides an interactive interface to explore and test the API endpoints.

## 🔌 API Endpoints

The API provides the following endpoints:

- Users:
  - GET /api/v1/users: List all users
  - POST /api/v1/users: Create a new user
  - GET /api/v1/users/{user_id}: Get a specific user
  - PUT /api/v1/users/{user_id}: Update a user

- Places:
  - GET /api/v1/places: List all places
  - POST /api/v1/places: Create a new place
  - GET /api/v1/places/{place_id}: Get a specific place
  - PUT /api/v1/places/{place_id}: Update a place

- Reviews:
  - GET /api/v1/reviews: List all reviews
  - POST /api/v1/reviews: Create a new review
  - GET /api/v1/reviews/{review_id}: Get a specific review
  - PUT /api/v1/reviews/{review_id}: Update a review
  - DELETE /api/v1/reviews/{review_id}: Delete a review

- Amenities:
  - GET /api/v1/amenities: List all amenities
  - POST /api/v1/amenities: Create a new amenity
  - GET /api/v1/amenities/{amenity_id}: Get a specific amenity
  - PUT /api/v1/amenities/{amenity_id}: Update an amenity

## 🧠 Business Logic Layer

The Business Logic layer contains the core entities of the HBnB application. These entities are implemented as Python classes in the `app/models/` directory.

### Entities

1. **BaseModel**: The base class for all entities, providing common attributes and methods.
   - Attributes: id, created_at, updated_at
   - Methods: save(), update(), to_dict()

2. **User**: Represents a user of the HBnB application.
   - Attributes: first_name, last_name, email, is_admin
   - Methods: validate()

3. **Place**: Represents a place that can be rented.
   - Attributes: title, description, price, latitude, longitude, owner, reviews, amenities
   - Methods: validate(), add_review(), add_amenity()

4. **Review**: Represents a review for a place.
   - Attributes: text, rating, place, user
   - Methods: validate()

5. **Amenity**: Represents an amenity that a place can have.
   - Attributes: name
   - Methods: validate()

Each entity class inherits from the BaseModel class and implements its own validation logic and specific methods. The relationships between entities (e.g., User owning Places, Places having Reviews and Amenities) are represented through object references.

### Validation

Each model includes robust validation:

- **User**: Validates first name, last name (1-50 characters), and email format.
- **Place**: Validates title (1-100 characters), description (max 1000 characters), price (positive number), latitude (-90 to 90), longitude (-180 to 180), and owner (must be a User instance).
- **Review**: Validates text (required, max 1000 characters), rating (integer 1-5), and associations with Place and User.
- **Amenity**: Validates name (1-50 characters).

### Unit Tests

Comprehensive unit tests have been implemented for each model, covering:

- Valid object creation
- Invalid attribute values
- Updating objects
- Converting objects to dictionaries

This structure allows for easy manipulation of data and enforcement of business rules within the application.

## 🤝 Contributing

We welcome contributions to the HBnB project! If you'd like to contribute, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and commit them with clear, descriptive messages
4. Push your changes to your fork
5. Create a pull request to the main repository

Please ensure that your code adheres to the project's coding standards and is well-documented. Also, make sure to update or add tests as necessary.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👥 Authors

<li> Adrien MENDES RAMOS - <a href="https://github.com/Saynez667">@Saynez667</a></li>
<li> Benjamin RISTORD - <a href="https://github.com/jbn179">@jbn179</a></li>

