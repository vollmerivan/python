from datetime import datetime

date_now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

EVENT_DATA_SET = {
    "description": "изенение описание мероприятия для автотеста методом пут",
    "responsibleMail": "engineer@krit.pro",
    "plan": date_now,
    "status": {
        "id": 2}
}

EVENT_DATA_GET = {
    "description": "изменение назначеного методом патч ",

    "responsibleMail": "ivan.folmer@krit.pro",
    "plan": date_now,
    "status": {
        "id": 2},
    "comment": "описание комментария автотест"
}

EVENT_DATA = {"description": "мероприятие создано через автотест", "responsibleMail": "engineer@krit.pro",
              "plan": date_now, "status": {"id": 2}
              }

EVENT_DATA_APPROVED = {'status': {'id': 5}}

EVENT_DATA_CLOSED = {'closed': date_now,
                     'comment': "Мероприятие выполнено",
                     'status': {'id': 3}
                     }
