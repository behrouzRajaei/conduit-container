import os

from pathlib import Path

# --- Base Directory ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Secret & Debug ---
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "unsafe-dev-key")
DEBUG = os.environ.get("DJANGO_DEBUG", "False").lower() == "true"

# --- Allowed Hosts ---
ALLOWED_HOSTS = [
  host.strip()
  for host in os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(",") if host.strip()
]

# --- Installed Apps ---
INSTALLED_APPS = [
  "django.contrib.admin",
  "django.contrib.auth",
  "django.contrib.contenttypes",
  "django.contrib.sessions",
  "django.contrib.messages",
  "django.contrib.staticfiles",

  "rest_framework",

  "conduit.apps.articles",
  "conduit.apps.authentication",
  "conduit.apps.profiles",
  "conduit.apps.core",
]

# --- Middleware ---
MIDDLEWARE = [
  "corsheaders.middleware.CorsMiddleware",
  "django.middleware.security.SecurityMiddleware",
  "django.contrib.sessions.middleware.SessionMiddleware",
  "django.middleware.common.CommonMiddleware",
  "django.contrib.auth.middleware.AuthenticationMiddleware",
  "django.contrib.messages.middleware.MessageMiddleware",
  "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# --- URLs & WSGI ---
ROOT_URLCONF = "conduit.urls"
WSGI_APPLICATION = "conduit.wsgi.application"

# --- Database ---
DATABASES = {
  "default": {
    "ENGINE": "django.db.backends.postgresql",
    "NAME": os.environ.get("POSTGRES_DB", "conduit_db"),
    "USER": os.environ.get("POSTGRES_USER", "postgres"),
    "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "changeme"),
    "HOST": os.environ.get("DB_HOST", "db"),
    "PORT": os.environ.get("DB_PORT", "5432"),
  }
}

# --- Static Files ---
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# --- REST Framework ---
REST_FRAMEWORK = {
  "DEFAULT_RENDERER_CLASSES": ( "rest_framework.renderers.JSONRenderer", ),
  "DEFAULT_AUTHENTICATION_CLASSES": ( "rest_framework.authentication.TokenAuthentication", ),
}
