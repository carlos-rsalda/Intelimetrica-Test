from . import db

class Restaurant(db.Model):
    id = db.Column(db.String, primary_key=True)
    rating = db.Column(db.Integer)
    name = db.Column(db.String)
    site = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)
    street = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)

    def to_dict(self):
        return {
            'id': self.id,
            'rating': self.rating,
            'name': self.name,
            'site': self.site,
            'email': self.email,
            'phone': self.phone,
            'street': self.street,
            'city': self.city,
            'state': self.state,
            'lat': self.lat,
            'lng': self.lng
        }
