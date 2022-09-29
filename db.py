from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Engine,
engine =create_engine('sqlite:///database/tareas.db', connect_args={'check_same_thread': False})

# Sessión
Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()