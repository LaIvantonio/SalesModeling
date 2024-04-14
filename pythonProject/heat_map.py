from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_excel("1train.xlsx")

corr_matrix = df.corr()
print(corr_matrix)