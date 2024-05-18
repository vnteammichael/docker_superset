# Cấu hình database URI
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://data:sh2vfaKW89uH@mysql:3307/data_warehouse?charset=utf8mb4"

# Cấu hình cho phép embedding dashboard
ENABLE_JWT_COOKIE_AUTHENTICATION = True
SESSION_COOKIE_SAMESITE = 'None'  # Cho phép cookie trên các trang khác nhau
SESSION_COOKIE_SECURE = True      # Bảo đảm sử dụng HTTPS
SESSION_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SECURE = True
ENABLE_PROXY_FIX = True

SECRET_KEY = 'bvvEF+5qFxABJk1CB1u2IpWouEpRywCI6ew5UVXme9sLACcNn9uLlZuS'

CORS_OPTIONS = {
'supports_credentials': True,
'allow_headers': ['*'],
'resources': ['*'],
'origins': ['*']
}
FEATURE_FLAGS = {
    "DYNAMIC_PLUGINS": True,
    "ALERTS_ATTACH_REPORTS": True,
    "DASHBOARD_RBAC": True,
    "EMBEDDABLE_CHARTS": True,
    "EMBEDDED_SUPERSET": True,
    "ENABLE_TEMPLATE_PROCESSING": True,
    "LISTVIEWS_DEFAULT_CARD_VIEW": True,
    "SCHEDULED_QUERIES": True,
    "SQL_VALIDATORS_BY_ENGINE": True,
    "THUMBNAILS": True
}

from flask_appbuilder.security.manager import AUTH_DB
AUTH_TYPE = AUTH_DB
AUTH_ROLE_ADMIN = 'Admin'
AUTH_USER_REGISTRATION = False