import pandas as pd
import numpy as np
import random
import string
np.random.seed(42)
n=10000
data={
    'user_age':np.random.randint(10,60,n),
    'device_type':np.random.choice(
        ['mobile','desktop','tablet'],n
    ),
    'time_of_day':np.random.choice(
        ['morning','afternoon','evening','night'],n
    ),
    'ad_category':np.random.choice(
        ["tech","fashion","finance","gaming","educat"],n
    ),
    "placement":np.random.choice(
        ['homepage','sidebar','search','video'],n
    ),
    'past_ctr':np.round(
        np.random.uniform(0.01,0.30,n),2
    ),
    'session_duration':np.random.randint(10,600,n),
    "pages_visited":np.random.randint(1,20,n)
}
df=pd.DataFrame(data)

click_probability=(
(df['past_ctr']*2)+(df['session_duration']/1000)+(df["pages_visited"]/50)
)

df['clicked']=[
    1 if random.random()<prob else 0
    for prob in click_probability
]

#saving my dataset
df.to_csv("ctr_prediction_dataset.csv",index=False)

print(df.head())
print("Dataset created successfully")
print(df.shape)