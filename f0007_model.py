from aplication import db
from wtforms import Form, StringField, SelectField, validators, IntegerField
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import UniqueConstraint, exc
class f0007(db.Model):
    __tablename__ = "f0007"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String, nullable=False)
    subarea = db.Column(db.String, nullable=False)
    ubicacion = db.Column(db.String, nullable=False)
    elemento = db.Column(db.String, nullable=False)
    plano = db.Column(db.String, nullable=False)
    e11 = db.Column(db.String, nullable=False)
    e12 = db.Column(db.String, nullable=False)
    e13 = db.Column(db.String, nullable=False)
    e14 = db.Column(db.String, nullable=False)
    e15 = db.Column(db.String, nullable=False)
    e16 = db.Column(db.String, nullable=False)
    e17 = db.Column(db.String, nullable=False)
    e18 = db.Column(db.String, nullable=False)
    e19 = db.Column(db.String, nullable=False)
    e110 = db.Column(db.String, nullable=False)
    e111 = db.Column(db.String, nullable=False)
    e21 = db.Column(db.String, nullable=False)
    e22 = db.Column(db.String, nullable=False)
    e23 = db.Column(db.String, nullable=False)
    e24 = db.Column(db.String, nullable=False)
    e25 = db.Column(db.String, nullable=False)
    e26 = db.Column(db.String, nullable=False)
    e27 = db.Column(db.String, nullable=False)
    e28 = db.Column(db.String, nullable=False)
    e29 = db.Column(db.String, nullable=False)
    e210 = db.Column(db.String, nullable=False)
    e211 = db.Column(db.String, nullable=False)
    e212 = db.Column(db.String, nullable=False)
    e213 = db.Column(db.String, nullable=False)
    e31 = db.Column(db.String, nullable=False)
    e32 = db.Column(db.String, nullable=False)
    e33 = db.Column(db.String, nullable=False)
    e34 = db.Column(db.String, nullable=False)
    e35 = db.Column(db.String, nullable=False)
    e36 = db.Column(db.String, nullable=False)
    e37 = db.Column(db.String, nullable=False)
    e38 = db.Column(db.String, nullable=False)
    e39 = db.Column(db.String, nullable=False)
    e41 = db.Column(db.String, nullable=False)
    e42 = db.Column(db.String, nullable=False)
    e43 = db.Column(db.String, nullable=False)
    e44 = db.Column(db.String, nullable=False)
    e45 = db.Column(db.String, nullable=False)
    e46 = db.Column(db.String, nullable=False)
    e47 = db.Column(db.String, nullable=False)
    e48 = db.Column(db.String, nullable=False)
    e49 = db.Column(db.String, nullable=False)
    e410 = db.Column(db.String, nullable=False)
    e411 = db.Column(db.String, nullable=False)
    e412 = db.Column(db.String, nullable=False)
    e413 = db.Column(db.String, nullable=False)
    e51 = db.Column(db.String, nullable=False)
    e52 = db.Column(db.String, nullable=False)
    e53 = db.Column(db.String, nullable=False)
    e54 = db.Column(db.String, nullable=False)
    e55 = db.Column(db.String, nullable=False)
    e56 = db.Column(db.String, nullable=False)
    e57 = db.Column(db.String, nullable=False)
    e58 = db.Column(db.String, nullable=False)
    e59 = db.Column(db.String, nullable=False)
    e59 = db.Column(db.String, nullable=False)
    e510 = db.Column(db.String, nullable=False)
    e511 = db.Column(db.String, nullable=False)
    e512 = db.Column(db.String, nullable=False)
    e513 = db.Column(db.String, nullable=False)
    e61 = db.Column(db.String, nullable=False)
    e62 = db.Column(db.String, nullable=False)
    e63 = db.Column(db.String, nullable=False)
    e64 = db.Column(db.String, nullable=False)
    e65 = db.Column(db.String, nullable=False)
    e66 = db.Column(db.String, nullable=False)
    e67 = db.Column(db.String, nullable=False)
    e68 = db.Column(db.String, nullable=False)
    e69 = db.Column(db.String, nullable=False)
    e610 = db.Column(db.String, nullable=False)
    e611 = db.Column(db.String, nullable=False)
    e612 = db.Column(db.String, nullable=False)
    observacion = db.Column(db.String, nullable=False)
