import pandas as pd
import os

def rfm_segmentation(df):
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    snapshot = df['InvoiceDate'].max() + pd.Timedelta(days=1)
    rfm = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (snapshot - x.max()).days,
        'InvoiceNo': 'count',
        'TotalAmount': 'sum'
    })
    rfm.columns = ['Recency', 'Frequency', 'Monetary']
    return rfm

if __name__ == "__main__":
    if not os.path.exists('data/sales.csv'):
        print('Place data/sales.csv with columns InvoiceDate, InvoiceNo, CustomerID, TotalAmount')
    else:
        df = pd.read_csv('data/sales.csv')
        rfm = rfm_segmentation(df)
        print(rfm.head())
