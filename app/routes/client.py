from flask import Blueprint, jsonify
from app.models import Detection, Location, Weather

client_bp = Blueprint("client", __name__)

@client_bp.route("/logs", methods=["GET"])
def get_logs():
    # 모든 Detection을 시간순으로 가져오기 (최신순)
    detections = Detection.query.order_by(Detection.timestamp.desc()).all()

    # 결과 JSON 변환
    result = []
    for d in detections:
        result.append({
            "id": d.detection_id,
            "timestamp": d.timestamp,
            "location": d.location.name if d.location else None,
            "weather": {
                "sky": d.weather.sky_status if d.weather else None,
                "pty": d.weather.pty_status if d.weather else None
            }
        })

    return jsonify(result)
