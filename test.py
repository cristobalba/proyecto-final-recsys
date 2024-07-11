import pandas as pd
from sklearn.model_selection import train_test_split
from scipy.sparse import coo_matrix
from implicit.als import AlternatingLeastSquares
import numpy as np

# Load the dataset
df = pd.read_csv('data/myanime_600K.csv')
df = df.rename(columns={'anime_id': 'item_id'})

# Preprocess the data
df['rating'] = df['rating'].apply(lambda x: 1 if x >= 7 else 0)

# Split the data into training and test sets
train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)

# Create a sparse matrix for ALS training
sparse_item_user_train = coo_matrix((train_data['rating'].astype(float),
                                     (train_data['item_id'], train_data['user_id'])))

# Create a sparse matrix for ALS test
sparse_item_user_test = coo_matrix((test_data['rating'].astype(float),
                                    (test_data['item_id'], test_data['user_id'])))

