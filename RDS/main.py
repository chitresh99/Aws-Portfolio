import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


DB_USERNAME = 'your_username'
DB_PASSWORD = 'your_password'
DB_HOST = 'your-rds-endpoint.rds.amazonaws.com'
DB_PORT = '3306'
DB_NAME = 'your_database_name'


CONNECTION_STRING = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


engine = create_engine(CONNECTION_STRING)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(120), unique=True)

    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}')>"


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

#operations

# Create a new user
new_user = User(name='John Doe', email='john@example.com')
session.add(new_user)
session.commit()


users = session.query(User).all()
for user in users:
    print(user)


user_to_update = session.query(User).filter_by(name='').first()
if user_to_update:
    user_to_update.email = ''
    session.commit()


user_to_delete = session.query(User).filter_by(name='John Doe').first()
if user_to_delete:
    session.delete(user_to_delete)
    session.commit()


session.close()