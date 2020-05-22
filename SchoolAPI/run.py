import os
from app import create_app, db
from app.api_v1 import api
"""from app.api_v1.city import city_list
from app.api_v1.school_review import schoolreview
from app.api_v1.course_info import courseinfo
#from app.api_v1.edit_review import editreview
from app.api_v1.faculty_info import facultyinfo
from app.api_v1.fee_info import feeinfo
from app.api_v1.hostel_detail import hosteldetail
from app.api_v1.images import image
from app.api_v1.library_info import libraryinfo
from app.api_v1.new_user import newuser
from app.api_v1.school_detail import schooldetail
from app.api_v1.send_query import sendquery
from app.api_v1.sports_info import sportsinfo
from app.api_v1.submit_review import submitreview
from app.api_v1.transport_info import transportinfo
from app.api_v1.elastic_search import es
from app.api_v1.contact_us import contact
from app.api_v1.compare_data import compare"""
from app.api_v1.school import get_Quotes
from flask.ext.script import Manager, Shell
#from flask.ext.cors import CORS

app = create_app(os.getenv('FLASK_CONFIG') or 'development')
#CORS(app,resources={r"*": {"origins": "*"}})

"""app.register_blueprint(city_list)
app.register_blueprint(schoolreview)
app.register_blueprint(courseinfo)
#app.register_blueprint(editreview)
app.register_blueprint(facultyinfo)
app.register_blueprint(feeinfo)
app.register_blueprint(hosteldetail)
app.register_blueprint(image)
app.register_blueprint(libraryinfo)
app.register_blueprint(newuser)
app.register_blueprint(schooldetail)
app.register_blueprint(sendquery)
app.register_blueprint(sportsinfo)
app.register_blueprint(submitreview)
app.register_blueprint(transportinfo)
app.register_blueprint(contact)
app.register_blueprint(es)
app.register_blueprint(compare)"""
app.register_blueprint(get_Quotes)



if __name__ == '__main__':
    
    manager = Manager(app)

    with app.app_context():
        db.create_all()

    manager.run()

