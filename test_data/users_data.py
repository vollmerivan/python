import random
from datetime import datetime

# Пользователи PrePROD
superuser = {"email": "office@krit.pro", "password": "super"}

data_rm_preprod = {"email": "rmtest2@krit.pro", "password": "super"}
data_hunter_preprod = {"email": "huntertest@krit.pro", "password": "super"}
data_admin_preprod = {"email": "admintest@krit.pro", "password": "super"}
data_engineer_preprod = {"email": "engineer@krit.pro", "password": "super"}

# Не валидные PrePROD
invalid_pass = {"email": "rmtest2@krit.pro", "password": "1233"}
invalid_login = {"email": "1231@krit.pro", "password": "super"}
invalid_login_pass = {"email": "1231@krit.pro", "password": "1213"}
invalid_empty = {"email": "", "password": ""}
invalid_empty_pass = {"email": "rmtest2@krit.pro", "password": ""}
invalid_empty_login = {"email": "", "password": "super"}


# Пользователи DEV
data_rm = {"email": "123@krit.pro", "password": "123"}
data_admin = {"email": "admin@krit.pro", "password": "admin"}
data_hunter = {"email": "ivan.folmer@krit.pro","password": "123"}


password_data = {"password": "super"}
role_admin_data = {"id": 4}
role_rm_data = {"id": 3}