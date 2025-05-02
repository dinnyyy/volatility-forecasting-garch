import matplotlib.pyplot as plt
import seaborn as sns

def plot_log_returns(data):
    plt.figure(figsize=(12,6))
    plt.plot(data['log_return'])
    plt.title('Log Returns')
    plt.show()

def plot_squared_returns(data):
    plt.figure(figsize=(12,6))
    plt.plot(data['log_return']**2)
    plt.title('Squared Log Returns')
    plt.show()