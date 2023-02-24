import pandas as pd

data = pd.read_excel('Credentials.xlsx')
users = data.values.tolist()

username, password = users[0]
