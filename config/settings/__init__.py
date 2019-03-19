'''
__init__.py
'''
import os
import glob
from split_settings.tools import optional, include


# 구동 환경 체크
ENV = os.environ.get('DJANGO_ENV') or 'development'
print('****Running on %s settings****' % ENV)

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
SECRET_KEY = 'yb^^#^(x36=f%w4=g4!d0q07xoom$a70a5*p&q5elm%20wj!=f'

# 설정 파일 분리
COMPONENT_DIR = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'components')
EXEMPT_COMPONENT = [
    'static_file.py',
]
COMPONENTS = [
    'components/{}'.format(os.path.basename(component)) for component
    in glob.glob(os.path.join(COMPONENT_DIR, '*.py'))
    if not os.path.basename(component) in EXEMPT_COMPONENT
]
NEW_COMPONENTS = COMPONENTS + [
    'components/{}'.format(component) for component
    in EXEMPT_COMPONENT
]
SETTINGS = [
    'environments/%s.py' % ENV,
] + NEW_COMPONENTS
include(*SETTINGS)
