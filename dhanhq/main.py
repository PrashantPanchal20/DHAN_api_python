from dhanhq import dhanhq
import pandas as pd
from datetime import datetime

client_id = "Add your Clint ID"
access_token = "Enter your token here"

dhan = dhanhq(client_id, access_token)

my_fund = dhan.get_fund_limits()
print(my_fund)

# chart = dhan.historical_minute_charts(data)
# print(chart)

holdings = dhan.get_holdings()
print(holdings)
#SEM_SMST_SECURITY_ID = 13 for nifty
# master_list = pd.read_csv("https://images.dhan.co/api-data/api-scrip-master.csv", nrows = 1)
master_list = pd.read_csv("https://images.dhan.co/api-data/api-scrip-master.csv", low_memory=False)

df = pd.DataFrame(master_list)
df.drop('SEM_EXPIRY_FLAG', axis=1, inplace=True)
df.drop('SEM_EXCH_INSTRUMENT_TYPE', axis=1, inplace=True)
df.drop('SEM_EXPIRY_CODE', axis=1, inplace=True)
df.drop('SM_SYMBOL_NAME', axis=1, inplace=True)
df.drop('SEM_SERIES', axis=1, inplace=True)
# df.drop(' SEM_SEGMENT', axis=1, inplace=True)
df.drop('SEM_TRADING_SYMBOL', axis=1, inplace=True)
df.drop('SEM_OPTION_TYPE', axis=1, inplace=True)
df.drop('SEM_TICK_SIZE', axis=1, inplace=True)
df.drop('SEM_STRIKE_PRICE', axis=1, inplace=True)

filtered_data = []
option = []
SEM_SMST_SECURITY_ID = ""
current_time = datetime.now()
for index, row in df.iterrows():
    if (row['SEM_EXM_EXCH_ID'] == "NSE" and row['SEM_INSTRUMENT_NAME'] == ("OPTIDX") or row['SEM_CUSTOM_SYMBOL'] == ("Nifty 50")):
        filtered_data.append(row)

data = pd.DataFrame(filtered_data)
data[['SYMBOL', 'EXP_DATE', 'EXP_MONTH', 'STRIKE', 'OPT_TYPE']] = data['SEM_CUSTOM_SYMBOL'].str.split(' ', n=4, expand=True)
data.drop('SEM_CUSTOM_SYMBOL', axis=1, inplace=True)
data.drop('SEM_EXPIRY_DATE', axis=1, inplace=True)
data['SYMBOL'] = "NIFTY"
data['EXP_MONTH'] = "JAN"
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_rows', None)
# print(data)
# print(type(data))
for index, row in data.iterrows():
    if (row['SEM_INSTRUMENT_NAME'] == "INDEX"):
        print(row)
# for index, row in data.iterrows():
    elif (row['STRIKE'] == "21750" and row['EXP_DATE'] == "04" and row['OPT_TYPE'] == "PUT"):
        SEM_SMST_SECURITY_ID = row['SEM_SMST_SECURITY_ID']
        option.append(row)
data = pd.DataFrame(option)

data.reset_index(drop=True, inplace=True)
print(data)
# print(SEM_SMST_SECURITY_ID)

chart = dhan.intraday_daily_minute_charts(13, 'NSE', 'INDEX' )
print(chart)
# chart = dhan.historical_minute_charts(
#     symbol='TCS',
#     exchange_segment='NSE_EQ',
#     instrument_type='EQUITY',
#     expiry_code=0,
#     from_date='2023-12-25',
#     to_date='2023-12-30'
# )
# chart = dhan.historical_minute_charts(
#     symbol='nifty',
#     exchange_segment='NSE_FNO',
#     instrument_type='INDEX',
#     expiry_code=0,
#     from_date='2023-12-25',
#     to_date='2023-12-30'
# )

# print(chart)
