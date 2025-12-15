import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns


Weather = pd.read_csv("Weather_Data.csv")
print(Weather.head())

print(Weather.describe())

print(Weather.info())

Weather.dropna(inplace=True)

print(Weather.head())