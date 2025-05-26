filepath=r"C:\Users\dirisala.maheswari\NLP\Sentiment Analysis\TestReviews.csv"

import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    df.dropna(subset=["review"], inplace=True)
    return df
