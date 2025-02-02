import uuid

RISK_DATA = {
    "uniqueId": str(uuid.uuid4()),
    "description": "Создание риска через автотест",
    "category": {"id": 3},
    "place": {"id": 35},
    "priority": {"id": -1},
    "user": {"id": 3},
    "status": {"id": 1}
}