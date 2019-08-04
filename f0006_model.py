from aplication import db
from wtforms import Form, StringField, SelectField, validators, IntegerField
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import UniqueConstraint, exc
class f0006(db.Model):
    __tablename__ = "f0006"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String, nullable=False)
    subarea = db.Column(db.String, nullable=False)
    ubicacion = db.Column(db.String, nullable=False)
    elemento = db.Column(db.String, nullable=False)
    fecha = db.Column(db.String, nullable=False)
    plano = db.Column(db.String, nullable=False)
    resistencia_concreto = db.Column(db.String, nullable=False)
    temperatura_concreto = db.Column(db.String, nullable=False)
    temperatura_ambiente = db.Column(db.String, nullable=False)
    slump = db.Column(db.String, nullable=False)
    aire = db.Column(db.String, nullable=False)
    cilindros_muestra = db.Column(db.String, nullable=False)
    muestras = db.Column(db.String, nullable=False)
    limpieza_estructura = db.Column(db.String, nullable=False)
    teorico = db.Column(db.String, nullable=False)
    real = db.Column(db.String, nullable=False)
    segregacion = db.Column(db.String, nullable=False)
    junta_fria = db.Column(db.String, nullable=False)
    start = db.Column(db.String, nullable=False)
    finish = db.Column(db.String, nullable=False)
    duracion = db.Column(db.String, nullable=False)
    observacion = db.Column(db.String, nullable=False)
    fprint = db.Column(db.String, nullable=False)
    fscan = db.Column(db.String, nullable=False)
class f0006_form(Form):
    id = IntegerField('id')
    area = StringField('area')
    subarea = StringField('subarea')
    ubicacion = StringField('ubicacion')
    elemento = StringField('elemento')
    fecha = StringField('fecha')
    plano = StringField('plano')
    resistencia_concreto = StringField('resistencia_concreto')
    temperatura_concreto = StringField('temperatura_concreto')
    temperatura_ambiente = StringField('temperatura_ambiente')
    slump = StringField('slump')
    aire = StringField('aire')
    cilindros_muestra = StringField('cilindros_muestra')
    muestras = StringField('muestras')
    limpieza_estructura = StringField('limpieza_estructura')
    teorico = StringField('teorico')
    real = StringField('real')
    segregacion = StringField('segregacion')
    junta_fria = StringField('junta_fria')
    start = StringField('start')
    finish = StringField('finish')
    duracion = StringField('duracion')
    observacion = StringField('observacion')
    fprint = StringField('fprint')
    fscan = StringField('fscan')
def f0006_convert(f0006, form):
    f0006.id = form.id.data
    f0006.area = form.area.data
    f0006.subarea = form.subarea.data
    f0006.ubicacion = form.ubicacion.data
    f0006.elemento = form.elemento.data
    f0006.fecha = form.fecha.data
    f0006.plano = form.plano.data
    f0006.resistencia_concreto = form.resistencia_concreto.data
    f0006.temperatura_concreto = form.temperatura_concreto.data
    f0006.temperatura_ambiente = form.temperatura_ambiente.data
    f0006.slump = form.slump.data
    f0006.aire = form.aire.data
    f0006.cilindros_muestra = form.cilindros_muestra.data
    f0006.muestras = form.muestras.data
    f0006.limpieza_estructura = form.limpieza_estructura.data
    f0006.teorico = form.teorico.data
    f0006.real = form.real.data
    f0006.segregacion = form.segregacion.data
    f0006.junta_fria = form.junta_fria.data
    f0006.start = form.start.data
    f0006.finish = form.finish.data
    f0006.duracion = form.duracion.data
    f0006.observacion = form.observacion.data
    f0006.fprint = form.fprint.data
    f0006.fscan = form.fscan.data
    return f0006
def f0006_obj(f0006, obj):
    f0006.id = obj.id
    f0006.area = obj.area
    f0006.subarea = obj.subarea
    f0006.ubicacion = obj.ubicacion
    f0006.elemento = obj.elemento
    f0006.fecha = obj.fecha
    f0006.plano = obj.plano
    f0006.resistencia_concreto = obj.resistencia_concreto
    f0006.temperatura_concreto = obj.temperatura_concreto
    f0006.temperatura_ambiente = obj.temperatura_ambiente
    f0006.slump = obj.slump
    f0006.aire = obj.aire
    f0006.cilindros_muestra = obj.cilindros_muestra
    f0006.muestras = obj.muestras
    f0006.limpieza_estructura = obj.limpieza_estructura
    f0006.teorico = obj.teorico
    f0006.real = obj.real
    f0006.segregacion = obj.segregacion
    f0006.junta_fria = obj.junta_fria
    f0006.start = obj.start
    f0006.finish = obj.finish
    f0006.duracion = obj.duracion
    f0006.observacion = obj.observacion
    f0006.fprint = obj.fprint
    f0006.fscan = obj.fscan
    return f0006