import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import numpy as np

def preprocess_time(time_str):
    # Convert time like '12:00:00 AM' to minutes from midnight
    from datetime import datetime
    dt = datetime.strptime(time_str, '%I:%M:%S %p')
    return dt.hour * 60 + dt.minute

def load_and_train_model(csv_path):
    df = pd.read_csv(csv_path).dropna()

    # Convert Time to numeric
    df['Time'] = df['Time'].apply(preprocess_time)

    # Features and target
    X = df.drop('Traffic Situation', axis=1)
    y = df['Traffic Situation']

    # One-hot encode 'Day of the week'
    categorical_features = ['Day of the week']
    numeric_features = [col for col in X.columns if col not in categorical_features]

    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(), categorical_features),
        ],
        remainder='passthrough'
    )

    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
    ])

    model.fit(X, y)
    return model

def predict(model, input_dict):
    # Convert time input to numeric
    input_dict['Time'] = preprocess_time(input_dict['Time'])
    input_df = pd.DataFrame([input_dict])
    return model.predict(input_df)[0]
