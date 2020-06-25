import pandas as pd

pd.set_option('max_rows', 5)
import numpy as np

reviews = pd.read_csv("winemag-data-130k-v2.csv")
print(reviews.dtypes)