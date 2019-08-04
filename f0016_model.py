from aplication import db
from wtforms import Form, StringField, SelectField, validators, IntegerField
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import UniqueConstraint, exc
class f0016(db.Model):
    __tablename__ = "f0016"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String, nullable=False)
    subarea = db.Column(db.String, nullable=False)
    elemento = db.Column(db.String, nullable=False)
    ubicacion = db.Column(db.String, nullable=False)
    fecha = db.Column(db.String, nullable=False)
    plano = db.Column(db.String, nullable=False)
    metodo = db.Column(db.String, nullable=False)
    q21 = db.Column(db.String, nullable=False)
    q22 = db.Column(db.String, nullable=False)
    q23 = db.Column(db.String, nullable=False)
    q24 = db.Column(db.String, nullable=False)
    q25 = db.Column(db.String, nullable=False)
    q26 = db.Column(db.String, nullable=False)
    q27 = db.Column(db.String, nullable=False)
    fprint =  db.Column(db.String, nullable=False)
    fscan = db.Column(db.String, nullable=False)
    esquema = db.Column(db.String, nullable=False)
    observacion = db.Column(db.String, nullable=False)
class f0016_form(Form):
    id = IntegerField('id')
    area = StringField('area')
    subarea = StringField('subarea')
    elemento = StringField('elemento')
    ubicacion = StringField('ubicacion')
    fecha = StringField('fecha')
    plano = StringField('plano')
    metodo = StringField('metodo')
    q21 = StringField('21')
    q22 = StringField('22')
    q23 = StringField('23')
    q24 = StringField('24')
    q25 = StringField('25')
    q26 = StringField('26')
    q27 = StringField('27')
    fprint = StringField('fprint')
    fscan = StringField('fscan')
    esquema = StringField('esquema')
    observacion = StringField('observacion')
def f0016_convert(f0016, form):
    f0016.id = form.id.data
    f0016.area = form.area.data
    f0016.subarea = form.subarea.data
    f0016.elemento = form.elemento.data
    f0016.ubicacion = form.ubicacion.data
    f0016.fecha = form.fecha.data
    f0016.plano = form.plano.data
    f0016.metodo = form.metodo.data
    f0016.q21 = form.q21.data
    f0016.q22 = form.q22.data
    f0016.q23 = form.q23.data
    f0016.q24 = form.q24.data
    f0016.q25 = form.q25.data
    f0016.q26 = form.q26.data
    f0016.q27 = form.q27.data
    f0016.fprint = form.fprint.data
    f0016.fscan = form.fscan.data
    f0016.esquema = form.esquema.data
    f0016.observacion = form.observacion.data
    return f0016
#def area_obj(area, obj):
#    area.id = obj.id
#    area.area = obj.area_nombre
#    area.codigo = obj.area
#    return area

