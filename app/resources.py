from flask_restful import Resource, reqparse
from flask import request
from app.models import Restaurant
from app import db
from flasgger import swag_from
from sqlalchemy import func

class RestaurantListResource(Resource):
    @swag_from('docs/restaurants_get.yml')
    def get(self):
        restaurants = Restaurant.query.all()
        return [restaurant.to_dict() for restaurant in restaurants], 200

    @swag_from('docs/restaurants_post.yml')
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', required=True, type=str)
        parser.add_argument('rating', required=True, type=int)
        parser.add_argument('name', required=True, type=str)
        parser.add_argument('site', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('phone', type=str)
        parser.add_argument('street', type=str)
        parser.add_argument('city', type=str)
        parser.add_argument('state', type=str)
        parser.add_argument('lat', type=float)
        parser.add_argument('lng', type=float)
        args = parser.parse_args()

        new_restaurant = Restaurant(**args)
        db.session.add(new_restaurant)
        db.session.commit()
        return new_restaurant.to_dict(), 201

class RestaurantResource(Resource):
    @swag_from('docs/restaurants_id_get.yml')
    def get(self, id):
        restaurant = Restaurant.query.get_or_404(id)
        return restaurant.to_dict(), 200

    @swag_from('docs/restaurants_id_put.yml')
    def put(self, id):
        restaurant = Restaurant.query.get_or_404(id)
        parser = reqparse.RequestParser()
        parser.add_argument('rating', type=int)
        parser.add_argument('name', type=str)
        parser.add_argument('site', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('phone', type=str)
        parser.add_argument('street', type=str)
        parser.add_argument('city', type=str)
        parser.add_argument('state', type=str)
        parser.add_argument('lat', type=float)
        parser.add_argument('lng', type=float)
        args = parser.parse_args()

        for key, value in args.items():
            if value is not None:
                setattr(restaurant, key, value)

        db.session.commit()
        return restaurant.to_dict(), 200

    @swag_from('docs/restaurants_id_delete.yml')
    def delete(self, id):
        restaurant = Restaurant.query.get_or_404(id)
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204

class RestaurantStatisticsResource(Resource):
    @swag_from('docs/restaurants_statistics_get.yml')
    def get(self):
        lat = float(request.args.get('latitude'))
        lng = float(request.args.get('longitude'))
        radius = float(request.args.get('radius'))

        distance_query = func.acos(
            func.cos(func.radians(lat)) * func.cos(func.radians(Restaurant.lat)) *
            func.cos(func.radians(Restaurant.lng) - func.radians(lng)) +
            func.sin(func.radians(lat)) * func.sin(func.radians(Restaurant.lat))
        ) * 6371000

        restaurants = Restaurant.query.with_entities(Restaurant.rating).filter(distance_query < radius).all()
        ratings = [r.rating for r in restaurants]

        if not ratings:
            return {'count': 0, 'avg': 0, 'std': 0}, 200

        avg = sum(ratings) / len(ratings)
        std = (sum((x - avg) ** 2 for x in ratings) / len(ratings)) ** 0.5
        return {'count': len(ratings), 'avg': avg, 'std': std}, 200

