from {{name}}_model import {{name}},{{name}}_form,{{name}}_convert
from db_setup import init_db, db_session
from flask import Blueprint, Flask, jsonify, request, render_template, redirect, url_for, json
from sqlalchemy.orm.attributes import flag_modified
from sqlalchemy import create_engine
import pandas as pd
{{name}}_app = Blueprint('{{name}}_app', __name__)
@{{name}}_app.route('/{{name}}_list')
def {{name}}_list():
    qry = db_session.query({{name}}).all()
    return render_template('{{name}}_list.html', table=qry )
@{{name}}_app.route('/{{name}}_new', methods=['GET', 'POST'])
def {{name}}_new():
    if request.method == 'GET':
        return render_template('{{name}}_new.html')
    if request.method == 'POST':
        form = {{name}}_form(request.form)
        db_session.add({{name}}_convert({{name}}(), form))
        db_session.commit()
        return redirect('/{{name}}_list')
@{{name}}_app.route('/{{name}}_edit', methods=['GET', 'POST'])
def {{name}}_edit():
    if request.method == 'GET':
        id=request.args.get('id', None)
        qry = db_session.query({{name}}).filter({{name}}.id==id).first()
        return render_template('{{name}}_edit.html', val=qry)
    if request.method == 'POST':
        form = {{name}}_form(request.form)
        fo={{name}}_convert({{name}}(), form)
        flag_modified(fo,'{{name}}')
        db_session.merge(fo)
        db_session.flush()
        db_session.commit()
        return redirect('/{{name}}_list')
@{{name}}_app.route('/{{name}}_delete', methods=['GET', 'POST'])
def {{name}}_delete():
    id=request.args.get('id', None)
    qry = db_session.query({{name}}).filter({{name}}.id==int(id))
    db_session.delete(qry.first())
    db_session.commit()
    return redirect('/{{name}}_list')