from flask import request, jsonify
from . import db
from .models import Restaurant
from app import create_app
from flasgger import Swagger, swag_from

app = create_app()

print("Inicio de la definición de rutas")

@app.route('/')
def home():
    print("Ruta '/' registrada")
    return "Welcome to the Melp Restaurants API!"

@app.route('/restaurants', methods=['POST'])
@swag_from({
    'tags': ['restaurants'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'string'},
                    'rating': {'type': 'integer'},
                    'name': {'type': 'string'},
                    'site': {'type': 'string'},
                    'email': {'type': 'string'},
                    'phone': {'type': 'string'},
                    'street': {'type': 'string'},
                    'city': {'type': 'string'},
                    'state': {'type': 'string'},
                    'lat': {'type': 'number', 'format': 'float'},
                    'lng': {'type': 'number', 'format': 'float'}
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Restaurant created successfully'
        }
    }
})
def create_restaurant():
    print("Ruta '/restaurants' [POST] registrada")
    data = request.get_json()
    new_restaurant = Restaurant(**data)
    db.session.add(new_restaurant)
    db.session.commit()
    return jsonify({'message': 'Restaurant created successfully'}), 201

@app.route('/restaurants', methods=['GET'])
@swag_from({
    'tags': ['restaurants'],
    'responses': {
        200: {
            'description': 'A list of restaurants',
            'schema': {
                'type': 'array',
                'items': {
                    'properties': {
                        'id': {'type': 'string'},
                        'rating': {'type': 'integer'},
                        'name': {'type': 'string'},
                        'site': {'type': 'string'},
                        'email': {'type': 'string'},
                        'phone': {'type': 'string'},
                        'street': {'type': 'string'},
                        'city': {'type': 'string'},
                        'state': {'type': 'string'},
                        'lat': {'type': 'number', 'format': 'float'},
                        'lng': {'type': 'number', 'format': 'float'}
                    }
                }
            }
        }
    }
})
def get_restaurants():
    print("Ruta '/restaurants' [GET] registrada")
    restaurants = Restaurant.query.all()
    return jsonify([restaurant.to_dict() for restaurant in restaurants])

@app.route('/restaurants/<id>', methods=['GET'])
@swag_from({
    'tags': ['restaurants'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'string',
            'required': True
        }
    ],
    'responses': {
        200: {
            'description': 'Restaurant details',
            'schema': {
                'properties': {
                    'id': {'type': 'string'},
                    'rating': {'type': 'integer'},
                    'name': {'type': 'string'},
                    'site': {'type': 'string'},
                    'email': {'type': 'string'},
                    'phone': {'type': 'string'},
                    'street': {'type': 'string'},
                    'city': {'type': 'string'},
                    'state': {'type': 'string'},
                    'lat': {'type': 'number', 'format': 'float'},
                    'lng': {'type': 'number', 'format': 'float'}
                }
            }
        },
        404: {
            'description': 'Restaurant not found'
        }
    }
})
def get_restaurant(id):
    print(f"Ruta '/restaurants/<id>' [GET] registrada")
    restaurant = Restaurant.query.get_or_404(id)
    return jsonify(restaurant.to_dict())

@app.route('/restaurants/<id>', methods=['PUT'])
@swag_from({
    'tags': ['restaurants'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'string',
            'required': True
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'rating': {'type': 'integer'},
                    'name': {'type': 'string'},
                    'site': {'type': 'string'},
                    'email': {'type': 'string'},
                    'phone': {'type': 'string'},
                    'street': {'type': 'string'},
                    'city': {'type': 'string'},
                    'state': {'type': 'string'},
                    'lat': {'type': 'number', 'format': 'float'},
                    'lng': {'type': 'number', 'format': 'float'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Restaurant updated successfully'
        },
        404: {
            'description': 'Restaurant not found'
        }
    }
})
def update_restaurant(id):
    print(f"Ruta '/restaurants/<id>' [PUT] registrada")
    data = request.get_json()
    restaurant = Restaurant.query.get_or_404(id)
    for key, value in data.items():
        setattr(restaurant, key, value)
    db.session.commit()
    return jsonify({'message': 'Restaurant updated successfully'})

@app.route('/restaurants/<id>', methods=['DELETE'])
@swag_from({
    'tags': ['restaurants'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'string',
            'required': True
        }
    ],
    'responses': {
        200: {
            'description': 'Restaurant deleted successfully'
        },
        404: {
            'description': 'Restaurant not found'
        }
    }
})
def delete_restaurant(id):
    print(f"Ruta '/restaurants/<id>' [DELETE] registrada")
    restaurant = Restaurant.query.get_or_404(id)
    db.session.delete(restaurant)
    db.session.commit()
    return jsonify({'message': 'Restaurant deleted successfully'})

# Task 2: Statistics endpoint
@app.route('/restaurants/statistics', methods=['GET'])
@swag_from({
    'tags': ['statistics'],
    'parameters': [
        {
            'name': 'latitude',
            'in': 'query',
            'type': 'number',
            'required': True,
            'format': 'float'
        },
        {
            'name': 'longitude',
            'in': 'query',
            'type': 'number',
            'required': True,
            'format': 'float'
        },
        {
            'name': 'radius',
            'in': 'query',
            'type': 'number',
            'required': True,
            'format': 'float'
        }
    ],
    'responses': {
        200: {
            'description': 'Statistics of restaurants within the specified radius',
            'schema': {
                'properties': {
                    'count': {'type': 'integer'},
                    'avg': {'type': 'number', 'format': 'float'},
                    'std': {'type': 'number', 'format': 'float'}
                }
            }
        }
    }
})
def get_statistics():
    print("Ruta '/restaurants/statistics' [GET] registrada")
    lat = float(request.args.get('latitude'))
    lng = float(request.args.get('longitude'))
    radius = float(request.args.get('radius'))

    # Haversine formula to calculate distance in meters
    query = """
    SELECT *, (6371000 * acos(cos(radians(:lat)) * cos(radians(lat)) * cos(radians(lng) - radians(:lng)) + sin(radians(:lat)) * sin(radians(lat)))) AS distance
    FROM restaurant
    HAVING distance < :radius
    """

    results = db.session.execute(query, {'lat': lat, 'lng': lng, 'radius': radius}).fetchall()
    ratings = [result['rating'] for result in results]

    if ratings:
        avg = sum(ratings) / len(ratings)
        std = (sum([(x - avg) ** 2 for x in ratings]) / len(ratings)) ** 0.5
    else:
        avg = std = 0

    return jsonify({
        'count': len(ratings),
        'avg': avg,
        'std': std
    })

print("Fin de la definición de rutas")
