import pandas as pd

df_crash = pd.read_csv("C:/Users/jiho3/Downloads/Motor_Vehicle_Collisions_-_Crashes.csv")

df_crash['CRASH_DATE_FORMATTED'] = pd.to_datetime(df_crash['CRASH DATE']).dt.strftime('%Y/%m/%d')
df_crash['CRASH_TIME_HH'] = df_crash['CRASH TIME'].str.pad(width=5, side='left', fillchar='0')
df_crash = df_crash[(df_crash['CRASH_TIME_HH'].between("00:00","06:00")) & (df_crash['BOROUGH'].isin(['MANHATTAN']))]\
                                              .groupby(['CRASH_DATE_FORMATTED','CRASH_TIME_HH']).agg(TOTAL_INJURED=pd.NamedAgg(column='NUMBER OF PERSONS INJURED',aggfunc='max')
                                                                                                    ,TOTAL_KILLED=pd.NamedAgg(column='NUMBER OF PERSONS KILLED',aggfunc='max'))

print(df_crash)