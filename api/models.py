from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy.sql.expression import null
from .database import Base

class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True)
    word = Column(String, nullable=False)
    gender = Column(String, nullable=True)
    article = Column(String, nullable=True)
    word_type = Column(String, nullable=True)
    translation = Column(Text)
    example_sentences = Column(Text)
    usage_frequency = Column(Integer)
    ipa = Column(String)
    verb_auxiliary = Column(String)
    difficulty_level = Column(String)
    irregular = Column(Boolean)
    present_3s = Column(String)
    past_perfect = Column(String)
    preterite = Column(String)
    frequency_scale = Column(Integer)