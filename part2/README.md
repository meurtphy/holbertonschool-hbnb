# hbnb Project

## Overview
The hbnb project is a web application built using Flask that provides a RESTful API for managing users, places, reviews, and amenities. This project is structured to separate concerns into different modules, making it easier to maintain and extend.

## Project Structure
```
part2
├── app
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── v1
│   │       ├── __init__.py
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       ├── amenities.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   ├── amenity.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── facade.py
│   ├── persistence
│       ├── __init__.py
│       ├── repository.py
├── run.py
├── config.py
├── requirements.txt
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/hbnb.git
   cd hbnb
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command:
```
python run.py
```
The server will start, and you can access the API at `http://localhost:5000/api/v1/`.

## API Endpoints
- **Users**: Manage user accounts and authentication.
- **Places**: Manage places and their details.
- **Reviews**: Manage reviews for places.
- **Amenities**: Manage amenities associated with places.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.