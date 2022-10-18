import pandas as pd
net = pd.read_csv('share-of-individuals-using-the-internet.csv')
life = pd.read_csv('life-expectancy.csv', skiprows=3)
life = pd.melt(life, 'Country Code', [str(x) for x in range(1990,2018)])
life['variable'] = [int(x) for x in life['variable']]
res = pd.merge(net, life, how='inner', left_on=['Code','Year'], right_on=['Country Code','variable'])[['Entity','Code','Year','Individuals using the Internet (% of population)','value']].rename(columns={'Individuals using the Internet (% of population)': 'InternetUsage', 'value': 'LifeExpectancy'})
res.to_csv('datavis2.csv')
