#MySQL 데이터베이스를 사용하기 위해 settings.py를 커스터마이징 합니다.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'algo_db',
        'USER': 'root',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

#기존 settings.py의 secret_key입니다.
SECRET_KEY = "django-insecure-h_z2qeq_m*e7h8rqpz3c%q)42)#ae!f=ah3-*wxd*woh=y%zep"