import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

data = pd.read_csv('./world-development-indicators/Indicators.csv')

data.shape

countries = data['CountryName'].unique().tolist()
indicators = data['IndicatorName'].unique().tolist()

# Picks years of choice
yearsFilter = [2010, 2011, 2012, 2013, 2014]

