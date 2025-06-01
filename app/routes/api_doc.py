from flask import Blueprint
from flask_restx import Api, Resource, fields
from app.models import db, Detection, Location, Weather

api_bp = Blueprint("api", __name__)
api = Api(api_bp, version='1.0', title='KickGuard API',
          description='킥보드 인도 주행 감지 시스템 API 문서',
          doc='/docs')

detection_model = api.model('Detection', {
    'timestamp': fields.String(required=True, description='감지 시각'),
    'location_id': fields.Integer(required=True),
    'weather_id': fields.Integer(required=True)
})

@api.route('/detection')
class DetectionResource(Resource):
    def get(self):
        """모든 감지 데이터 조회"""
        detections = Detection.query.all()
        result = [
            {
                "detection_id": d.detection_id,
                "timestamp": d.timestamp,
                "location_id": d.location_id,
                "weather_id": d.weather_id
            } for d in detections
        ]
        return result, 200

    @api.expect(detection_model)
    def post(self):
        """감지 데이터 추가"""
        data = api.payload

        detection = Detection(
            timestamp=data["timestamp"],
            location_id=data["location_id"],
            weather_id=data["weather_id"]
        )
        db.session.add(detection)
        db.session.commit()

        return {
            "message": "감지 추가 완료",
            "id": detection.detection_id
        }, 201
