import random
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class UsersData:
    email: str
    password: str


SUPER_USER = UsersData(email="office@krit.pro", password="super")
DATA_HUNTER = UsersData(email="huntertest@krit.pro", password="super")
DATA_RM_PREPROD = UsersData(email="rmtest2@krit.pro", password="super")
DATA_ADMIN_PREPROD = UsersData(email="admintest@krit.pro", password="super")
DATA_ENGINEER_PREPROD = UsersData(email="engineer@krit.pro", password="super")

# Не валидные PrePROD
INVALID_PASS = UsersData(email="rmtest2@krit.pro", password="1233")
INVALID_LOGIN = UsersData(email="1231@krit.pro", password="super")
INVALID_LOGIN_PASS = UsersData(email="1231@krit.pro", password="1213")
INVALID_EMPTY = UsersData(email="", password="")
INVALID_EMPTY_PASS = UsersData(email="rmtest2@krit.pro", password="")
INVALID_EMPTY_LOGIN = UsersData(email="", password="super")

# Пользователи DEV
DATA_RM = UsersData(email="123@krit.pro", password="123")
DATA_ADMIN = UsersData(email="admin@krit.pro", password="admin")
DATA_HUNTER = UsersData(email="ivan.folmer@krit.pro", password="123")

password_data = {"password": "super"}
role_admin_data = {"id": 4}
role_rm_data = {"id": 3}

USER_DATA = {
    "name": f"User{random.randint(1, 999)}",
    "email": f"user{datetime.now().strftime('%m%d%y%H%M')}@krit.pro",
    "isActive": True
}

USER_DATA_SUPER = {
    "name": f"User{random.randint(1, 999)}",
    "email": f"user{datetime.now().strftime('%m%d%y%H%M')}@krit.pro",
    "isActive": True,
    "organization": {"id": 1}
}
