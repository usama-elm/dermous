from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Database_url = "sqlite:///../data/words_database.db"
Engine = create_engine(Database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)
Base = declarative_base()
