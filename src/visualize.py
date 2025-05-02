import matplotlib.pyplot as plt

def plot_log_returns(data):
    plt.figure(figsize=(10, 4))
    plt.plot(data['log_return'])
    plt.title("Log Returns")
    plt.xlabel("Date")
    plt.ylabel("Log Return")
    plt.tight_layout()
    plt.show()

def plot_squared_returns(data):
    plt.figure(figsize=(10, 4))
    plt.plot(data['log_return'] ** 2)
    plt.title("Squared Log Returns")
    plt.xlabel("Date")
    plt.ylabel("Squared Log Return")
    plt.tight_layout()
    plt.show()