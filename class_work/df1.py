# import pandas as pd
# df=pd.DataFrame(columns=['URL', 'Article_title', 'Article_description'])
# print (df)

import pandas as pd
data = {
    'SapId': ['001','002'],
    'Fname': ['Adi','Saakshi',],
    'Lname': ['Bhatt','Tewari'],
    'subject': ['Python','Math'],
    'teacher': ['Sajid','Gayatri'],
    'Marks': ['60','80']
}
df = pd.DataFrame(data)
df.index.name = 'Row'
print(df)
