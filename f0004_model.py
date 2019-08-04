from aplication import db
from wtforms import Form, StringField, SelectField, validators, IntegerField
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import UniqueConstraint, exc
class f0004(db.Model):
    __tablename__ = "f0004"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String, nullable=False)
    subarea = db.Column(db.String, nullable=False)
    ubicacion = db.Column(db.String, nullable=False)
    elemento = db.Column(db.String, nullable=False)
    fecha = db.Column(db.String, nullable=False)
    plano = db.Column(db.String, nullable=False)
    r1 = db.Column(db.String, nullable=False)
    r2 = db.Column(db.String, nullable=False)
    r3 = db.Column(db.String, nullable=False)
    r4 = db.Column(db.String, nullable=False)
    r5 = db.Column(db.String, nullable=False)
    r6 = db.Column(db.String, nullable=False)
    r7 = db.Column(db.String, nullable=False)
    observacion = db.Column(db.String, nullable=False)
class f0004_form(Form):
    id = IntegerField('id')
    area = StringField('area')
    subarea = StringField('subarea')
    ubicacion = StringField('ubicacion')
    elemento = StringField('elemento')
    fecha = StringField('fecha')
    plano = StringField('plano')
    r1 = StringField('r1')
    r2 = StringField('r2')
    r3 = StringField('r3')
    r4 = StringField('r4')
    r5 = StringField('r5')
    r6 = StringField('r6')
    r7 = StringField('r7')
    observacion = StringField('observacion')
def f0004_convert(f0004, form):
    f0004.id = form.id.data
    f0004.area = form.area.data
    f0004.subarea = form.subarea.data
    f0004.ubicacion = form.ubicacion.data
    f0004.elemento = form.elemento.data
    f0004.fecha = form.fecha.data
    f0004.plano = form.plano.data
    f0004.r1 = form.r1.data
    f0004.r2 = form.r2.data
    f0004.r3 = form.r3.data
    f0004.r4 = form.r4.data
    f0004.r5 = form.r5.data
    f0004.r6 = form.r6.data
    f0004.r7 = form.r7.data
    f0004.observacion = form.observacion.data
    return f0004
def f0004_obj(f0004, obj):
    f0004.id = obj.id
    f0004.area = obj.area
    f0004.subarea = obj.subarea
    f0004.ubicacion = obj.ubicacion
    f0004.elemento = obj.elemento
    f0004.fecha = obj.fecha
    f0004.plano = obj.plano
    f0004.r1 = obj.r1
    f0004.r2 = obj.r2
    f0004.r3 = obj.r3
    f0004.r4 = obj.r4
    f0004.r5 = obj.r5
    f0004.r6 = obj.r6
    f0004.r7 = obj.r7
    f0004.observacion = obj.observacion
    return f0004