from arch import arch_model
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def fit_garch_model(data, p=1, q=1):
    model = arch_model(data['log_return'], vol='Garch', p=p, q=q, rescale=False)
    result = model.fit(disp='off')
    return result

def forecast_garch(result, steps=5):
    forecasts = result.forecast(horizon=steps)
    variance_forecast = forecasts.variance.values[-1, :]  # Assuming you're interested in this
    
    # Plot using matplotlib
    plt.figure(figsize=(10, 5))
    plt.plot(variance_forecast, marker='o', linestyle='-')
    plt.title(f"{steps}-Day Ahead Volatility Forecast")   
    plt.xlabel("Day")
    plt.ylabel("Forecasted Variance")
    plt.grid(True)
    plt.show()
    return forecasts

def get_aic_bic(data, max_p=6, max_q=6):
    aic_values = []
    bic_values = []
    pq_combinations = []
    
    for p in range(1, max_p + 1):
        for q in range(1, max_q + 1):
            try:
                model = arch_model(data, vol='Garch', p=p, q=q, rescale=False)
                results = model.fit(disp='off')
                aic_values.append(results.aic)
                bic_values.append(results.bic)
                pq_combinations.append((p, q))
            except Exception as e:
                print(f"Model GARCH({p}, {q}) failed: {str(e)}")
                aic_values.append(np.inf)
                bic_values.append(np.inf)
    
    return pq_combinations, aic_values, bic_values

def plot_ranking(aic_values, bic_values, pq_combinations):
    rankings = pd.DataFrame({
        'Combination': pq_combinations,
        'AIC': aic_values,
        'BIC': bic_values
    })

    # Sort rankings by AIC and BIC
    rankings.sort_values(by='AIC', inplace=True)
    aic_ranking = rankings.reset_index(drop=True)
    
    rankings.sort_values(by='BIC', inplace=True)
    bic_ranking = rankings.reset_index(drop=True)

    plt.figure(figsize=(14, 7))

    # Plot AIC rankings
    plt.plot(range(len(aic_ranking)), aic_ranking['AIC'], marker='o', label='AIC Ranking', color='b')
    for i, txt in enumerate(aic_ranking['Combination']):
        plt.annotate(txt, (i, aic_ranking['AIC'][i]), textcoords="offset points", xytext=(-5,5), ha='right', fontsize=8)
    
    # Plot BIC rankings
    plt.plot(range(len(bic_ranking)), bic_ranking['BIC'], marker='o', label='BIC Ranking', color='r')
    for i, txt in enumerate(bic_ranking['Combination']):
        plt.annotate(txt, (i, bic_ranking['BIC'][i]), textcoords="offset points", xytext=(-5,5), ha='left', fontsize=8)

    plt.title("Model Selection Ranking by AIC and BIC")
    plt.xlabel("Rank")
    plt.ylabel("Criterion")
    plt.legend()
    plt.grid(True)
    plt.show()