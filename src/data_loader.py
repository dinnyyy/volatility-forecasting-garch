import pandas as pd

def load_data(path='../data/cleaned_data.csv'):
    data = pd.read_csv(path, header=[0, 1], index_col=0, parse_dates=True)
    data.index.name = 'Date'  # Optional: name the index for clarity

    # Flatten multi-index columns for easier access: ('Price', '^GSPC') -> 'Price_^GSPC'
    data.columns = [f'{a}_{b}' for a, b in data.columns]
    return data