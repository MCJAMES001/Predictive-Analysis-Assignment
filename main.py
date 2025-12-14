import pandas as pd
import numpy as np

Weather = pd.read_csv("Weather_data.csv")
print(Weather.head())

print(Weather.describe())

print(Weather.info())