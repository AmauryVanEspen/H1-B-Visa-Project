import pandas as pd
import numpy as np
from clean import returnClean

h1b_data = returnClean()
X = h1b_data.drop('CASE_STATUS', axis=1)
Y = h1b_data['CASE_STATUS']
