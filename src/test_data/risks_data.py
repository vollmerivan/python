import uuid

RISK_DATA = {
    "uniqueId": str(uuid.uuid4()),
    "description": "Создание риска через автотест",
    "category": {"id": 5},
    "place": {"id": 52},
    "priority": {"id": -1},
    "user": {"id": 239},
    "status": {"id": 1}
}

RISK_DATA_APPROVED = {'status': {'id': 2}, 'priority': {'id': 4}}
RISK_DATA_DEVATION = {'status': {'id': 3}, 'comment': "Отклонение риска"}
RISK_DATA_WORK = {'status': {'id': 4}}
RISK_DATA_CLOSED = {'status': {'id': 5}, 'comment': "Закрытие риска"}