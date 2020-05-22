from flask import request
from . import api
from .. import db
from ..decorators import json, paginate
from webargs.flaskparser import parser
import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalch import Sqlal
from flask_sqlalchemy import get_debug_queries
import settings
from elasticsearch import Elasticsearch                 #elasticsearch library
from flask import Blueprint

es = Blueprint('es' , __name__)                         #BluePrint of elasticsearch called in run.py

@es.route('/api/search', methods=['GET','POST'])
@json
def search():
    res = []
    es = Elasticsearch()                                 #elasticsearch object
    data = request.get_json()                            #get the data of the submit field

    str = list()
    need = list()
    conjunctions = list()
    others = list()
    not_req = list()
    final = dict()
    req = ['hostel' , 'wifi' , 'badminton' , 'basketball' , 'tennis' , 'swimming' , 'ac' , 'wifi' , 'school_rating' , 'football']

    conjunctions = ['for' , 'nor' , 'but' , 'or' , 'yet' , 'so' , 'there' , 'in' , 'is' , 'schools' , 'sports'] # all conjunctions
    str =  data['search'].split()                          #split data into multiple fields

    flag = 0

    for i in range(len(str)):                              #filter out all conjunctions
       flag = 0
       for j in range(len(conjunctions)):
           if str[i].lower() == conjunctions[j]:
               flag = 1
               break
       if flag == 0:
           others.append(str[i].lower())

    for x in range(len(req)):
        final[req[x]] = -1

    for i in range(len(others)):                             #identifying all the with or without statements
       flag = 0
       for j in range(len(req)):
           if others[i] == req[j]:
               if others[i - 1] == 'not' or others[i - 1] == 'without' or others[i - 1] == 'no':
                   final[others[i]] = 0
                   flag = 1
                   break
               if others[i - 1] == 'with' or others[i - 1] == 'having':
                   final[others[i]] = 1
                   flag = 2
                   break

               if others[i - 1] == 'and':
                   if flag == 1:
                       final[others[i]] = 0
                   else:
                       final[others[i]] = 1

    flag = 0

    for x in range(len(req)):
        if final[req[x]] == -1:
            continue
        else:
            flag = 1
            break

    for x in range(len(req)):
        print final[req[x]]


    if flag == 0:
        search_body = {
            "query" : {
                "query_string" : {
                    "query" : others[0],
                    "match_all" : {}
                }
            }
        }
                                                                    #elasticsearch query
    else:
        search_body = {
            "query":{
        "filtered": {
                "query": {
                    "query_string": {
                        "query": others[0]
                    }
                },
                "filter": {
                    "bool" : {
                        "should" : [
                            {"term" : { req[0] : final[req[0]]}     #to filter the search query text
                            },
                            {
                              "term" : { req[1] : final[req[1]]}
                            },
                            {
                              "term" : { req[2] : final[req[2]]}
                            },
                            {
                              "term" : { req[3] : final[req[3]]}
                            },
                            {
                               "term" : { req[4] : final[req[4]]}
                            },
                            {
                               "term" : { req[5] : final[req[5]]}
                            },
                            {
                                "term" : { req[6] : final[req[6]]}
                            },
                            {
                                "term" : { req[7] : final[req[7]]}
                            },
                            {
                                "term" : { req[8] : final[req[8]]}
                            },
                        ]
                     }
                 }
             }

    }

}

    filtered_result = []

    for x in es.search(body=search_body).get('hits').get('hits'):
        _src = x.get('_source')
        entry = {'id': x.get('_id')}
        entry.update(_src)
        filtered_result.append(entry)

    return {"result" : filtered_result}                                     #print final result
