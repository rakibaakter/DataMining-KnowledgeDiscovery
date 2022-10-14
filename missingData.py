import pandas as pd
import re
df = pd.read_csv('data.csv')
# fiil the missing Calories with its mean value
meanCal = df["Calories"].mean()
df["Calories"].fillna(meanCal, inplace = True)
#drop all the duplicates value 
df.drop_duplicates(inplace = True)
bfill = "1000"  #boundary fill for noisy data
for key,val in enumerate(df['Maxpulse']):
    if(re.search("^[0-9]+(\.[0-9]+)?", val)):
        pass
    else:
        df.loc[key,'Maxpulse'] = bfill
print(df.to_string())