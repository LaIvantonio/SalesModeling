import pandas as pd
from pandas import DataFrame
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import numpy as np  #импортируем numpy
from sklearn.model_selection import StratifiedShuffleSplit
df = pd.read_excel("1train.xlsx")

# df['Продажи, рубли'] = df['Продажи, рубли'].astype('int64') // 10**9
# df['Статистика заболеваемости'] = df['Статистика заболеваемости'].astype('int64') // 10**9
# df['(1)ТВ, рубли'] = df['(1)ТВ, рубли'].astype('int64') // 10**9
print(df['(3)ТВ, рубли'].info())
print(f"{'_':_^100}")
print(df.info())
df_put = SimpleImputer(missing_values=np.nan, strategy='mean').fit(df)
df_filled = pd.DataFrame(df_put.fit_transform(df), columns=df.columns)

