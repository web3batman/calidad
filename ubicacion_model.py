from aplication import db
from wtforms import Form, StringField, SelectField, validators, IntegerField
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import UniqueConstraint, exc
class ubicacion(db.Model):
    __tablename__ = "ubicacion"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String, nullable=False)
    ubicacion = db.Column(db.String, nullable=False)
    subarea_id = db.Column(Integer, ForeignKey('subarea.id'))

class ubicacion_form(Form):
    id = IntegerField('id')
    codigo = StringField('codigo')
    ubicacion = StringField('ubicacion')
    subarea_id = StringField('subarea_id')
def ubicacion_convert(ubicacion, form):
    ubicacion.id = form.id.data
    ubicacion.codigo = form.codigo.data
    ubicacion.ubicacion = form.ubicacion.data
    ubicacion.subarea_id = form.subarea_id.data
    return ubicacion
def ubicacion_obj(ubicacion, obj):
    ubicacion.id = obj.id
    ubicacion.codigo = obj.ubicacion
    ubicacion.ubicacion = obj.ubicacion_nombre
    ubicacion.subarea_id = obj.subarea_id
    return ubicacion