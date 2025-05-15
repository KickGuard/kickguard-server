from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Location(db.Model):
    __tablename__ = 'location'

    location_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    detections = db.relationship("Detection", back_populates="location")


class Weather(db.Model):
    __tablename__ = 'weather'

    weather_id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String)
    sky_status = db.Column(db.String)
    pty_status = db.Column(db.String)

    detections = db.relationship("Detection", back_populates="weather")


class Detection(db.Model):
    __tablename__ = 'detection'

    detection_id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey("location.location_id"))
    weather_id = db.Column(db.Integer, db.ForeignKey("weather.weather_id"))
    timestamp = db.Column(db.String)  # 감지 시각

    location = db.relationship("Location", back_populates="detections")
    weather = db.relationship("Weather", back_populates="detections")
