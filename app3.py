from nicegui import ui
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base,sessionmaker
engine = create_engine('sqlite:///people.db')
Base = declarative_base()
class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)

Base.metadata.create_all(engine)

Session=sessionmaker(bind=engine)
session=Session()

all_people=session.query(Person).all()
session.close()

columns = [
    {'name': 'id', 'label': 'ID', 'field': 'id'},
    {'name': 'firstname', 'label': 'Firstname', 'field': 'firstname'},
    {'name': 'lastname', 'label': 'Lastname', 'field': 'lastname'},
    {'name': 'age', 'label': 'Age', 'field': 'age'},
]
rows=[]
for p in all_people:
    d1=dict()
    d1['id']=p.id
    d1['firstname']=p.firstname
    d1['lastname']=p.lastname
    d1['age']=p.age
    rows.append(d1)
    
print(rows)
ui.table(columns=columns, rows=rows, row_key='name')
ui.run()