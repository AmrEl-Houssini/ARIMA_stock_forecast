from math import sqrt
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error


def one_step_prediction(df, best_model):
    df_values = df.values
    size = int(len(df_values) * 0.66)
    train, test = df_values[0:size], df_values[size:len(df_values)]
    history = [x for x in train]
    predictions = list()
    for t in range(len(test)):
        model = ARIMA(history, order=best_model)
        model_fit = model.fit(disp=0)
        output = model_fit.forecast()
        yhat = output[0]
        predictions.append(yhat)
        obs = test[t]
        history.append(obs)
        print('predicted=%f, expected=%f' % (yhat, obs))
    error = mean_squared_error(test, predictions)
    print("error : ", error)
    predictions_series = pd.Series(predictions)

    # prediction vs actual
    fig = plt.figure(figsize=(20, 15))
    plt.subplot(211)
    plt.plot(test, color='red', label='Original Data')
    plt.plot(predictions, color='blue', label='Predictions')
    plt.legend()
    return predictions_series, test


def accuracy_metrics(predictions_series, test):
    # Accuracy metrics
    mae = mean_absolute_error(predictions_series, test)
    mse = mean_squared_error(predictions_series, test)
    rmse = sqrt(mse)
    print("MAE value --> ", mae)
    print("MSE value --> ", mse)
    print("RMSE value --> ", rmse)









