from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

import pandas as pd
import numpy as np
from apiclient.http import MediaIoBaseDownload
from apiclient.http import MediaFileUpload
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm, Inches, Pt
import barcode
from barcode.writer import ImageWriter
import cv2
import io
import imutils
from datetime import date

from pdf2image import convert_from_path, convert_from_bytes
from pyzbar.pyzbar import decode
from db_setup import init_db, db_session
from flask import Flask, jsonify, request, render_template, redirect, url_for, json
from flask import send_file
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.attributes import flag_modified

from f0016_model import f0016,f0016_form,f0016_convert
from f0006_model import f0006,f0006_form,f0006_convert
from f0007_model import f0007,f0007_form,f0007_convert
from f0033_model import f0033,f0033_form,f0033_convert
from f0004_model import f0004,f0004_form,f0004_convert
from f0005_model import f0005,f0005_form,f0005_convert
def all_files(service):
    result = []
    page_token = None
    while True:
        param = {}
        if page_token:
            param['pageToken'] = page_token
        files = service.files().list(**param).execute()
        
        result.extend(files['items'])
        page_token = files.get('nextPageToken')
        if not page_token:
            break
    return result

def items_folder(service, path):
    query = "title='{}'".format(path)
    f_id = service.files().list(q=query,pageToken=None).execute()['items'][0]['id']
    page_token = None
    while True:
        result = []
        param = {}
        if page_token:
            param['pageToken'] = page_token
        children = service.children().list(folderId=f_id, **param).execute()
        result.extend(children['items'])
        page_token = children.get('nextPageToken')
        if not page_token:
            break
    result = [service.files().get(fileId=x['id'] ).execute() for x in result]
    return result

def get_contain_file(service, contain):
    query = "title contains '{}'".format(contain)
    file1 = service.files().list(q=query,pageToken=None).execute()
    return file1

def upload_file(service, pathgoogle, filename, name,  mimetype):
    query = "title='{}'".format(pathgoogle)
    buscar = service.files().list(q=query,fields='nextPageToken, items(id, title)',pageToken=None).execute()
    folder_id = buscar['items'][0]['id']
    body = {
    'title': name,
    'mimeType': mimetype,
    "parents": [{"id": folder_id, "kind": "drive#childList"}] }                 
    media_body = MediaFileUpload(filename, mimetype=mimetype, resumable=True)
    res = service.files().insert(
                body=body,
                media_body= media_body).execute()
    return res
def download(service, file_id):
    request1 = service.files().get_media(fileId=file_id)
    tmp_file = 'temp/temp_plano.pdf'
    fh = io.FileIO(tmp_file,'wb')     
    downloader = MediaIoBaseDownload(fh, request1)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
    fh.close()
    return tmp_file

def generate_doc(formato, id):
    docform = "doc/" + formato +  ".docx"
    exec("qry2 = db_session.query("+formato+").filter("+formato+".id==int(id)).first()")
#    qry3 = locals()['qry2']
#    list1 = [x for x in qry3.items.split(' ') if x]
#    [{"descripcion":x,"cable":"4/0 - 4/0","metal":"250"} for x in list1 if x=="s3"]
    doc = DocxTemplate(docform)
    fid = id.zfill(3)
    fform = formato[1:]
    name = fform + fid
    EAN = barcode.get_barcode_class('ean8')
    ean = EAN(name + '0', writer=ImageWriter())
    pngname = ean.save('ean8_1')
    image = cv2.imread(pngname)
    cv2.imwrite(pngname, image[20:100,:,2])
    context = {'f' : locals()['qry2'],
               'bcean8' : InlineImage(doc,pngname,width=Mm(40))}
    doc.render(context)
    filename = "temp/temp.docx"
    doc.save(filename)
    fname = name + ".docx"
    qry3 = locals()['qry2']
    return filename, fname, qry3
def detect_barcode(f):
    jpgname = 'temp/temp.jpg'
    jpgbar = 'temp/tempbar.jpg'
    f.save(jpgname)
#        images_from_path = convert_from_path(pdfname, dpi=300, last_page=1, first_page =1)
#        for page in images_from_path:
#            page.save(jpgname)
    image = cv2.imread(jpgname)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ddepth = cv2.cv.CV_32F if imutils.is_cv2() else cv2.CV_32F
    gradX = cv2.Sobel(gray, ddepth=ddepth, dx=1, dy=0, ksize=-1)
    gradY = cv2.Sobel(gray, ddepth=ddepth, dx=0, dy=1, ksize=-1)
    gradient = cv2.subtract(gradX, gradY)
    gradient = cv2.convertScaleAbs(gradient)
    blurred = cv2.blur(gradient, (9, 9))
    (_, thresh) = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (80, 3))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    closed = cv2.erode(closed, None, iterations = 25)
    closed = cv2.dilate(closed, None, iterations = 25)
    cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
    rect = cv2.minAreaRect(c)
    box = cv2.cv.BoxPoints(rect) if imutils.is_cv2() else cv2.boxPoints(rect)
    box = np.int0(box)
    x1,x2,x3,x4,y1,y2,y3,y4 =box[0][0],box[1][0],box[2][0],box[3][0],box[0][1],box[1][1],box[2][1],box[3][1]
    top_left_x = min([x1,x2,x3,x4])
    top_left_y = min([y1,y2,y3,y4])
    bot_right_x = max([x1,x2,x3,x4])
    bot_right_y = max([y1,y2,y3,y4])
    img = image[top_left_y+6:bot_right_y+6, top_left_x-10:bot_right_x+10]
    image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(jpgbar, image_gray)
    code = decode(cv2.imread(jpgbar))[0][0]
    c1 = code.decode('ascii')
    nom_form = c1[0:4]
    reg = int(c1[4:7])
    tablas = 'f' + nom_form
    exec("qry = db_session.query(" + tablas + ").filter(" + tablas + ".id==" + str(reg) + ").first()")
    qry1 = locals()['qry']
    qry1.fscan = str(date.today())
    flag_modified(qry1,'fscan')
    db_session.merge(qry1)
    db_session.flush()
    db_session.commit()
    name = nom_form[1:4] + str(reg).zfill(4) + ".jpg"
    filename = "temp/" + name
#    os.rename(jpgname, filename)
    return jpgname, name

