from flask import Blueprint, request, jsonify
from app.models import db, Detection, Weather

raspi_bp = Blueprint("raspi", __name__)

@raspi_bp.route("/report", methods=["POST"])
def report():
    data = request.get_json()

    # 유효성 검사
    timestamp = data.get("time")
    if not timestamp:
        return jsonify({"error": "Missing 'time' field"}), 400

    # 고정된 location_id
    location_id = 1

    # 가장 최근 weather_id (없을 수도 있음)
    weather = Weather.query.order_by(Weather.timestamp.desc()).first()
    weather_id = weather.weather_id if weather else None

    # 감지 기록 저장
    detection = Detection(
        timestamp=timestamp,
        location_id=location_id,
        weather_id=weather_id
    )

    db.session.add(detection)
    db.session.commit()

    return jsonify({
        "message": "saved",
        "id": detection.detection_id  # 자동 생성된 id 반환
    }), 201
