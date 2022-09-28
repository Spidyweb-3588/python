import pandas as pd
pd.set_option('display.max_columns', None)
df_crash = pd.read_csv("C:/Users/JIHO PARK/Downloads/Motor_Vehicle_Collisions_-_Crashes.csv")

df_crash['CRASH_DATE_FORMATTED'] = pd.to_datetime(df_crash['CRASH DATE']).dt.strftime('%Y/%m/%d')
df_crash['CRASH_TIME_HH'] = df_crash['CRASH TIME'].str.pad(width=5, side='left', fillchar='0')
df_crash_losses = df_crash[(df_crash['CRASH_TIME_HH'].between("00:00","06:00")) & (df_crash['BOROUGH'].isin(['MANHATTAN']))]\
                                              .groupby(['CRASH_DATE_FORMATTED','CRASH_TIME_HH'],as_index=False).agg(TOTAL_INJURED=pd.NamedAgg(column='NUMBER OF PERSONS INJURED',aggfunc='max')
                                                                                                                     ,TOTAL_KILLED=pd.NamedAgg(column='NUMBER OF PERSONS KILLED',aggfunc='max'))
df_crash_losses['MAX_INJURED_DESC_RN'] = df_crash_losses.groupby('CRASH_DATE_FORMATTED',as_index=False)['TOTAL_INJURED'].rank(method='first', ascending=False).astype('int')
df_crash_losses['MAX_KILLED_DESC_RN'] = df_crash_losses.groupby('CRASH_DATE_FORMATTED',as_index=False)['TOTAL_KILLED'].rank(method='first', ascending=False).fillna(0).astype('int')
df_crash_or = df_crash_losses[((df_crash_losses['MAX_INJURED_DESC_RN'] <= 1) | (df_crash_losses['MAX_KILLED_DESC_RN'] <= 1))]
df_crash_or = df_crash_or[['CRASH_DATE_FORMATTED','CRASH_TIME_HH','TOTAL_INJURED','TOTAL_KILLED','MAX_INJURED_DESC_RN','MAX_KILLED_DESC_RN']]
df_crash_or.sort_values(by=['CRASH_DATE_FORMATTED','CRASH_TIME_HH'])

print(df_crash_or)
