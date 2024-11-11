import logging
import pandas as pd
from zenml import step


class IngestData:
    def __init__(self, data_path: str):
        self.data_path = data_path
        
    def get_data(self):
        logging.info(f"Ingesting data from {self.data_path}")
        
        # Charger les données en spécifiant des paramètres pour garantir que toutes les colonnes soient ingérées
        try:
            pd.set_option('display.max_columns', None)  # Permet d'afficher toutes les colonnes
            df = pd.read_csv(self.data_path, sep=',', encoding='utf-8')  # Ajustez sep si nécessaire
            return df
        except pd.errors.ParserError as e:
            logging.error(f"Parsing error: {e}")
            raise e
        except Exception as e:
            logging.error(f"Error while reading the CSV file: {e}")
            raise e
    
    
@step
def ingest_df(data_path: str) -> pd.DataFrame:
    """
    Ingesting the data from the data_path. 
    
    Args:
        data_path: path to the data
    Returns:
        pd.DataFrame: the ingested data
    """
    try:
        ingest_data = IngestData(data_path)
        df = ingest_data.get_data()
        return df
    except Exception as e:
        logging.error(f"Error while ingesting data: {e}")
        raise e
