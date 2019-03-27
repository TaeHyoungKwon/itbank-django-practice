if ENV == 'development':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'web_db',  # DB명
            'USER': 'root',  # 데이터베이스 계정
            'PASSWORD': '',  # 계정 비밀번호
            'HOST': '127.0.0.1',  # 데이테베이스 주소(IP)
            'PORT': '3306',  # 데이터베이스 포트(보통은 3306)
        }

    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'web_db',  # DB명
            'USER': 'root',  # 데이터베이스 계정
            'PASSWORD': '',  # 계정 비밀번호
            'HOST': 'http://127.0.0.1',  # 데이테베이스 주소(IP)
            'PORT': '3306',  # 데이터베이스 포트(보통은 3306)
        }

    }
