# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:44:50 2017

@author: agleo
"""

import pandas as pd
import csv
import glob
import os

### for now, path placeholder ###
path = r'C:\Users\agleo\Dropbox\Anton\Experiments\2018\Stop-signal task spring 2018\Final results Spring 2018\Mouse'
#path = r'C:\Users\agleo\Google Drive\Data analysis\Fall 2017 real results\Mouse'                     # use the path
#path = r'/Users/agleontiev/Google Drive/Data analysis/Fall 2017 real results/Mouse'
all_files = glob.glob(os.path.join(path, "*.csv"))

all_files_data = (pd.read_csv(f) for f in all_files)
df_all  = pd.concat(all_files_data, ignore_index=True)

## experimental data ##

all_exp = df_all[df_all.soa.notnull()]
experimental_columns = ['UIN', 'Age','Gender(m/f/o)','soa','vol','coh', 'direct', 'response', 'correct', 'RT_exp','mouse.x', 'mouse.y', 'mouse.time']
df_exp = all_exp[experimental_columns]
df_exp_real = df_exp[df_exp.UIN.notnull()]
exp_countpersubj = df_exp_real.groupby(['UIN'])['UIN'].count()
print(exp_countpersubj)



## CAARS data ##
df_caars = df_all[df_all.question.notnull()]
caars_columns = ['UIN', 'Age','Gender(m/f/o)', 'question', 'caars_rating.response']
caars = df_caars[caars_columns]
caars_real = caars[caars.UIN.notnull()]
caars_real = caars_real.drop_duplicates(subset=['question', 'UIN'], keep='first')
value_list = ['I talk to much.']
caars_real = caars_real[~caars_real.question.isin(value_list)]

caars_countpersubj = caars_real.groupby(['UIN'])['UIN'].count()
print(caars_countpersubj)

## BIS-10 data ##

#df_bis = df_all[df_all.bisq.notnull()]
#bis_columns = ['UIN', 'Age','Gender(m/f/o)', 'bisq', 'bis_rating.response']
#biss = df_bis[bis_columns]
#bis_real = biss[biss.UIN.notnull()]
#bis_countpersubj = bis_real.groupby(['UIN'])['UIN'].count()
#print(bis_countpersubj)

## BDEFS data ##

df_bdef = df_all[df_all.bdefq.notnull()]
bdef_columns = ['UIN', 'Age','Gender(m/f/o)', 'bdefq', 'rating_3.response']
bdef = df_bdef[bdef_columns]
bdef_real = bdef[bdef.UIN.notnull()]
bdef_countpersubj = bdef_real.groupby(['UIN'])['UIN'].count()
print(bdef_countpersubj)


print (len(exp_countpersubj))
print (len(caars_countpersubj))
#print (len(bis_countpersubj))
print (len(bdef_countpersubj))

gender_mouse = df_exp_real.groupby('Gender(m/f/o)')['UIN'].nunique()
print(gender_mouse)
