from data_analysis import DataAnalysis
from data_ingestion import DataIngestion
from data_visualization import DataVisualization


def main():
    Ingestion = DataIngestion(url="https://json.buienradar.nl",
                              database_path="data/database.db")
    Ingestion.run()

    Analysis = DataAnalysis()
    Analysis.run()

    Visualization = DataVisualization()
    Visualization.run()


if __name__ == "__main__":
    main()
