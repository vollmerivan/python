

risk_id = 572     #  194 препрод, 572 дев
user_id = 178     # 70/178 айди поьзователя из препрод/dev engineer@krit.pro

AUTH_ENDPOINT: str = "api/v1/auth/SignIn"

USER_ENDPOINT = "api/v1/users"
USERS_ME_ENDPOINT = "api/v1/users/me"
USERS_MANAGED_ENDPOINT = "api/v1/users/managed"
ROLES_ENDPOINT = "api/v1/roles"
ROLES_POST_ENDPOINT = "api/v1/users/{user_id}/roles"

PLACES_ENDPOINT = "api/v1/places"
PLACES_MINE_ENDPOINT = "api/v1/places/mine"

PRIORITIES_ENDPOINT = "api/v1/priorities"
ORG_ENDPOINT = "api/v1/organizations"
STATISTICS_MINE_ENDPOINT = "api/v1/statistics/mine"
RATING_ENDPOINT = "api/v1/rating"

CATEGORIES_ENDPOINT = "api/v1/categories"
CATEGORIES_MINE_ENDPOINT = "api/v1/categories/mine"

TASKS_ENDPOINT = "api/v1/tasks"
BADGES_ENDPOINT = "api/v1/badges"
SEASONS_ENDPOINT = "api/v1/seasons"
SEASONS_MINE_ENDPOINT = "api/v1/seasons/mine"

RISKS_ENDPOINT = "api/v1/risks"
RISKS_MINE_ENDPOINT = "api/v1/risks/mine"
RISKS_STATUS_RU_ENDPOINT = "api/v1/risk-statuses?culture=ru"
RISKS_STATUS_EN_ENDPOINT = "api/v1/risk-statuses"
RISKS_ID_ENDPOINT = "api/v1/risks/{risk_id}"
RISKS_ID_EVENT_ENDPOINT = "api/v1/risks/{risk_id}/events"
RISKS_ID_HISTORY = "api/v1/risks/{risk_id}/history"
RISKS_EXPORT_ENDPOINT = "api/v1/risks"


TIMEZONE_ENDPOINT = "api/v1/settings/timezones"
PROPERTIES_ENDPOINT = "api/v1/organizations/mine/properties"


EVENTS_ENDPOINT = "api/v1/events"
EVENTS_STATUS_RU_ENDPOINT = "api/v1/event-statuses?culture=ru"
EVENTS_STATUS_EN_ENDPOINT = "api/v1/event-statuses?culture=en"



Admin_AUTH_ENDPOINT = "admin/api/v1/auth/SignIn"
Admin_ORG_ENDPOINT = "admin/api/v1/organizations"
Admin_USER_ENDPOINT = "admin/api/v1/users"
Admin_USER_patch_ENDPOINT = "admin/api/v1/users/user_id"
Admin_role_ENDPOINT = "admin/api/v1/users/user_id/roles"