import pandas as pd

def load_data(path='../data/cleaned_data.csv'):
    # Load with MultiIndex columns
    data = pd.read_csv(path, header=[0, 1], index_col=0, parse_dates=True)
    data.index.name = 'Date'

    # Rename the columns explicitly
    new_cols = []
    for col in data.columns:
        if 'price' in col[0].lower():
            new_cols.append('price')
        elif 'log_return' in col[0].lower():
            new_cols.append('log_return')
        else:
            new_cols.append('_'.join(col).strip())

    data.columns = new_cols
    data = data.sort_index()
    return data
