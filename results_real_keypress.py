# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:13:21 2017

@author: agleo
"""

import pandas as pd
import numpy as np
import glob
import os

### for now, path placeholder ###
key_path = r'C:\Users\agleo\iCloudDrive\Documents\Experiments\Summer2-Fall 2018 experiement results\Keypress'
#key_path = r'/Users/agleontiev/Google Drive/Data analysis/Fall 2017 real results/Keypress'
#key_path = r'C:\Users\agleo\Google Drive\Data analysis\Fall 2017 real results\Keypress'                     # use the path
all_files_key = glob.glob(os.path.join(key_path, "*.csv"))

all_files_data_key = (pd.read_csv(f) for f in all_files_key)
df_all_key  = pd.concat(all_files_data_key, ignore_index=True)

## experimental data ##

all_exp_key = df_all_key[df_all_key.soa.notnull()]
experimental_columns_key = ['UIN', 'Age','Gender','soa','vol', 'coh','direct', 'key_resp_2.keys','key_resp_2.rt','key_resp_2.corr' ]
df_exp_key = all_exp_key[experimental_columns_key]
df_exp_real_key = df_exp_key[df_exp_key.UIN.notnull()]
exp_countpersubj_key = df_exp_real_key.groupby(['UIN'])['UIN'].count()
print(exp_countpersubj_key)


## CAARS data ##
df_caars_key = df_all_key[df_all_key.question.notnull()]
caars_columns_key = ['UIN', 'Age','Gender', 'question', 'rating_2.response']
caars_key = df_caars_key[caars_columns_key]
caars_real_key = caars_key[caars_key.UIN.notnull()]
caars_real_key = caars_real_key.drop_duplicates(subset=['question', 'UIN'], keep='first')
value_list = ['I talk to much.']
caars_real_key = caars_real_key[~caars_real_key.question.isin(value_list)]
caars_countpersubj_key = caars_real_key.groupby(['UIN'])['UIN'].count()
print(caars_countpersubj_key)

## BIS-10 data ##

df_bis_key = df_all_key[df_all_key.bisq.notnull()]
bis_columns_key = ['UIN', 'Age','Gender(m/f/o)', 'bisq', 'bis_rating.response']
biss_key = df_bis_key[bis_columns_key]
bis_real_key = biss_key[biss_key.UIN.notnull()]
bis_countpersubj_key = bis_real_key.groupby(['UIN'])['UIN'].count()
print(bis_countpersubj_key)

## BDEFS data ##

df_bdef_key = df_all_key[df_all_key.bdefq.notnull()]
bdef_columns_key = ['UIN', 'Age','Gender(m/f/o)', 'bdefq', 'rating_3.response']
bdef_key = df_bdef_key[bdef_columns_key]
bdef_real_key = bdef_key[bdef_key.UIN.notnull()]
bdef_countpersubj_key = bdef_real_key.groupby(['UIN'])['UIN'].count()
print(bdef_countpersubj_key)

