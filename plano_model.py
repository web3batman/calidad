from aplication import db
from wtforms import Form, StringField, SelectField, validators, IntegerField
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import UniqueConstraint, exc
class plano(db.Model):
    __tablename__ = "plano"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String, nullable=False)
    rev = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    id_google = db.Column(db.String, nullable=False)
class plano_form(Form):
    id = IntegerField('id')
    codigo = StringField('codigo')
    rev = StringField('rev')
    title = StringField('title')
    id_google = StringField('id_google')
def plano_convert(plano, form):
    plano.id = form.id.data
    plano.codigo = form.codigo.data
    plano.rev = form.rev.data
    plano.title = form.title.data
    plano.id_google = form.title.data
    return plano
def plano_obj(plano, obj):
    plano.id = obj.id
    plano.codigo = obj.codigo
    plano.rev = obj.rev
    plano.title =  obj.title
    plano.id_google = obj.id_google
    return plano
def plano_dict(plano, dictionary):
    plano.codigo = dictionary['codigo']
    plano.rev = dictionary['rev']
    plano.title =  dictionary['title']
    plano.id_google = dictionary['id_google']
    return plano