import os
from pathlib import Path
from django.core.wsgi import get_wsgi_application


def load_env():
    env_path = Path(__file__).resolve().parent.parent / '.env'
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, _, value = line.partition('=')
                os.environ.setdefault(key.strip(), value.strip())


load_env()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diemap_project.settings')
application = get_wsgi_application()
