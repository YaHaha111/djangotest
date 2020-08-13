from .common import *

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
DEBUG = False


ALLOWED_HOSTS = ['127.0.0.1', 'localhost ', '47.110.14.69']


#HAYSTACK_CONNECTIONS['default']['URL'] = 'http://hellodjango_blog_tutorial_elasticsearch:9200/'