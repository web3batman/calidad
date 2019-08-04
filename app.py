from flask import Flask, jsonify, request, render_template, redirect, url_for, json
from flask import send_file
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.attributes import flag_modified
import pandas as pd
from db_setup import init_db, db_session, service

import googledrive as gd
from f0016_model import f0016,f0016_form,f0016_convert
from f0006_model import f0006,f0006_form,f0006_convert
from f0007_model import f0007,f0007_form,f0007_convert
from f0033_model import f0033,f0033_form,f0033_convert
from f0004_model import f0004,f0004_form,f0004_convert
from f0005_model import f0005,f0005_form,f0005_convert
from plano_model import plano,plano_form,plano_convert,plano_dict
from ubicacion_model import ubicacion,ubicacion_form,ubicacion_convert

app= Flask(__name__)
#app.register_blueprint(f0016_app)
#@app.route("/", methods=['GET', 'POST'])
#def home():
#    if request.method == 'GET':
#        return redirect('https://drive.google.com/uc?id=17I_bNVPVvkyNVDHz2QvgMt7ndaipUn_b')
#    return redirect('/')
@app.route("/")
def home():
    disc = gd.items_folder(service,'Formatos_Calidad')
    disc = [x['title'] for x in disc]
    return render_template('pages/disciplina_list.html', table=disc )
    
@app.route("/list_formato")
def list_formato():
    name = request.args.get('disciplina', None)
    disc = gd.items_folder(service,name )
#    disc = [x['title'].split('_')[-1] for x in disc]
    disc = [x['title'] for x in disc]
    return render_template('pages/formato_list.html', table=disc )
@app.route("/list_protocolo", methods=['GET', 'POST'])
def list_protocolo():
    if request.method == 'GET':
        global fname
        name = request.args.get('format', None)
        fname = 'f' + name.split('.')[0].split('-')[-1]
        exec("qry1 = db_session.query(" + fname + ").all()")
        return render_template('pages/protocolo_list.html',table=locals()['qry1'], formato = fname)
@app.route("/edit_protocolo", methods=['GET', 'POST'])
def edit_protocolo():
    if request.method == 'GET':
        global fname
        name = request.args.get('format', None)
        fname = 'f' + name.split('.')[0].split('-')[-1]
        return render_template('forms/' + fname + '.html')
    if request.method == 'POST':
        print(request.form)
        exec("form =" + fname + "_form(request.form)")
        exec("formats = " + fname + "_convert(" + fname + "(),form)")
        exec("db_session.add(formats)")
        db_session.commit()
        return redirect('/')     
@app.route('/protocolo_print', methods=['GET', 'POST'])
def protocolo_print():
    if request.method == 'GET':
        id=request.args.get('id', None)
        formato=request.args.get('formato', None)
        fid = id.zfill(3)
        fform = formato[1:]
        name = fform + fid
        filename, fname, qry3= gd.generate_doc(formato, id)
        ps = qry3.plano.split(' ')
        count = 0
        planos = []
        for x in ps:
            if x:
                ps1 = x.split('Rev._')
                qry4 = db_session.query(plano).filter(plano.codigo==ps1[0] and plano.rev==ps1[1].rstrip()).first()
                print(qry4)
                tmpfile = gd.download(service, qry4.id_google)
                name1 = name + str(count) + ".pdf"
                count = count + 1
                upload2 =  gd.upload_file(service, 'DataBase',  tmpfile, name1, 'application/pdf')
                planos.append(upload2['id'])
        upload1 =  gd.upload_file(service, 'DataBase', filename, fname, 'application/msword')
        embedLink = upload1['embedLink']
        downloadlink = 'https://drive.google.com/uc?id=' + upload1['id']
        return render_template('pages/result_protocolo.html',embedLink = embedLink, downloadlink = downloadlink, planos=planos)
#    return send_file(file_stream, as_attachment=True, attachment_filename="f0016_2_"+"_1_"+".docx")

@app.route("/getData", methods=['GET'])
def getData():
    name = request.args.get('q', None)
    print(name)
    qry = db_session.query(ubicacion).all()
    ubica = [x.codigo+' '+x.ubicacion for x in qry]
    json_str = json.dumps(ubica)
    return jsonify(json_str)
@app.route("/planogetData", methods=['GET'])
def planogetData():
    name = request.args.get('q', None)
    print(name)
    qry = db_session.query(plano).all()
    planos = [x.codigo+'Rev._'+ x.rev + ' ' for x in qry]
    json_str = json.dumps(planos)
    return jsonify(json_str)
@app.route("/planogetid", methods=['GET'])
def planogetDid():
    name = request.args.get('q', None)
    name1 = name.split('Rev._')
    try:
        qry = db_session.query(plano).filter(plano.codigo==name1[0] and plano.rev==name1[1].rstrip()).first()
    except:
        print("no tiene reviscion")
    return jsonify(qry.id_google)
@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('pages/upload.html')
    if request.method == 'POST':
        f = request.files['file']
        filename, name = gd.detect_barcode(f)
        gd.upload_file(service, 'DataBase', filename, name, 'image/jpeg')
        
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)



