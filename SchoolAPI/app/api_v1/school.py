from flask import request
from . import api
from .. import db
from ..models import Quotes, Category
from ..decorators import json,paginate
from webargs.flaskparser import parser
import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalch import Sqlal
from flask_sqlalchemy import get_debug_queries
from ..email import send_email2
import settings
from webargs import fields
from webargs.flaskparser import parser
from flask import Blueprint
from elasticsearch import Elasticsearch
import re

get_Quotes = Blueprint('getquotes' , __name__)

@get_Quotes.route('/getQuotes', methods=['POST','GET'])
@json
def index():
    request_settings = settings.API_PARAMETERS['GET_SCHOOLS_REQUEST'] # accessing the class API_PARAMETERS
    # 'GETS_SCHOOLS_REQUEST'
    filters = dict()                 # for checking the  requested json  using filters
    RequestObject = request.get_json()    # the  json which we will receive from the front end

   #RequestData = parser.parse(args, request)
    r=list()
    for key in request_settings['QUOTE_FILTERS']:        #
        param = RequestObject.get(key, None)
        if param is None or str(param).strip() == '':
            continue
        else:
            if param == True:
                param = 1
                filters[key] = param                # for storing the  true for requested json in filters
                r.append(key)

    session = Sqlal.Session()                # making session
    quotes_session = session.query(Category)   #  making query on Class Category

    for x in filters:                         # iterating over the class Category
        quotes_session = quotes_session.filter(getattr(Category, x) == filters[x]) # for the filter part
        #  filtering for the motivational, spiritual , fun , friendship

    rows = quotes_session.all()            # for selecting all the rows

    response_settings = settings.API_PARAMETERS['GET_QUOTE_RESPONSE']
    result = list()
    rowx =list()

    for s in rows:
        for u in session.query(Quotes).all():
             if s.quote_id == u.id:
                 rowx.append(u)

    for s in rowx:
        data= dict()
        for x in response_settings['SCHOOL_DATA']:
            data[x] = getattr(s,x)
        result.append(data)
       # result.append(r)



    db.session.commit()

    return {"quotes" : result}


@get_Quotes.route('/addQuotes', methods=['POST','GET'])
@json
def add():
    args = {
        'id'    : fields.Int(),
        'author' : fields.Str(required = True),
        'quotes' : fields.Str(required = True),
        'quotecategory' :fields.List(fields.Str(required = True))

    }

    RequestData = parser.parse(args , request)

    add_in_table = Quotes()

    add_in_table.import_data(request.json)

    db.session.add(add_in_table)

    db.session.commit()

    return {"Success" : "OK"}

@get_Quotes.route('/editRating', methods=['POST'])
@json
def rate():
    args = {
        'id'  : fields.Int(required=True),
        'rating': fields.Int(required=True)
    }
    RequestObject = request.get_json()
    quotes_id = RequestObject['id']
    quote_new_rating = RequestObject['rating']

 #  making session with   database
    session = Sqlal.Session()
   # search quotes id in the Class Quotes
    for u in session.query(Quotes).all():
        if quotes_id == u.id:
            x = u.rating
            y = u.count_rating
            break

    obj1 = Quotes.query.get_or_404(quotes_id)

    total_count = y + 1
    new_rating = (u.rating + quote_new_rating) / total_count

    obj1.increment_count(total_count , new_rating)

    db.session.add(obj1)

    db.session.commit()

    return {"Success" : "OK"}


@get_Quotes.route('/TopQuotes', methods=['GET','POST'])
@json
def top():
    session = Sqlal.Session()                # making session
    result = list()
    response_settings = settings.API_PARAMETERS['GET_QUOTE_RESPONSE']

    for u in session.query(Quotes).all():
        data = dict()
        for x in response_settings['SCHOOL_DATA']:
            data[x] = getattr(u , x)
           # str = unicode(str, errors='ignore')
        result.append(data)
    print result
    return {"quote_list" : result}


@get_Quotes.route('/authorname',methods=['GET'])
@json
def display():
    res=list()
    session = Sqlal.Session()
    for u in session.query(Quotes).all():
        res.append(u.author)
    return {"author_name":res}


@get_Quotes.route('/category',methods=['GET'])
@json
def cadis():
    res=list()
    session=Sqlal.Session()
    res.append("motivational")
    res.append("spiritual")
    res.append("love")
    res.append("religion")
    res.append("success")
    res.append("friendship")
    res.append("fun")
    return {"category":res}


@get_Quotes.route('/displayAuthor',methods=['POST'])
@json
def get_author():
    request_settings = settings.API_PARAMETERS['GET_SCHOOLS_REQUEST']
    filters = dict()                 # for checking the  requested json  using filters
    RequestObject = request.get_json()    # the  json which we will receive from the front end
    print RequestObject

   #RequestData = parser.parse(args, request)
    param = list()
    for key in request_settings['AUTHOR_FILTERS']:        #
        param = RequestObject.get(key, None)
        if param is None or str(param).strip() == '':
            continue
        else:
            filters[key] = param

    #print "param=",param
                   # for storing the  true for requested json in filters

    session = Sqlal.Session()                # making session
    quotes_session = session.query(Quotes)

    rowx = list()
    for y in param:
        for s in session.query(Quotes).all():
            us = unicode(s.author,"utf-8")
            print us , y
            if us == y:
                rowx.append(s)


    #rows = quotes_session.all()            # for selecting all the rows

    response_settings = settings.API_PARAMETERS['GET_QUOTE_RESPONSE']
    result = list()
    #rowx =list()

    for s in rowx:
        data= dict()
        for x in response_settings['SCHOOL_DATA']:
            data[x] = getattr(s,x)
        result.append(data)
       # result.append(r)

    db.session.commit()

    return {"quotes" : result}


@get_Quotes.route('/search' , methods=['GET' , 'POST'])
@json
def search():
    es = Elasticsearch()

    data = request.get_json()

    search_body = {
            "query" : {
                "query_string" : {
                    "query" : data.get('search'),
                    "match_all" : {},
                    "index": "not_analyzed"
                }
            }
        }

    filtered_result = []

    for x in es.search(body=search_body).get('hits').get('hits'):
        _src = x.get('_source')
        entry = {'id': x.get('_id')}
        entry.update(_src)
        filtered_result.append(entry)

    return {"result" : filtered_result}

