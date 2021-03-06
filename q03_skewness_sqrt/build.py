# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')

def skewness_sqrt(df):
    df['GrLivArea'] = np.sqrt(df['GrLivArea'])
    skewness_grLiv = skew(df['GrLivArea'])
    df['SalePrice'] = np.sqrt(df['SalePrice'])
    skewness_sp = skew(df['SalePrice'])
    return skewness_grLiv,skewness_sp
