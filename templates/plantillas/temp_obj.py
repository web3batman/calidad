from aplication import db
from wtforms import Form, StringField, SelectField, validators, IntegerField
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import UniqueConstraint, exc
class {{name}}(db.Model):
    __tablename__ = "{{name}}"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True){%for form in dbform%}
    {{form}} = db.Column(db.String, nullable=False){%endfor%}
class {{name}}_form(Form):
    id = IntegerField('id'){%for form in dbform%}
    {{form}} = StringField('{{form}}'){%endfor%}
def {{name}}_convert({{name}}, form):
    {{name}}.id = form.id.data{%for form in dbform%}
    {{name}}.{{form}} = form.{{form}}.data{%endfor%}
    return {{name}}
def {{name}}_obj({{name}}, obj):
    {{name}}.id = obj.id{%for form in dbform%}
    {{name}}.{{form}} = obj.{{form}}{%endfor%}
    return {{name}}