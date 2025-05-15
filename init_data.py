from app import create_app
from app.models import db, Location

app = create_app()

with app.app_context():
    locations = [
        {"name": "Seoul Station", "latitude": 37.5563, "longitude": 126.9723},
        {"name": "Gangnam", "latitude": 37.4979, "longitude": 127.0276},
        {"name": "Hongdae", "latitude": 37.5560, "longitude": 126.9235},
    ]

    for loc in locations:
        if not Location.query.filter_by(name=loc["name"]).first():
            db.session.add(Location(**loc))

    db.session.commit()
    print("✅ Location 데이터 삽입 완료")
