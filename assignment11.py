import numpy as np
import pandas as pd

np.random.seed(42)

numbers = np.random.randint(1, 101, 10)

series = pd.Series(numbers)

print(series)