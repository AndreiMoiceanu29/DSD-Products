from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '{{secret_key}}'


DATABASES = {
    'mongodb': {
        'USER': '{{database_user}}',
        'PASSWORD': '{{database_pass}}',
        'HOST': '{{internal_docker_ip}}',
        'PORT': '{{database_port}}'
    }
}
