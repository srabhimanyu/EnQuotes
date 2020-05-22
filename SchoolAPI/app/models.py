from datetime import datetime
from dateutil import parser as datetime_parser
from dateutil.tz import tzutc
from sqlalchemy import event
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import url_for, current_app
from . import db
from .exceptions import ValidationError
from elasticsearch import Elasticsearch
from .utils import split_url
import json
from sqlalchemy import Column, Integer, String, Enum
"""
class City(db.Model):
    __tablename__='city'
    id = db.Column(db.Integer,primary_key=True)
    school_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    def set_name(self, name):
        self.name = name

    def export_data(self):
        return{
            'self_url': self.get_url(),
            'id' : self.id,
            'name': self.name
        }"""

class Quotes(db.Model):
    __tablename__='quotes'
    id = db.Column(db.Integer,primary_key=True)
    author=db.Column(db.String(256))
    quotes=db.Column(db.String(256))
    rating=db.Column(db.Integer)
    count_rating = db.Column(db.Integer)
    category=db.Column(db.String(256))
    image=db.Column(db.String(256))
    url=db.Column(db.String(256))
    def export_data(self):
        # Quotes_data
       return {
           'self_url': self.get_url(),
            'id' : self.id,
           'author'  : self.author,
           'quotes'  : self.quotes,
           'rating'  : self.rating,
           'category':self.category,
           'image'   : self.image,
           'url'     : self.url

       }

    def import_data(self , data):
        try:
            self.author = data['author'],
            self.quotes = data['quotes'],
            self.rating = data['rating']
            res = list()

        except KeyError as e:
            raise ValidationError('Invalid Input' +e.args[0])
        return self

    def increment_count(self, data1 , data2):
        try:
            self.count_rating = data1
            self.rating = data2
        except KeyError as e:
             raise ValidationError('Invalid input ' +e.args[0])
        return self


def after_entry_insert(mapper, connection, target):
    es = Elasticsearch()
    es.index(index="my_quotes", doc_type="test-1", id=target.id,
             body={"id": target.id, "quotes": target.quotes, "author" : target.author,
                   "category" : target.category, "image_url" : target.image_url , "url" : target.url,
                   "rating" : target.rating} )

def after_entry_update(mapper, connection, target):
        pass

event.listen(Quotes, 'after_insert', after_entry_insert)
event.listen(Quotes, 'after_update', after_entry_insert)



class  Category(db.Model):
    __tablename__='category'
    id=db.Column(db.Integer,primary_key=True)
    quote_id = db.Column(db.Integer, db.ForeignKey('quotes.id'),index=True)
    motivational=db.Column(db.Boolean)
    spiritual=db.Column(db.Boolean)
    love=db.Column(db.Boolean)
    religion=db.Column(db.Boolean)
    success=db.Column(db.Boolean)
    friendship=db.Column(db.Boolean)
    fun=db.Column(db.Boolean)


    def export_data(self):
        # Quotes_data
       return {
           'self_url': self.get_url(),
           'id' : self.id,
           'motivational'  : self.motivational,
           'spiritual'  : self.spiritual,
           'love': self.love,
           'religion':self.religion,
           'success':self.success,
           'friendship':self.friendship,
           'fun':self.fun

       }

