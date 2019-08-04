from aplication import db
from wtforms import Form, StringField, SelectField, validators, IntegerField
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import UniqueConstraint, exc
class f0033a(db.Model):
    __tablename__ = "f0033a"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    id_f0033 = db.Column(db.String, nullable=False)
    id_item = db.Column(db.String, nullable=False)
    detalle = db.Column(db.String, nullable=False)
    cable = db.Column(db.String, nullable=False)
    metal = db.Column(db.String, nullable=False)
class f0033a_form(Form):
    id = IntegerField('id')
    id_f0033 = StringField('id_f0033')
    id_item = StringField('id_item')
    detalle = StringField('detalle')
    cable = StringField('cable')
    metal = StringField('metal')
def f0033a_convert(f0033a, form):
    f0033a.id = form.id.data
    f0033a.id_f0033 = form.id_f0033.data
    f0033a.id_item = form.id_item.data
    f0033a.detalle = form.detalle.data
    f0033a.cable = form.cable.data
    f0033a.metal = form.metal.data
    return f0033a
def f0033a_obj(f0033a, obj):
    f0033a.id = obj.id
    f0033a.id_f0033 = obj.id_f0033
    f0033a.id_item = obj.id_item
    f0033a.detalle = obj.detalle
    f0033a.cable = obj.cable
    f0033a.metal = obj.metal
    return f0033a