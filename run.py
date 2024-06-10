import os
from app import create_app, db
from app.models import Restaurant
import pandas as pd

app = create_app()

def load_data():
    if not Restaurant.query.first():
        df = pd.read_csv('restaurants.csv')
        for _, row in df.iterrows():
            restaurant = Restaurant(
                id=row['id'],
                rating=row['rating'],
                name=row['name'],
                site=row['site'],
                email=row['email'],
                phone=row['phone'],
                street=row['street'],
                city=row['city'],
                state=row['state'],
                lat=row['lat'],
                lng=row['lng']
            )
            db.session.add(restaurant)
        db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        load_data()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
