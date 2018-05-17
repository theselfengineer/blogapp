import os
APP_DIR = os.path.dirname(os.path.realpath(__file__))
basedir = os.path.abspath(os.path.dirname(__file__))

#   export FLASK_APP=blogapp.py
#   export FLASK_DEBUG=1

class Config(object):

    SQLALCHEMY_DATABASE_URI = 'sqlite:////%s' % os.path.join(APP_DIR, 'DB/blog.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 2
    LANGUAGES = ['en', 'es']
    SECRET_KEY = 'supercalifragilisticoespialidoso'
    CKEDITOR_FILE_UPLOADER = 'upload'
    UPLOADED_PATH = os.path.join(basedir, 'app/uploads')
    CKEDITOR_SERVE_LOCAL = True
    CKEDITOR_HEIGHT = 600
    CKEDITOR_PKG_TYPE = 'full'
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
