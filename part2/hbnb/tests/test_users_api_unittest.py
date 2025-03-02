import unittest
import requests

BASE_URL = "http://localhost:5000/api/v1"
USER_ENDPOINT = f"{BASE_URL}/users"
AMENITY_ENDPOINT = f"{BASE_URL}/amenities"
PLACE_ENDPOINT = f"{BASE_URL}/places"
REVIEW_ENDPOINT = f"{BASE_URL}/reviews"

class TestHbnbAPI(unittest.TestCase):
    def setUp(self):
        """Préparation des tests: suppression des anciens utilisateurs si nécessaire."""
        self.session = requests.Session()

    def test_1_create_user(self):
        """Test de création d'un utilisateur valide."""
        payload = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com"
        }
        response = self.session.post(USER_ENDPOINT, json=payload)
        self.assertEqual(response.status_code, 201)
        self.user_id = response.json().get("id")
        self.assertIsNotNone(self.user_id)

    def test_2_create_duplicate_user(self):
        """Test de création d'un utilisateur avec un email existant."""
        payload = {
            "first_name": "Jane",
            "last_name": "Smith",
            "email": "john.doe@example.com"
        }
        response = self.session.post(USER_ENDPOINT, json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("Email already registered", response.text)

    def test_3_create_user_invalid_data(self):
        """Test de création d'un utilisateur avec données invalides."""
        payload = {
            "last_name": "Doe",
            "email": "invalid_user@example.com"
        }
        response = self.session.post(USER_ENDPOINT, json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.text)

    def test_4_get_all_users(self):
        """Test de récupération de tous les utilisateurs."""
        response = self.session.get(USER_ENDPOINT)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)

    def test_5_get_user_by_id(self):
        """Test de récupération d'un utilisateur par ID."""
        response = self.session.get(f"{USER_ENDPOINT}/{self.user_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("id"), self.user_id)

    def test_6_get_user_invalid_id(self):
        """Test de récupération d'un utilisateur avec un ID inexistant."""
        response = self.session.get(f"{USER_ENDPOINT}/invalid_id_12345")
        self.assertEqual(response.status_code, 404)
        self.assertIn("not found", response.text)

    def test_7_update_user(self):
        """Test de mise à jour d'un utilisateur."""
        payload = {
            "first_name": "John-Updated",
            "last_name": "Doe-Updated",
            "email": "john.updated@example.com"
        }
        response = self.session.put(f"{USER_ENDPOINT}/{self.user_id}", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("first_name"), "John-Updated")

    def test_8_update_user_invalid_id(self):
        """Test de mise à jour d'un utilisateur avec un ID inexistant."""
        payload = {
            "first_name": "Invalid",
            "last_name": "User",
            "email": "invalid@example.com"
        }
        response = self.session.put(f"{USER_ENDPOINT}/invalid_id_12345", json=payload)
        self.assertEqual(response.status_code, 404)
        self.assertIn("not found", response.text)

    def test_9_delete_user(self):
        """Test de suppression d'un utilisateur."""
        response = self.session.delete(f"{USER_ENDPOINT}/{self.user_id}")
        self.assertEqual(response.status_code, 200)
        self.assertIn("successfully", response.text)

    def test_10_delete_user_invalid_id(self):
        """Test de suppression d'un utilisateur avec un ID inexistant."""
        response = self.session.delete(f"{USER_ENDPOINT}/invalid_id_12345")
        self.assertEqual(response.status_code, 404)
        self.assertIn("not found", response.text)

if __name__ == "__main__":
    unittest.main()
