from . import db

# 链接表
class Link(db.Model):
    __tablename__ = 'link'
    id   = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(20))
    type = db.Column(db.String(20))
    url  = db.Column(db.String(100))
    
    def __init__(self, data):
        self.id       = data['id']
        self.name     = data['name']
        self.type     = data['type']
        self.url      = data['url']