class f0007_form(Form):
    id = IntegerField('id')
    area = StringField('area')
    subarea = StringField('subarea')
    ubicacion = StringField('ubicacion')
    elemento = StringField('elemento')
    plano = StringField('plano')
    e11 = StringField('e11')
    e12 = StringField('e12')
    e13 = StringField('e13')
    e14 = StringField('e14')
    e15 = StringField('e15')
    e16 = StringField('e16')
    e17 = StringField('e17')
    e18 = StringField('e18')
    e19 = StringField('e19')
    e110 = StringField('e110')
    e111 = StringField('e111')
    e21 = StringField('e21')
    e22 = StringField('e22')
    e23 = StringField('e23')
    e24 = StringField('e24')
    e25 = StringField('e25')
    e26 = StringField('e26')
    e27 = StringField('e27')
    e28 = StringField('e28')
    e29 = StringField('e29')
    e210 = StringField('e210')
    e211 = StringField('e211')
    e212 = StringField('e212')
    e213 = StringField('e213')
    e31 = StringField('e31')
    e32 = StringField('e32')
    e33 = StringField('e33')
    e34 = StringField('e34')
    e35 = StringField('e35')
    e36 = StringField('e36')
    e37 = StringField('e37')
    e38 = StringField('e38')
    e39 = StringField('e39')
    e41 = StringField('e41')
    e42 = StringField('e42')
    e43 = StringField('e43')
    e44 = StringField('e44')
    e45 = StringField('e45')
    e46 = StringField('e46')
    e47 = StringField('e47')
    e48 = StringField('e48')
    e49 = StringField('e49')
    e410 = StringField('e410')
    e411 = StringField('e411')
    e412 = StringField('e412')
    e413 = StringField('e413')
    e51 = StringField('e51')
    e52 = StringField('e52')
    e53 = StringField('e53')
    e54 = StringField('e54')
    e55 = StringField('e55')
    e56 = StringField('e56')
    e57 = StringField('e57')
    e58 = StringField('e58')
    e59 = StringField('e59')
    e59 = StringField('e59')
    e510 = StringField('e510')
    e511 = StringField('e511')
    e512 = StringField('e512')
    e513 = StringField('e513')
    e61 = StringField('e61')
    e62 = StringField('e62')
    e63 = StringField('e63')
    e64 = StringField('e64')
    e65 = StringField('e65')
    e66 = StringField('e66')
    e67 = StringField('e67')
    e68 = StringField('e68')
    e69 = StringField('e69')
    e610 = StringField('e610')
    e611 = StringField('e611')
    e612 = StringField('e612')
    observacion = StringField('observacion')
def f0007_convert(f0007, form):
    f0007.id = form.id.data
    f0007.area = form.area.data
    f0007.subarea = form.subarea.data
    f0007.ubicacion = form.ubicacion.data
    f0007.elemento = form.elemento.data
    f0007.plano = form.plano.data
    f0007.e11 = form.e11.data
    f0007.e12 = form.e12.data
    f0007.e13 = form.e13.data
    f0007.e14 = form.e14.data
    f0007.e15 = form.e15.data
    f0007.e16 = form.e16.data
    f0007.e17 = form.e17.data
    f0007.e18 = form.e18.data
    f0007.e19 = form.e19.data
    f0007.e110 = form.e110.data
    f0007.e111 = form.e111.data
    f0007.e21 = form.e21.data
    f0007.e22 = form.e22.data
    f0007.e23 = form.e23.data
    f0007.e24 = form.e24.data
    f0007.e25 = form.e25.data
    f0007.e26 = form.e26.data
    f0007.e27 = form.e27.data
    f0007.e28 = form.e28.data
    f0007.e29 = form.e29.data
    f0007.e210 = form.e210.data
    f0007.e211 = form.e211.data
    f0007.e212 = form.e212.data
    f0007.e213 = form.e213.data
    f0007.e31 = form.e31.data
    f0007.e32 = form.e32.data
    f0007.e33 = form.e33.data
    f0007.e34 = form.e34.data
    f0007.e35 = form.e35.data
    f0007.e36 = form.e36.data
    f0007.e37 = form.e37.data
    f0007.e38 = form.e38.data
    f0007.e39 = form.e39.data
    f0007.e41 = form.e41.data
    f0007.e42 = form.e42.data
    f0007.e43 = form.e43.data
    f0007.e44 = form.e44.data
    f0007.e45 = form.e45.data
    f0007.e46 = form.e46.data
    f0007.e47 = form.e47.data
    f0007.e48 = form.e48.data
    f0007.e49 = form.e49.data
    f0007.e410 = form.e410.data
    f0007.e411 = form.e411.data
    f0007.e412 = form.e412.data
    f0007.e413 = form.e413.data
    f0007.e51 = form.e51.data
    f0007.e52 = form.e52.data
    f0007.e53 = form.e53.data
    f0007.e54 = form.e54.data
    f0007.e55 = form.e55.data
    f0007.e56 = form.e56.data
    f0007.e57 = form.e57.data
    f0007.e58 = form.e58.data
    f0007.e59 = form.e59.data
    f0007.e59 = form.e59.data
    f0007.e510 = form.e510.data
    f0007.e511 = form.e511.data
    f0007.e512 = form.e512.data
    f0007.e513 = form.e513.data
    f0007.e61 = form.e61.data
    f0007.e62 = form.e62.data
    f0007.e63 = form.e63.data
    f0007.e64 = form.e64.data
    f0007.e65 = form.e65.data
    f0007.e66 = form.e66.data
    f0007.e67 = form.e67.data
    f0007.e68 = form.e68.data
    f0007.e69 = form.e69.data
    f0007.e610 = form.e610.data
    f0007.e611 = form.e611.data
    f0007.e612 = form.e612.data
    f0007.observacion = form.observacion.data
    return f0007