"""
class School(db.Model):
    __tablename__='schools'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    address_line1 = db.Column(db.String(64))
    address_line2 = db.Column(db.String(64))
    city = db.Column(db.String(20))
    state = db.Column(db.String(20))
    country = db.Column(db.String(10))
    pincode = db.Column(db.Integer)
    website = db.Column(db.String(20))
    phone = db.Column(db.Integer)
    school_rating = db.Column(db.Float)
    hostel_id = db.Column(db.Integer, db.ForeignKey('hostels.id'),index=True)
    #faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'),index=True)
    latitude = db.Column(db.Float,index=True)
    longitude = db.Column(db.Float,index=True)
    coeducation = db.Column(db.Enum('1','2','3'))
    courses_id = db.Column(db.Integer, db.ForeignKey('courses.id'),index=True)
    library_id = db.Column(db.Integer, db.ForeignKey('library.id'),index=True)
    transport_id = db.Column(db.Integer, db.ForeignKey('transport.id'),index=True)
    sports_id = db.Column(db.Integer, db.ForeignKey('sports.id'),index=True)
    educomp = db.Column(db.Boolean)
    educational_trips = db.Column(db.Boolean)
    ac = db.Column(db.Boolean)
    wifi = db.Column(db.Boolean)
    auditorium = db.Column(db.Boolean)
    cafeteria = db.Column(db.Boolean)
    level = db.Column(db.Enum('Primary','Secondary','Senior-Secondary','Play-School'))
    board = db.Column(db.String(64))
    image_url = db.Column(db.String(512))
    hostel_facility = db.Column(db.Boolean)
    description = db.Column(db.String(64))
    count_review = db.Column(db.Integer)
    mail_id = db.Column(db.String(64))
    city_id = db.Column(db.Integer)
    #basketball = db.Column(db.Boolean)
    #tennis = db.Column(db.Boolean)
    #football = db.Column(db.Boolean)
    #fee_day_id = db.Column(db.Integer , db.ForeignKey('fee_day.id') , index=True)
    #fee_res_id = db.Column(db.Integer , db.ForeignKey('fee_boarding.id') , index=True)

    def set_name(self, name):
        self.name = name

    def get_url(self):
        return url_for('api.getSchoolDetail', id=self.id, _external=True)

    def increment_review_count(self ,data1,data2):
        try:
            self.count_review = data1,
            self.school_rating = data2
        except KeyError as e:
             raise ValidationError('Invalid input ' +e.args[0])
        return self

    def export_data(self):
        #hostel_data = Hostel.query.get_or_404(self.hostel_id)
        return {
            'self_url': self.get_url(),
            'id' : self.id,
            'hostel_id' : self.hostel_id,
            #'facility_id' : self.facility_id,
            'name': self.name,
            'address_line1': self.address_line1,
            'address_line2': self.address_line2,
            'city':self.city,
            'state':self.state,
            'country':self.country,
            'pincode':self.pincode,
            'latitude':self.latitude,
            'longitude':self.longitude,
            'website':self.website,
            'phone':self.phone,
            'coeducation':self.coeducation,
            'rating':self.rating,
            'image_url':self.image_url,
            'count_review':self.count_review
        }
    def import_data(self , data):
        try:
            self.id = data['id'],
            self.name = data['name'],
            self.city=data['city'],
            self.school_rating=data['school_rating']

        except KeyError as e:
            raise ValidationError('Invalid input ' +e.args[0])
        return self



class Entry(db.Model):
    __tablename__ = 'elastic_index'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    city = db.Column(db.String(64))
    school_rating = db.Column(db.Integer)
    wifi = db.Column(db.Boolean)
    ac = db.Column(db.Boolean)
    address_line1 = db.Column(db.String(64))
    address_line2 = db.Column(db.String(64))
    state = db.Column(db.String(64))
    website = db.Column(db.String(64))
    swimming = db.Column(db.Boolean)
    basketball = db.Column(db.Boolean)
    tennis = db.Column(db.Boolean)
    football = db.Column(db.Boolean)
    hostel = db.Column(db.Boolean)
    image_url = db.Column(db.String(128))
    countreview = db.Column(db.String(128))

    def import_data(self , data):
        try:
            self.id = data['id'],
            self.name = data['name'],
            self.city=data['city'],
            self.school_rating=data['school_rating']
            self.wifi = data['wifi']
            self.address_line1 = data['address_line1']
            self.address_line2 = data['address_line2']
            self.state = data['state']
            self.website = data['website']
            self.basketball = data['basketball']
            self.tennis = data['tennis']
            self.football = data['football']
            self.hostel = data['hostel']
            self.swimming = data['swimming']
            self.ac = data['ac']
            self.image_url = data['image_url']
            self.countreview = data['countreview']

        except KeyError as e:
            raise ValidationError('Invalid input ' +e.args[0])
        return self


def after_entry_insert(mapper, connection, target):
    es = Elasticsearch()
    es.index(index="index-1", doc_type="test-1", id=target.id,
             body={"name": target.name, "city": target.city, "school_rating" : target.school_rating,
                   "wifi" : target.wifi, "ac" : target.ac , "address_line1" : target.address_line1,
                   "address_line2" : target.address_line2, "state" : target.state, "website" : target.website,
                   "basketball" : target.basketball, "tennis" : target.tennis,
                   "football" : target.football, "hostel" : target.hostel , "swimming" : target.swimming ,
                   "image_url" : target.image_url , "countreview" : target.countreview} )

def after_entry_update(mapper, connection, target):
    pass

event.listen(Entry, 'after_insert', after_entry_insert)
event.listen(Entry, 'after_update', after_entry_insert)


class Sports(db.Model):
    __tablename__='sports'
    id = db.Column(db.Integer, primary_key=True)
    swimming = db.Column(db.Boolean)
    ground = db.Column(db.Boolean)
    basketball = db.Column(db.Boolean)
    tennis = db.Column(db.Boolean)
    badminton = db.Column(db.Boolean)
    squash = db.Column(db.Boolean)
    horse_riding = db.Column(db.Boolean)
    table_tennis = db.Column(db.Boolean)
    cricket = db.Column(db.Boolean)
    hockey = db.Column(db.Boolean)
    football = db.Column(db.Boolean)
    sports_rating = db.Column(db.Float)
    School = db.relationship('School', backref = 'schools.sports_id', lazy = 'joined')


    def set_name(self, name):
        self.name = name


    def export_data(self):
        #hostel_data = Hostel.query.get_or_404(self.hostel_id)
        return {
            'self_url': self.get_url(),
            'id' : self.id,
            'swimming': self.swimming,
            'ground': self.ground,
            'basketball':self.basketball,
            'tennis':self.tennis,
            'badminton':self.badminton,
            'squash':self.squash,
            'horse_riding':self.horse_riding,
            'table_tennis':self.table_tennis,
            'cricket':self.cricket,
            'hockey' :self.hockey,
            'football':self.football
        }

class Transport(db.Model):
    __tablename__='transport'
    id = db.Column(db.Integer, primary_key=True)
    buses = db.Column(db.Integer)
    bus_ac = db.Column(db.Boolean)
    description = db.Column(db.String(64))
    transport_rating = db.Column(db.Float)
    School = db.relationship('School', backref = 'schools.transport_id', lazy = 'joined')


    def set_name(self, name):
        self.name = name


    def export_data(self):
        #hostel_data = Hostel.query.get_or_404(self.hostel_id)
        return {
            'self_url': self.get_url(),
            'id' : self.id,
            'buses': self.buses,
            'bus_ac': self.bus_ac,
            'description':self.description
        }

class Library(db.Model):
    __tablename__='library'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(64))
    library_rating = db.Column(db.Float)
    books = db.Column(db.Integer)
    journals = db.Column(db.Integer)
    capacity = db.Column(db.Integer)
    School = db.relationship('School', backref = 'schools.library_id', lazy = 'joined')


    def set_name(self, name):
        self.name = name


    def export_data(self):
        #hostel_data = Hostel.query.get_or_404(self.hostel_id)
        return {
            'self_url': self.get_url(),
            'id' : self.id,
            'description': self.description,
            'journals':self.journals,
            'books':self.books,
            'capacity':self.capacity
        }

class Courses(db.Model):
    __tablename__='courses'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(64))
    courses_rating = db.Column(db.Float)
    science=db.Column(db.Boolean)
    commerce=db.Column(db.Boolean)
    humanities=db.Column(db.Boolean)


    School = db.relationship('School', backref = 'schools.courses_id', lazy = 'joined')


    def set_name(self, name):
        self.name = name


    def export_data(self):
        #hostel_data = Hostel.query.get_or_404(self.hostel_id)
        return {
            'self_url': self.get_url(),
            'id' : self.id,
            'description': self.description,
            'commerce':self.commerce,
            'science':self.science,
            'humanities':self.humanities
        }

class Faculty(db.Model):
    __tablename__='faculty'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(64))
    faculty_rating = db.Column(db.Float)
    qualifications = db.Column(db.String(64))
    image_url = db.Column(db.String(64))
    linkedin_url = db.Column(db.String(64))
    school_id=db.Column(db.Integer)

    #School = db.relationship('School', backref = 'schools.faculty_id', lazy = 'joined')


    def set_name(self, name):
        self.name = name


    def export_data(self):
        #hostel_data = Hostel.query.get_or_404(self.hostel_id)
        return {
            'self_url': self.get_url(),
            'id' : self.id,
            'qualifications':self.qualifications,
            'linkedin_url':self.linkedin_url,
            'image_url':self.image_url,
            'description': self.description
        }


class Hostel(db.Model):
    __tablename__ = 'hostels'
    id = db.Column(db.Integer, primary_key=True)
    hostel_rating = db.Column(db.Float)
    name = db.Column(db.String(64), index=True)
    ac_facility = db.Column(db.Boolean)
    capacity = db.Column(db.Integer)
    wifi_facility = db.Column(db.Boolean)
    room_type = db.Column(db.Enum('single','double-sharing','triple-sharing','all'))
    reading_hall=db.Column(db.Boolean)
    image_location = db.Column(db.String(64))
    School = db.relationship('School', backref = 'schools.hostel_id', lazy = 'joined')

    def export_data(self):
        return {
            'id' : self.id,
            'name':self.name,
            'ac_facility':self.ac_facility,
            'capacity': self.capacity,
            'wifi_facility': self.wifi_facility,
            'room_type': self.room_type,
            'reading_hall':self.reading_hall
        }


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    login_id = db.Column(db.String(64), index=True)
    email = db.Column(db.String(64), index=True)
    api_key = db.Column(db.String(64), index=True)
    user_image_url = db.Column(db.String(512),index=True)

    def export_data(self):
        return {
            'id' : self.id,
            'login_id':self.login_id,
            'email':self.email,
            'api_key': self.api_key,
            'user_image_url' : self.user_image_url
        }

    def import_data(self , data):
        try:
            #self.id = data['id'],
            self.login_id = data['login_id'],
            self.email=data['email'],
            self.user_image_url=data['user_image_url']
        except KeyError as e:
             raise ValidationError('Invalid input ' +e.args[0])
        return self


class Review(db.Model):
    __tablename__ = 'review'
    id = db.Column(db.Integer , primary_key = True)
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id'),index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),index=True)
    description = db.Column(db.String(64), index=True)
    school_rating = db.Column(db.Float)
    hostel_rating = db.Column(db.Float)
    cafeteria_rating = db.Column(db.Float)
    sports_rating = db.Column(db.Float)
    transport_rating = db.Column(db.Float)
    faculty_rating = db.Column(db.Float)
    library_rating = db.Column(db.Float)
    courses_rating = db.Column(db.Float)
    timestamp = db.Column(db.String(64))

    def get_url(self):
       return url_for('api.school_review', id=self.id, _external=True)

    def getdes(self):
       return {
           'self_url': self.get_url(),
           'description' : self.description,
           'school_rating':self.school_rating,
           'hostel_rating':self.hostel_rating,
           'cafeteria_rating':self.cafeteria_rating,
           'sports_rating':self.sports_rating,
           'transport_rating':self.transport_rating,
           'faculty_rating':self.faculty_rating,
           'library_rating':self.library_rating,
           'courses_rating':self.courses_rating
       }

    def export_data(self):
        return {
            'id' : self.id,
            'hostel_id':self.hostel_id,
            'faculty_id':self.faculty_id,
            'description':self.description,
            'school_rating':self.school_rating,
            'hostel_rating':self.hostel_rating,
            'cafeteria_rating':self.cafeteria_rating,
            'sports_rating':self.sports_rating,
            'transport_rating':self.transport_rating,
            'faculty_rating':self.faculty_rating,
            'library_rating':self.library_rating,
            'courses_rating':self.courses_rating,
            'timestamp':self.timestamp.getDate()

        }

    def import_data(self , data):
        try:
            self.user_id = data['user_id'],
            self.description=data['description'],
            self.school_id=data['school_id']
            if 'school_rating' in data :
                self.school_rating=data['school_rating'],
            if 'hostel_rating' in data :
                self.hostel_rating=data['hostel_rating'],
            if 'sports_rating' in data :
                self.sports_rating=data['sports_rating'],
            if 'transport_rating' in data :
                self.transport_rating=data['transport_rating'],
            if 'faculty_rating' in data :
                self.faculty_rating=data['faculty_rating'],
            if 'library_rating' in data :
                self.library_rating=data['library_rating'],
            if 'courses_rating' in data :
                self.courses_rating=data['courses_rating']
        except KeyError as e:
            raise ValidationError('Invalid input ' +e.args[0])
        return self    
"""
"""
class FeeDetail_Day(db.Model):
   __tablename__ = 'fee_day'
   id = db.Column(db.Integer, primary_key=True)
   std_1 = db.Column(db.Integer)
   std_2 = db.Column(db.Integer)
   std_3 = db.Column(db.Integer)
   std_4 = db.Column(db.Integer)
   std_5 = db.Column(db.Integer)
   std_6 = db.Column(db.Integer)
   std_7 = db.Column(db.Integer)
   std_8 = db.Column(db.Integer)
   std_9 = db.Column(db.Integer)
   std_10 = db.Column(db.Integer)
   std_11 = db.Column(db.Integer)
   std_12 = db.Column(db.Integer)
   School = db.relationship('School', backref = 'schools.fee_day_id', lazy = 'joined')

   def set_name(self, name):
       self.name = name

   def export_data(self):
       return {
           'id' : self.id,
           "std_1" : self.std_1,
           "std_2" : self.std_2,
           "std_3" : self.std_3,
           "std_4" : self.std_4,
           "std_5" : self.std_5,
           "std_6" : self.std_6,
           "std_7" : self.std_7,
           "std_8" : self.std_8,
           "std_9" : self.std_9,
           "std_10" : self.std_10,
           "std_11" : self.std_11,
           "std_12" : self.std_12

       }

"""
"""class FeeDetail_Boarding(db.Model):
   __tablename__ = 'fee_boarding'
   id = db.Column(db.Integer, primary_key=True)
   std_5 = db.Column(db.Integer)
   std_6 = db.Column(db.Integer)
   std_7 = db.Column(db.Integer)
   std_8 = db.Column(db.Integer)
   std_9 = db.Column(db.Integer)
   std_10 = db.Column(db.Integer)
   std_11 = db.Column(db.Integer)
   std_12 = db.Column(db.Integer)
   School = db.relationship('School', backref = 'schools.fee_res_id', lazy = 'joined')

   def export_data(self):
       return {
           'id' : self.id,
           "std_5" : self.std_5,
           "std_6" : self.std_6,
           "std_7" : self.std_7,
           "std_8" : self.std_8,
           "std_9" : self.std_9,
           "std_10" : self.std_10,
           "std_11" : self.std_11,
           "std_12" : self.std_12

       }

"""

