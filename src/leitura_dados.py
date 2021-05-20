import pandas as pd
import pathlib

def ler_dados():
    filepath = pathlib.Path(__file__).parent/'pokemon.csv'
    return pd.read_csv(filepath).drop(773)