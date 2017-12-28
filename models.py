from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#TODO: Account for connection errors or database validation errors
#TODO: See if class can be written better design-wise

#This file facilitates connecting to the database, creating objects
#   that map to RDBMS tables, and CRUD operations
#Replace dbPath with user:password@path/db_name
dbPath = 'root:sexy6621back@127.0.0.1:3306/grocery_items.db'
Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://%s' % dbPath,
                       echo=True)
metadata = MetaData(bind=engine)

def connectToDatabase():
    session = loadSession()
    print("Connected to Database")

class Items(Base):
    __table__ = Table('items', metadata, autoload=True)

#        def __str__(self):
#            "<Item>: %s, %s, %s" % (self.title, self.brand, self.price_desc)

def loadSession():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def addItem(session, title, brand=None, price=None, priceDesc=None):
    item = Items(title=title, brand=brand, price=price, price_desc=priceDesc)
    session.add(item)

def closeSession(session):
    session.commit()
