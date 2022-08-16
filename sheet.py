import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials


sa = gspread.service_account(filename="service.json")
sh = sa.open("test")

wks = sh.worksheet("s1")

# print('Rows:',wks.row_count)
# print('Rows:',wks.col_count)
# worksheet=wks.get_all_records()


# get all the records of the data
records_data = wks.get_all_records()

# convert the json to dataframe
records_df =pd.DataFrame.from_dict(records_data)

ids = [val['id'] for val in records_data]
print(ids)