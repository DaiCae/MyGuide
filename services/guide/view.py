from flask import jsonify, render_template, Blueprint, request

from models import db
from models import Link,Log
from .service import *

bp_guide = Blueprint('bp_guide',__name__)

links =[]
link ={
    'name':'monitor',
    'type':'ipv6',
    'url':'http://monitor.yuxuan.work:3000',
    }
links.append(link)

# 首页显示
@bp_guide.route('/')
def guide_index():  # put application's code here
    return render_template("index.html",links=links)



def saveLog(uid,url):
    log = Log()
    log.uid = uid
    log.url = url
    log.time = getNowDatetime()
    db.session.add(log)
    db.session.commit()