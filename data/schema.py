import sqlalchemy
from sqlalchemy import Integer, String, Column, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class StationMeasurements(Base):
    __tablename__ = "station_measurements"

    measurementid = Column(String, primary_key=True)
    stationid = Column(Integer, ForeignKey("weather_stations.stationid"), primary_key=True)
    timestamp = Column(String, primary_key=True)
    temperature = Column(Numeric)
    groundtemperature = Column(Numeric)
    feeltemperature = Column(Numeric)
    windgusts = Column(Numeric)
    windspeedBft = Column(Numeric)
    humidity = Column(Numeric)
    precipitation = Column(Numeric)
    sunpower = Column(Numeric)


class WeatherStations(Base):
    __tablename__ = "weather_stations"

    stationid = Column(Integer, primary_key=True)
    stationname = Column(String)
    lat = Column(Numeric)
    lon = Column(Numeric)
    regio = Column(String)


def create_database(database_path: str):
    engine = sqlalchemy.create_engine(f"sqlite:///{database_path}", echo=True)
    Base.metadata.create_all(engine)