def f0007_obj(f0007, obj):
    f0007.id = obj.id
    f0007.area = obj.area
    f0007.subarea = obj.subarea
    f0007.ubicacion = obj.ubicacion
    f0007.elemento = obj.elemento
    f0007.plano = obj.plano
    f0007.e11 = obj.e11
    f0007.e12 = obj.e12
    f0007.e13 = obj.e13
    f0007.e14 = obj.e14
    f0007.e15 = obj.e15
    f0007.e16 = obj.e16
    f0007.e17 = obj.e17
    f0007.e18 = obj.e18
    f0007.e19 = obj.e19
    f0007.e110 = obj.e110
    f0007.e111 = obj.e111
    f0007.e21 = obj.e21
    f0007.e22 = obj.e22
    f0007.e23 = obj.e23
    f0007.e24 = obj.e24
    f0007.e25 = obj.e25
    f0007.e26 = obj.e26
    f0007.e27 = obj.e27
    f0007.e28 = obj.e28
    f0007.e29 = obj.e29
    f0007.e210 = obj.e210
    f0007.e211 = obj.e211
    f0007.e212 = obj.e212
    f0007.e213 = obj.e213
    f0007.e31 = obj.e31
    f0007.e32 = obj.e32
    f0007.e33 = obj.e33
    f0007.e34 = obj.e34
    f0007.e35 = obj.e35
    f0007.e36 = obj.e36
    f0007.e37 = obj.e37
    f0007.e38 = obj.e38
    f0007.e39 = obj.e39
    f0007.e41 = obj.e41
    f0007.e42 = obj.e42
    f0007.e43 = obj.e43
    f0007.e44 = obj.e44
    f0007.e45 = obj.e45
    f0007.e46 = obj.e46
    f0007.e47 = obj.e47
    f0007.e48 = obj.e48
    f0007.e49 = obj.e49
    f0007.e410 = obj.e410
    f0007.e411 = obj.e411
    f0007.e412 = obj.e412
    f0007.e413 = obj.e413
    f0007.e51 = obj.e51
    f0007.e52 = obj.e52
    f0007.e53 = obj.e53
    f0007.e54 = obj.e54
    f0007.e55 = obj.e55
    f0007.e56 = obj.e56
    f0007.e57 = obj.e57
    f0007.e58 = obj.e58
    f0007.e59 = obj.e59
    f0007.e59 = obj.e59
    f0007.e510 = obj.e510
    f0007.e511 = obj.e511
    f0007.e512 = obj.e512
    f0007.e513 = obj.e513
    f0007.e61 = obj.e61
    f0007.e62 = obj.e62
    f0007.e63 = obj.e63
    f0007.e64 = obj.e64
    f0007.e65 = obj.e65
    f0007.e66 = obj.e66
    f0007.e67 = obj.e67
    f0007.e68 = obj.e68
    f0007.e69 = obj.e69
    f0007.e610 = obj.e610
    f0007.e611 = obj.e611
    f0007.e612 = obj.e612
    f0007.observacion = obj.observacion
    return f0007