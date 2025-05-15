# test_api.py
from app import create_app
from app.models import db, Detection, Location, Weather

app = create_app()

with app.app_context():
    detections = Detection.query.all()
    print(f"✅ 감지된 데이터 수: {len(detections)}")

    for d in detections:
        print({
            "id": d.detection_id,
            "timestamp": d.timestamp,
            "location": d.location.name if d.location else None,
            "weather": {
                "sky": d.weather.sky_status if d.weather else None,
                "pty": d.weather.pty_status if d.weather else None
            }
        })

    print("\n📍 Location 목록:")
    for loc in Location.query.all():
        print(f"{loc.location_id}: {loc.name} ({loc.latitude}, {loc.longitude})")

    print("\n☁️ Weather 목록:")
    for w in Weather.query.all():
        print(f"{w.weather_id}: {w.timestamp} | {w.sky_status} / {w.pty_status}")
