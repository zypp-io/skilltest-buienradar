import pandas as pd
import json
from urllib import request
import hashlib
import sqlalchemy
from data.schema import create_database, StationMeasurements, WeatherStations
from data.erm import create_erm


class DataIngestion:
    """
    Class to ingest data into a SQL database
    """

    def __init__(self, url: str, database_path: str):
        self.url = url
        self.database_path = database_path

    def load_data(self) -> dict:
        """
        Load json data given a url
        """
        with request.urlopen(self.url) as url_object:
            data = json.load(url_object)

        return data

    def generate_unique_id(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Generate unique measurement ID by hashing Station ID & timestamp
        """
        return (df["stationid"].astype(str) + df["timestamp"]).apply(lambda x: hashlib.md5(x.encode("utf-8")).hexdigest())

    def parse_measurements_data(self, data: list) -> pd.DataFrame:
        """
        Parse the measurements data of the weather stations.
        Generates measurementid from stationid & timestamp.

        Returns dataframe with columns:

        - measurementid
        - timestamp
        - temperature
        - groundtemperature
        - feeltemperature
        - windgusts
        - windspeedBft
        - humidity
        - precipitation
        - sunpower
        - stationid
        """
        df = pd.DataFrame(data)
        df["measurementid"] = self.generate_unique_id(df)
        cols = [
            "measurementid",
            "timestamp",
            "temperature",
            "groundtemperature",
            "feeltemperature",
            "windgusts",
            "windspeedBft",
            "humidity",
            "precipitation",
            "sunpower",
            "stationid",
        ]
        df = df[cols]

        return df

    def parse_stations_data(self, data: list) -> pd.DataFrame:
        """
        Parse the stations data of the weather stations.

        Returns dataframe with columns:

        - stationid
        - stationname
        - lat
        - lon
        - regio
        """
        df = pd.DataFrame(data)
        cols = [
            "stationid",
            "stationname",
            "lat",
            "lon",
            "regio",
        ]
        df = df[cols]

        return df

    def create_sql_database(self, table, df: pd.DataFrame):
        """
        Create SQL database

        :param table: SQLalchemy declarative base of a table
        :param df: dataframe to insert
        """
        # Defining the Engine
        engine = sqlalchemy.create_engine('sqlite:///data/database.db', echo=True)

        records = df.to_dict(orient='records')
        statement = sqlalchemy.insert(table).values(records)

        with engine.connect() as conn:
            conn.execute(statement)
            conn.commit()

    def run(self):
        # Load data
        data = self.load_data()

        # Parse data
        data_measurements = self.parse_measurements_data(data["actual"]["stationmeasurements"])
        data_stations = self.parse_stations_data(data["actual"]["stationmeasurements"])

        # Create SQL database
        create_database(self.database_path)
        self.create_sql_database(table=StationMeasurements, df=data_measurements)
        self.create_sql_database(table=WeatherStations, df=data_stations)

        # Create ERM
        create_erm()


if __name__ == "__main__":
    ingestion = DataIngestion(url="https://json.buienradar.nl",
                              database_path="data/database.db")
    ingestion.run()

