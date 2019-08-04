from aplication import db
from wtforms import Form, StringField, SelectField, validators, IntegerField
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import UniqueConstraint, exc
class f0005(db.Model):
    __tablename__ = "f0005"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String, nullable=False)
    subarea = db.Column(db.String, nullable=False)
    ubicacion = db.Column(db.String, nullable=False)
    elemento = db.Column(db.String, nullable=False)
    fecha = db.Column(db.String, nullable=False)
    plano = db.Column(db.String, nullable=False)
    r11 = db.Column(db.String, nullable=False)
    r12 = db.Column(db.String, nullable=False)
    r13 = db.Column(db.String, nullable=False)
    r14 = db.Column(db.String, nullable=False)
    r15 = db.Column(db.String, nullable=False)
    r16 = db.Column(db.String, nullable=False)
    r21 = db.Column(db.String, nullable=False)
    r22 = db.Column(db.String, nullable=False)
    r23 = db.Column(db.String, nullable=False)
    r24 = db.Column(db.String, nullable=False)
    r25 = db.Column(db.String, nullable=False)
    r26 = db.Column(db.String, nullable=False)
    r27 = db.Column(db.String, nullable=False)
    r28 = db.Column(db.String, nullable=False)
    observacion = db.Column(db.String, nullable=False)
class f0005_form(Form):
    id = IntegerField('id')
    area = StringField('area')
    subarea = StringField('subarea')
    ubicacion = StringField('ubicacion')
    elemento = StringField('elemento')
    fecha = StringField('fecha')
    plano = StringField('plano')
    r11 = StringField('r11')
    r12 = StringField('r12')
    r13 = StringField('r13')
    r14 = StringField('r14')
    r15 = StringField('r15')
    r16 = StringField('r16')
    r21 = StringField('r21')
    r22 = StringField('r22')
    r23 = StringField('r23')
    r24 = StringField('r24')
    r25 = StringField('r25')
    r26 = StringField('r26')
    r27 = StringField('r27')
    r28 = StringField('r28')
    observacion = StringField('observacion')
def f0005_convert(f0005, form):
    f0005.id = form.id.data
    f0005.area = form.area.data
    f0005.subarea = form.subarea.data
    f0005.ubicacion = form.ubicacion.data
    f0005.elemento = form.elemento.data
    f0005.fecha = form.fecha.data
    f0005.plano = form.plano.data
    f0005.r11 = form.r11.data
    f0005.r12 = form.r12.data
    f0005.r13 = form.r13.data
    f0005.r14 = form.r14.data
    f0005.r15 = form.r15.data
    f0005.r16 = form.r16.data
    f0005.r21 = form.r21.data
    f0005.r22 = form.r22.data
    f0005.r23 = form.r23.data
    f0005.r24 = form.r24.data
    f0005.r25 = form.r25.data
    f0005.r26 = form.r26.data
    f0005.r27 = form.r27.data
    f0005.r28 = form.r28.data
    f0005.observacion = form.observacion.data
    return f0005
def f0005_obj(f0005, obj):
    f0005.id = obj.id
    f0005.area = obj.area
    f0005.subarea = obj.subarea
    f0005.ubicacion = obj.ubicacion
    f0005.elemento = obj.elemento
    f0005.fecha = obj.fecha
    f0005.plano = obj.plano
    f0005.r11 = obj.r11
    f0005.r12 = obj.r12
    f0005.r13 = obj.r13
    f0005.r14 = obj.r14
    f0005.r15 = obj.r15
    f0005.r16 = obj.r16
    f0005.r21 = obj.r21
    f0005.r22 = obj.r22
    f0005.r23 = obj.r23
    f0005.r24 = obj.r24
    f0005.r25 = obj.r25
    f0005.r26 = obj.r26
    f0005.r27 = obj.r27
    f0005.r28 = obj.r28
    f0005.observacion = obj.observacion
    return f0005