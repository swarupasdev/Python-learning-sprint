import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

df = pd.read_csv("ctr_prediction_dataset.csv")

print(df.head())
print(df.shape)

x = df.drop("clicked",axis=1)
y = df["clicked"]

print(x.head())
print(y.head())

categorical_features=[
    "device_type",
    "time_of_day",
    "ad_category",
    "placement"
]
numerical_features=[
    "user_age",
    "past_ctr",
    "session_duration",
    "pages_visited"
]
preprocessor = ColumnTransformer(
    transformers=[

    ]
)