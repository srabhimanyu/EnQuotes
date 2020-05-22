from flask import request
from . import api
from .. import db
from ..models import Review , User
from ..decorators import json,paginate
from webargs.flaskparser import parser
import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalch import Sqlal
from flask_sqlalchemy import get_debug_queries
from ..email import send_email2
import settings
from flask import Blueprint

newuser = Blueprint('newuser' , __name__)

@newuser.route('/addUser' , methods = ['GET','POST'])                         #Route for adding new users
@json
def getUserInfo():

   user = User()
   RequestObject = request.get_json()
   print request.json

   request_email = RequestObject['email']
   request_school_id = int(RequestObject['school_id'])                                         #string handling

   flag = 0



   email_query_session = db.session.query(User.id).filter(User.email == request_email)      #check wether the email exists in db

   if email_query_session.count() > 0 : # only 1                                #if count > 0
         for c in email_query_session:                                          #Loop for obtaining the user id for the email id
             id_user = c.id


         query = db.session.query(Review).filter(Review.user_id == id_user)           #query for obtaining the review id for user id
         res = query.all()

         users_reviews = query.count();                                         #count the reviews for particular user id

         for c in res:
           if c.school_id == request_school_id :
               temp_review_id = c.id                                            #if the user reviewed the school get the review id
               flag = 1
               break

         if flag == 0 and users_reviews >= 0 :
             return {"user_id":id_user,"user_exists" : True, "review_canbe_added":True, "edit" : False } # review can be added

         if flag == 1 :
           return {"user_id":id_user,"user_exists" : True, "review_canbe_added":False, "edit":True ,"review_id": temp_review_id} #can be edited

         #else:
          #  user.import_data(request.json) # new user review added
           # db.session.add(user)
            #db.session.commit()
            #return {"success" : "ok"}

   else:
       user.import_data(request.json)                                           #if the email doesnt exist add user to the db
       db.session.add(user)
       db.session.commit()

       for c in db.session.query(User.id).filter(User.email == request_email):
            id_user = c.id

       return {"user_id":id_user, "user_exists" : False, "review_canbe_added":True , "edit":False}