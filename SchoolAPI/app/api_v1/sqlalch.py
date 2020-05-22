import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Sqlal:
    engine = None
    Session = None

    @staticmethod
    def init(app):                    #Enter here the username and pass as well as the name of the db
        try:
            Sqlal.engine = create_engine('mysql+pymysql://abhi:abhi@localhost:3306/dbname' , paramstyle = 'format' , isolation_level = "READ UNCOMMITTED")

            Sqlal.Session = sessionmaker(bind = Sqlal.engine)

        except Exception as exception:
            print exception




