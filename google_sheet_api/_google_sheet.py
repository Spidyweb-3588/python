#https://givemethesocks.tistory.com/65
#https://hleecaster.com/python-google-drive-spreadsheet-api/
#https://mentha2.tistory.com/207
#spread sheet가 널인 경우도 포함시켜서 넣기

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import pathlib

scope =[
    'https://spreadsheets.google.com/feeds',
]

json_file_name = 'C:/Users/jiho3/Downloads/scenic-aileron-315712-e4b251b97e73.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)

spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1kPG9xyVFl2lOeRHHNLOGwSYLKSOOWbCNPFWJAnpE9j4/edit#gid=0'

doc = gc.open_by_url(spreadsheet_url)

worksheet = doc.worksheet('시트1')

cell_data = worksheet.acell('A2').value
range_data = worksheet.range('A2:A9')

range_name = []
for i in range_data:
    if i.value != '':
        range_name.append(i.value)
###########################################
print(range_data)
print("\n")
print(range_name)
print("\n")



file_path="C:/covid19_result/all_day/"
#dictionary로 만들어보자
file_dict={}
for i in range(len(os.listdir(file_path))):
    if pathlib.Path(os.listdir(file_path)[i]).suffixes == ['.csv']:
        file_dict[os.listdir(file_path)[i]] = os.path.getmtime(file_path+os.listdir(file_path)[i])

print(sorted(file_dict.keys(), key = lambda item: item[1]))
"""file_oldname=[]
file_time=[]
for i in os.listdir(file_path):
    if pathlib.Path(i).suffixes == ['.csv']:
        file_oldname.append(file_path+i)
        file_time.append(os.path.getmtime(file_path+i))"""

file_newname = cell_data



"""for i in range(len(file_oldname)):
    print(file_oldname[i],range_name[i])
    os.rename(file_oldname[i],file_path+range_name[i]+".csv")"""