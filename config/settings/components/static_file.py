# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
# 정적파일이 위치한 경로들을 지정하는 설정 항목
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
