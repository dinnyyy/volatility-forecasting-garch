from statsmodels.stats.diagnostic import acorr_ljungbox, het_arch
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np

def ljung_box_test(residuals, lags=10):
    lb_test = acorr_ljungbox(residuals, lags=lags, return_df=True)
    return lb_test

def arch_lm_test(residuals, lags=10):
    arch_test = het_arch(residuals, nlags=lags)
    return {
        "LM Stat": arch_test[0],
        "p-value": arch_test[1],
        "F-Stat": arch_test[2],
        "F p-value": arch_test[3]
    }

def forecast_errors(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    return {"MSE": mse, "MAE": mae, "RMSE": rmse}