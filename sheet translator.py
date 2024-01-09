#!/usr/bin/env python
# coding: utf-8

# In[3]:


import time
from googletrans import Translator
import pandas as pd

excel_data_df = pd.read_excel('order_export.xlsx', sheet_name='sheet1')

translator = Translator()

def is_chinese(cell):
    for ch in str(cell):
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


start_time = time.time()


excel_data_df.columns = excel_data_df.columns.map(lambda x: translator.translate(x, dest='en').text)

for col in excel_data_df.columns:
    excel_data_df[col] = excel_data_df[col].map(lambda x: translator.translate(str(x), dest='en').text if pd.notnull(x) and is_chinese(x) else x)

excel_data_df.to_excel('tr-en_orderexport.xlsx', index=False)

end_time = time.time()

time_taken = end_time - start_time
print(f'Time taken to translate and save: {time_taken} seconds')


# In[ ]:




