import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.linear_model import Ridge
from  sklearn.linear_model import Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
import xgboost as xgb
import pickle

df = pd.read_excel("2train_filled.xlsx")
# scaler = StandardScaler()
# df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
# with open('scaler.pkl', 'wb') as f:
#     pickle.dump(scaler, f)
x = df.drop(['Продажи, рубли'], axis=1)
y = df['Продажи, рубли']
print(df.info())

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = LinearRegression(fit_intercept=True)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

sales_forecast = model.predict(x_test)
print(f'Mean squared error linear: {mean_squared_error(y_test, y_pred)}')
print(f'R-квадрат для линейной регрессии: {r2_score(y_test, y_pred)}')

with open('liner.pkl', 'wb') as f:
    pickle.dump(model, f)
print(f"{'_':_^100}")


model_ridge = Ridge(alpha=0.5)
model_ridge.fit(x_train, y_train)
y_pred_ridge = model_ridge.predict(x_test)
print(f'Mean squared error ridge: {mean_squared_error(y_test, y_pred_ridge)}')
print(f'R-квадрат для ridge: {r2_score(y_test, y_pred_ridge)}')
with open('ridge.pkl', 'wb') as f:
    pickle.dump(model_ridge, f)

print(f"{'_':_^100}")
model_lasso = Lasso(alpha=0.1)
model_lasso.fit(x_train, y_train)

# Прогнозирование продаж по неделям с помощью Lasso регрессии
forecast_lasso_weekly = model_lasso.predict(x_test)
print(f'Mean squared error lasso: {mean_squared_error(y_test, forecast_lasso_weekly)}')
print(f'R-квадрат для lasso: {r2_score(y_test, forecast_lasso_weekly)}')
with open('lasso.pkl', 'wb') as f:
    pickle.dump(model_lasso, f)

print(f"{'_':_^100}")


model_rf = RandomForestRegressor(n_estimators=1000, random_state=400)
model_rf.fit(x_train, y_train)

# Прогнозирование продаж по неделям с помощью RandomForestRegressor
forecast_rf_weekly = model_rf.predict(x_test)
print(f'Mean squared error random forest: {mean_squared_error(y_test, forecast_rf_weekly)}')
print(f'R-квадрат для random forest: {r2_score(y_test, forecast_rf_weekly)}')
with open('rqf.pkl', 'wb') as f:
    pickle.dump(model_rf, f)
print(f"{'_':_^100}")


model_knn = KNeighborsRegressor(n_neighbors=10)
model_knn.fit(x_train, y_train)

# Прогнозирование продаж по неделям с помощью KNeighborsRegressor
forecast_knn_weekly = model_knn.predict(x_test)


print(f'Mean squared error knn: {mean_squared_error(y_test, forecast_knn_weekly)}')
print(f'R-квадрат для knn: {r2_score(y_test, forecast_knn_weekly)}')
print(f"{'_':_^100}")


param_grid = {
    'max_depth': [3, 5, 7],
    'n_estimators': [50, 100, 150],
    'learning_rate': [0.05, 0.1, 0.3]
}
grid_search = GridSearchCV(estimator=xgb.XGBRegressor(objective='reg:squarederror'), param_grid=param_grid, cv=3, scoring='neg_mean_squared_error')
grid_search.fit(x_train, y_train)
print("Наилучшие гиперпараметры для XGBoost:", grid_search.best_params_)
best_xgb_model = grid_search.best_estimator_
y_pred_best_xgb = best_xgb_model.predict(x_test)
mse_best_xgb = mean_squared_error(y_test, y_pred_best_xgb)
r2_best_xgb = r2_score(y_test, y_pred_best_xgb)
print("Среднеквадратичная ошибка (MSE) лучшего XGBoost:", mse_best_xgb)
print("R-квадрат для лучшего XGBoost:", r2_best_xgb)
with open('xgb.pkl', 'wb') as f:
    pickle.dump(best_xgb_model, f)

