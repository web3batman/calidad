from aplication import db
from wtforms import Form, StringField, SelectField, validators, IntegerField
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import UniqueConstraint, exc
class f0033(db.Model):
    __tablename__ = "f0033"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String, nullable=False)
    subarea = db.Column(db.String, nullable=False)
    ubicacion = db.Column(db.String, nullable=False)
    plano = db.Column(db.String, nullable=False)
    fecha = db.Column(db.String, nullable=False)
    soldador = db.Column(db.String, nullable=False)
    items = db.Column(db.String, nullable=False)
    observacion = db.Column(db.String, nullable=False)
class f0033_form(Form):
    id = IntegerField('id')
    area = StringField('area')
    subarea = StringField('subarea')
    ubicacion = StringField('ubicacion')
    plano = StringField('plano')
    fecha = StringField('fecha')
    soldador = StringField('soldador')
    items = StringField('items')
    observacion= StringField('obsevacion')
def f0033_convert(f0033, form):
    f0033.id = form.id.data
    f0033.area = form.area.data
    f0033.subarea = form.subarea.data
    f0033.ubicacion = form.ubicacion.data
    f0033.plano = form.plano.data
    f0033.fecha = form.fecha.data
    f0033.soldador = form.soldador.data
    f0033.items = form.items.data
    f0033.observacion = form.observacion.data
    return f0033
def f0033_obj(f0033, obj):
    f0033.id = obj.id
    f0033.area = obj.area
    f0033.subarea = obj.subarea
    f0033.ubicacion = obj.ubicacion
    f0033.plano = obj.plano
    f0033.fecha = obj.fecha
    f0033.soldador = obj.soldador
    f0033.items = obj.items
    f0033.observacion = obj.observacion
    return f0033