import pandas as pd

def fund_infomation(input_fund):
  df = pd.read_csv('all_fund_list.csv')
  input_item = input_fund.upper()
  return df.loc[df['fund_name']==input_item] 