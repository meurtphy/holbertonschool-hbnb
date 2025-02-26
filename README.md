# 🏠 HBnB Application

- [🏠 HBnB Application](#-hbnb-application)
  - [📁 Project Structure](#-project-structure)
    - [📚 Directory and File Descriptions](#-directory-and-file-descriptions)
  - [🚀 Installation and Setup](#-installation-and-setup)
  - [▶️ Running the Application](#️-running-the-application)
  - [🧪 Running Tests](#-running-tests)
  - [📖 API Documentation](#-api-documentation)
  - [🧠 Business Logic Layer](#-business-logic-layer)
    - [Entities](#entities)
    - [Validation](#validation)
    - [Unit Tests](#unit-tests)
  - [👥 Authors](#-authors)

This is the HBnB (AirBnB clone) application, a RESTful API for managing users, places, reviews, and amenities.

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

## 🚀 Installation and Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd holbertonschool-hbnb/part2/task6
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

To run the application, use the following commands:

```bash
export PYTHONPATH="/path/to/project/root:$PYTHONPATH"
python3 run.py
```

The application will start, and you can access the API at `http://localhost:5000`.

## 🧪 Running Tests

To run the unit tests, use the following commands:

```bash
export PYTHONPATH="/path/to/project/root:$PYTHONPATH"
python3 -m unittest discover tests -v
```

## 📖 API Documentation

API documentation will be available at `http://localhost:5000/api/v1/` when the application is running.

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

## 👥 Authors

<li> Adrien MENDES RAMOS - <a href="https://github.com/Saynez667">@Saynez667</a></li>
<li> Benjamin RISTORD - <a href="https://github.com/jbn179">@jbn179</a></li>
<li> Mina SINANI - <a href="https://github.com/MINS2405">@MINS2405</a></li>
