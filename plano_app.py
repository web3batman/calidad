from plano_model import plano,plano_form,plano_convert
from db_setup import init_db, db_session
from flask import Blueprint, Flask, jsonify, request, render_template, redirect, url_for, json
from sqlalchemy.orm.attributes import flag_modified
from sqlalchemy import create_engine
import pandas as pd
plano_app = Blueprint('plano_app', __name__)
@plano_app.route('/plano_list')
def plano_list():
    qry = db_session.query(plano).all()
    return render_template('plano_list.html', table=qry )
@plano_app.route('/plano_new', methods=['GET', 'POST'])
def plano_new():
    if request.method == 'GET':
        return render_template('plano_new.html')
    if request.method == 'POST':
        form = plano_form(request.form)
        db_session.add(plano_convert(plano(), form))
        db_session.commit()
        return redirect('/plano_list')
@plano_app.route('/plano_edit', methods=['GET', 'POST'])
def plano_edit():
    if request.method == 'GET':
        id=request.args.get('id', None)
        qry = db_session.query(plano).filter(plano.id==id).first()
        return render_template('plano_edit.html', val=qry)
    if request.method == 'POST':
        form = plano_form(request.form)
        fo=plano_convert(plano(), form)
        flag_modified(fo,'plano')
        db_session.merge(fo)
        db_session.flush()
        db_session.commit()
        return redirect('/plano_list')
@plano_app.route('/plano_delete', methods=['GET', 'POST'])
def plano_delete():
    id=request.args.get('id', None)
    qry = db_session.query(plano).filter(plano.id==int(id))
    db_session.delete(qry.first())
    db_session.commit()
    return redirect('/plano_list')