# Melp Restaurants API

This project provides a REST API for managing restaurant data and retrieving statistics about restaurants within a specified radius. The API is built using Flask, Flask-RESTful, SQLAlchemy, and Flasgger for API documentation.

# Deployed Server

The API is live and can be accessed at: [Melp Restaurants API](https://intelimetrica-test.onrender.com/apidocs/)

https://intelimetrica-test.onrender.com/apidocs/


## Features

- **CRUD Operations**: Create, Read, Update, and Delete restaurant data.
- **Statistics Endpoint**: Retrieve statistics (count, average rating, standard deviation) for restaurants within a specified radius.
- **Swagger Documentation**: Interactive API documentation with Swagger UI.

## Getting Started

### Prerequisites to run locally

Make sure you have the following installed:

- Python 3.7+
- pip (Python package installer)

### Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/carlos-rsalda/Intelimetrica-Test.git
   ```
2. **Create a virtual environment** :

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install the dependencies** :

   ```sh
   pip install -r requirements.txt
   ```
4. **Set up the database and run the server** :

   ```sh
   python run.py
   ```

**Access the API documentation** :

Open your browser and navigate to `http://127.0.0.1:5000/apidocs/` to view and interact with the API documentation.


### Endpoints

#### 1. Create a Restaurant (POST)

* **URL** : `http://127.0.0.1:5000/restaurants`
* **Method** : `POST`
* **Body** :
* ```
  {
    "rating": 5,
    "name": "Restaurant A Updated",
    "site": "http://exampleupdated.com",
    "email": "contact@updated.com",
    "phone": "987654321",
    "street": "456 Updated St",
    "city": "Updated City",
    "state": "Updated State",
    "lat": 23.45,
    "lng": 67.89
  }

  ```

#### 2. Get All Restaurants (GET)

* **URL** : `http://127.0.0.1:5000/restaurants`
* **Method** : `GET`

#### 3. Get a Restaurant by ID (GET)

* **URL** : `http://127.0.0.1:5000/restaurants/{id}`
* **Method** : `GET`
* **Example** : `http://127.0.0.1:5000/restaurants/1`

#### 4. Update a Restaurant (PUT)

* **URL** : `http://127.0.0.1:5000/restaurants/{id}`
* **Method** : `PUT`
* **Body** :
* ```
  {
    "rating": 5,
    "name": "Restaurant A Updated",
    "site": "http://exampleupdated.com",
    "email": "contact@updated.com",
    "phone": "987654321",
    "street": "456 Updated St",
    "city": "Updated City",
    "state": "Updated State",
    "lat": 23.45,
    "lng": 67.89
  }

  ```


  `</code></div>``</div></pre>`

#### 5. Delete a Restaurant (DELETE)

* **URL** : `http://127.0.0.1:5000/restaurants/{id}`
* **Method** : `DELETE`
* **Example** : `http://127.0.0.1:5000/restaurants/1`

#### 6. Get Restaurant Statistics (GET)

* **URL** : `http://127.0.0.1:5000/restaurants/statistics?latitude={latitude}&longitude={longitude}&radius={radius}`
* **Method** : `GET`
* **Example** : `http://127.0.0.1:5000/restaurants/statistics?latitude=19.44&longitude=-99.12&radius=500`

`
