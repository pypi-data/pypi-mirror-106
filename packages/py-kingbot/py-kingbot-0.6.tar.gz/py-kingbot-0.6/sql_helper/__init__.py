import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from uti.confi import Var

def start() -> scoped_session:
    dbi_uri=Var.DB_URL
    dbi_uri="postgresql://"+dbi_uri[dbi_uri.index("//")+1:len(dbi_uri)]
    engine = create_engine()
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))

try:
    BASE = declarative_base()
    SESSION = start()
except AttributeError as e:
    print(
        "DB_URI is not configured. Features depending on the database might have issues."
    )
    print(str(e))
