from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_ckeditor import CKEditor
from flask_migrate import Migrate
from flask_wtf import CsrfProtect
from flask_debugtoolbar import DebugToolbar

bootstrap = Bootstrap()
mail = Mail()
login_manager = LoginManager()
db = SQLAlchemy()
ckeditor = CKEditor()
moment = Moment()
migrate = Migrate()
toolbar = DebugToolbar()
csrf = CsrfProtect()