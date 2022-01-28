from flask import jsonify, Blueprint, request

from models import db
from models import Link,Log
from .service import *

bp_topic = Blueprint('bp_topic',__name__)

@bp_topic.route('/')
def guide_index():  # put application's code here
    return jsonify()



def saveLog(uid,url):
    log = Log()
    log.uid = uid
    log.url = url
    log.time = getNowDatetime()
    db.session.add(log)
    db.session.commit()