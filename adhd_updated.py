# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:44:22 2019

@author: agleo
"""

import pandas as pd
caars = caars_real

caars_template_file_path = r'C:\Users\agleo\Dropbox\Anton\Experiments\2018\Stop-signal task summer-fall 2018\data\Keypress\test_Anton\template_CAARS_SL.csv'                     # use the path

caars_template = pd.read_csv(caars_template_file_path)

#path2 = r'/Users/agleontiev/Documents/templates/caars.xlsx'
caars_questions_file_path = r'C:\Users\agleo\Desktop\caars.xlsx'
caars_key = pd.read_excel(caars_questions_file_path)
#inconsistency scale question numbers
in1 = [11, 40, 20, 13, 30, 19, 6, 26] 
in2 = [49, 44, 25, 27, 47, 23, 37, 63]  

caars_total = pd.merge(
    caars_key,
    caars_template,
    on='stimID'
).set_index('stimID')
caars_total.loc[in1, "IN1"] = "T"
caars_total.loc[in2, "IN2"] = "T"


raws = {}
for key in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
    raws[key] = caars[caars['question'].isin(
        caars_total[caars_total['key'] == key]['question'].tolist()
    )]
for caars_total_key in ['IN1', 'IN2']:
    raws[caars_total_key] = caars[caars['question'].isin(
        caars_total[caars_total[caars_total_key] == "T"]['question'].tolist()
    )]


# Calculating inconsistency scores

raws['IN1'] = raws['IN1'].rename(
    columns={'caars_rating.response': 'IN1_response'}
).reset_index()
raws['IN2'] = raws['IN2'].rename(
    columns={'caars_rating.response': 'IN2_response'}
).reset_index()
result = pd.concat([raws['IN1'], raws['IN2']], axis=1, join='inner')
result['IN'] = result['IN1_response'] - result['IN2_response']
result['IN'] = result['IN'].abs()
result = result.loc[:, ~result.columns.duplicated()]

scores = {}
for key in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
    scores[key] = raws[key].groupby(
        ['UIN', 'Gender', 'Age']
    )[["caars_rating.response"]].sum().rename(
        columns={'caars_rating.response': key}
    )


scores['IN'] = result.groupby(['UIN', 'Gender', 'Age'])[["IN"]].sum()

# I belive that for the following line there could be a nice python operator.
# But I have no idea if it exists and if so - what's the name ;)
frames = [scores['A'], scores['B'], scores['C'], scores['D'], scores['E'], scores['F'], scores['H'], scores['IN']]
finalscore_key = pd.concat(frames, axis=1, join_axes=[scores['A'].index])
finalscore_key['G'] = finalscore_key['E'] + finalscore_key['F']

finalscore2 = finalscore_key[['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'IN']]
key_caars_scors = finalscore2.reset_index().set_index('UIN')
key_caars_scors.to_csv("key_caars_scors_spring2018.csv")
