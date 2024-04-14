import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
import datetime

# with open('scaler.pkl', 'rb') as f:
def main(pathname):
#     scaler = pickle.load(f)
    with open('rqf.pkl', 'rb') as f:
        model = pickle.load(f)
    df = pd.read_excel(pathname)
    # df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    x = df.drop(['Продажи, рубли'], axis=1)
    y = df['Продажи, рубли']
    sales_forecast = model.predict(x)
    print(type(sales_forecast), len(sales_forecast), sep="\n")
    print(len(x))
    current_datetime = datetime.datetime.now()

    # Извлечь текущий год из текущей даты
    year = current_datetime.year
    predictions = dict()
    for week in range(1, 30):
        # Получаем первый день недели для данной недели в году
        first_day_of_week = datetime.date(year, 1, 1) + datetime.timedelta(weeks=week-1, days=-datetime.date(year, 1, 1).weekday())
        predictions[first_day_of_week] = sales_forecast[week - 1]
    data = pd.DataFrame.from_dict(predictions, orient='index')
    return data.to_excel('predictions.xlsx')
