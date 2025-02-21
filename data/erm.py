from sqlalchemy_data_model_visualizer import generate_data_model_diagram, add_web_font_and_interactivity
from data.schema import StationMeasurements, WeatherStations


def create_erm(loc="data"):
    """
    Create ERM from the database

    TODO: I couldn't get the ForeignKey relation to show in the ERM
    """
    models = [StationMeasurements, WeatherStations]
    output_file_name = f"{loc}/data_model_diagram"
    generate_data_model_diagram(models, output_file_name)
    add_web_font_and_interactivity(f"{loc}/data_model_diagram.svg", f"{loc}/data_model_diagram.svg")
