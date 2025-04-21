from flask import Blueprint

toilet_bp = Blueprint("toilet", __name__)

from . import toilet_post
from . import toilet_get
from . import toilet_delete
from . import toilet_comments_post
from . import toilet_features_post
