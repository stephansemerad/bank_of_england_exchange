#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from pathlib import Path
from sqlalchemy import create_engine, Column, Numeric, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker

# * ─── Database specifications
Base = declarative_base()


engine = create_engine('sqlite:///database.db', echo = False)
Session = sessionmaker(bind=engine)
Base = declarative_base()

session = Session()


# * ─── FX Table
class FX(Base):
    __tablename__ = "fx"
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    rate = Column(String)
    symbol = Column(String)

    def __repr__(self):
        return f"{self.symbol} {self.date} {self.rate}"

Base.metadata.create_all(engine)
