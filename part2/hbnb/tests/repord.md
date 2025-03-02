Documentation du Processus de Test de l'API HBnB

1. Introduction

Cette documentation décrit le processus de test de l'API HBnB, en mettant en avant les cas de succès et les cas limites correctement gérés. Les tests ont été réalisés en utilisant un script Bash automatisé avec cURL et jq pour interagir avec l'API et valider les réponses.

Les tests couvrent les fonctionnalités CRUD (Create, Read, Update, Delete) des entités Utilisateurs (Users), Commodités (Amenities), Lieux (Places) et Avis (Reviews).

En complément des tests automatisés, nous avons utilisé Swagger UI pour valider manuellement les endpoints et vérifier la documentation de l’API.

2. Objectifs des Tests

Les tests visent à garantir que :

L’API fonctionne comme attendu pour toutes les actions CRUD.

Les validations des entrées utilisateur sont bien mises en place.

Les erreurs sont correctement gérées (ex : valeurs invalides, ID inexistant).

Les relations entre entités (ex : un place contient bien ses amenities et reviews) sont respectées.

L’API est sécurisée contre les manipulations incorrectes (ex : empêcher les actions non autorisées).

La documentation Swagger est bien générée et décrit fidèlement les fonctionnalités de l’API.

3. Environnement de Test

Serveur API : Flask-RESTx

Outil de test : cURL et jq

Base de données : SQLite/PostgreSQL (selon l’environnement)

Méthodes de test :

Tests unitaires via pytest et unittest

Tests manuels via Swagger UI

Tests automatisés via un script Bash

4. Utilisation de Swagger pour les Tests Manuels

Swagger UI a été utilisé pour tester visuellement et interagir avec l’API. Il permet de :

Explorer tous les endpoints disponibles.

Envoyer des requêtes API directement via l’interface web.

Visualiser les schémas de données et les formats attendus.

Vérifier les réponses et identifier les erreurs en temps réel.

Accéder à Swagger

Swagger est accessible à l'URL suivante lorsque l’API est en cours d’exécution :

http://127.0.0.1:5000/api/v1/

Vérifications effectuées avec Swagger

Endpoint

Vérifications

/users

Création, récupération, mise à jour et suppression des utilisateurs.

/amenities

Ajout et récupération des commodités.

/places

Vérification des relations entre lieux et commodités.

/reviews

Validation des avis et affichage des notes moyennes des lieux.

5. Exemples de Requêtes cURL pour Tester l'API

Création d’un utilisateur valide

curl -X POST "http://127.0.0.1:5000/api/v1/users/" -H "Content-Type: application/json" -d '{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com"
}'

Réponse attendue :

{
    "id": "uuid",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com"
}

Création d’un utilisateur avec un email déjà existant

curl -X POST "http://127.0.0.1:5000/api/v1/users/" -H "Content-Type: application/json" -d '{
    "first_name": "Jane",
    "last_name": "Smith",
    "email": "john.doe@example.com"
}'

Réponse attendue :

{
    "error": "Email already registered"
}

Récupération de la liste des utilisateurs

curl -X GET "http://127.0.0.1:5000/api/v1/users/" -H "accept: application/json"

Mise à jour d’un utilisateur

curl -X PUT "http://127.0.0.1:5000/api/v1/users/{user_id}" -H "Content-Type: application/json" -d '{
    "first_name": "John-Updated",
    "last_name": "Doe-Updated",
    "email": "john.updated@example.com"
}'

6. Résumé des Résultats

📌 Module testé

✅ Succès

❌ Échecs

📋 Commentaires

Utilisateurs (/users)

10/10

0

Création, récupération, mise à jour et suppression réussies.

Amenities (/amenities)

9/9

0

Détection des erreurs réussie (nom manquant, ID inexistant).

Places (/places)

9/9

0

Vérification des erreurs (propriétaire invalide, prix négatif, latitude incorrecte).

Reviews (/reviews)

14/14

0

Bonne gestion des erreurs, suppression confirmée, données mises à jour correctement.

✅ Taux de succès global : 100% (42 tests réussis sur 42).

7. Améliorations et Pistes Futures

Bien que les tests montrent que l’API fonctionne correctement, quelques optimisations peuvent être envisagées :

Tests de performance : Vérifier le temps de réponse des endpoints.

Tests de charge : Vérifier la capacité de l’API sous forte utilisation.

Tests de sécurité : Vérifier les accès avec des utilisateurs non autorisés.

Automatisation des tests Swagger : Générer automatiquement des requêtes à partir de la documentation.

🚀 L’API est prête pour le déploiement avec une excellente stabilité et robustesse !

