# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 15:36:00 2017

@author: agleo
"""

import pandas as pd
caars = caars_real_key
#path to the caars template
path = r'C:\Users\agleo\Dropbox\Anton\Experiments\2018\Stop-signal task summer-fall 2018\data\Keypress\test_Anton\template_CAARS_SL.csv'                     # use the path
#path = r'/Users/agleontiev/Documents/templates/template_CAARS_SL.csv'
caars_template = pd.read_csv(path)

#path to the caars questions
#path2 = r'/Users/agleontiev/Documents/templates/caars.xlsx'
path2 = r'C:\Users\agleo\Desktop\caars.xlsx'
caars_key = pd.read_excel(path2)
in1 = [11, 40, 20, 13, 30, 19, 6, 26]
in2 = [49, 44, 25, 27, 47, 23, 37, 63]

caars_total = pd.merge(caars_key, caars_template, on ='stimID')
caars_total = caars_total.set_index('stimID')
caars_total.ix[in1, "IN1"] = "T"
caars_total.ix[in2, "IN2"] = "T"

scaleA = caars_total[caars_total['key'] == "A"]
listA = scaleA['question'].tolist()

scaleB = caars_total[caars_total['key'] == "B"]
listB = scaleB['question'].tolist()

scaleC = caars_total[caars_total['key'] == "C"]
listC = scaleC['question'].tolist()

scaleD = caars_total[caars_total['key'] == "D"]
listD = scaleD['question'].tolist()

scaleE = caars_total[caars_total['key'] == "E"]
listE = scaleE['question'].tolist()

scaleF = caars_total[caars_total['key'] == "F"]
listF = scaleF['question'].tolist()

scaleH = caars_total[caars_total['key'] == "H"]
listH = scaleH['question'].tolist()

scaleIN1 = caars_total[caars_total['IN1'] == "T"]
listIN1 = scaleIN1['question'].tolist()


scaleIN2 = caars_total[caars_total['IN2'] == "T"]
listIN2 = scaleIN2['question'].tolist()

#select rows from caars
rawA = caars[caars['question'].isin(listA)]
rawB = caars[caars['question'].isin(listB)]
rawC = caars[caars['question'].isin(listC)]
rawD = caars[caars['question'].isin(listD)]
rawE = caars[caars['question'].isin(listE)]
rawF = caars[caars['question'].isin(listF)]
rawH = caars[caars['question'].isin(listH)]
rawIN1 = caars[caars['question'].isin(listIN1)]
rawIN2 = caars[caars['question'].isin(listIN2)]


### Calculating inconsistency scores ###
rawIN1 = rawIN1.rename(columns={'caars_rating.response': 'IN1_response'})
rawIN2 = rawIN2.rename(columns={'caars_rating.response': 'IN2_response'})
rawIN1 = rawIN1.reset_index()
rawIN2 = rawIN2.reset_index()
result = pd.concat([rawIN1, rawIN2], axis=1, join='inner')
result['IN'] = result['IN1_response'] - result['IN2_response']
result['IN']= result['IN'].abs()
result = result.loc[:,~result.columns.duplicated()]



scoreA = rawA.groupby(['UIN', 'Gender(m/f/o)','Age'])[["caars_rating.response"]].sum()
scoreA = scoreA.rename(columns={'caars_rating.response': 'A'})

scoreB = rawB.groupby(['UIN', 'Gender(m/f/o)','Age'])[["caars_rating.response"]].sum()
scoreB = scoreB.rename(columns={'caars_rating.response': 'B'})

scoreC = rawC.groupby(['UIN', 'Gender(m/f/o)','Age'])[["caars_rating.response"]].sum()
scoreC = scoreC.rename(columns={'caars_rating.response': 'C'})

scoreD = rawD.groupby(['UIN', 'Gender(m/f/o)','Age'])[["caars_rating.response"]].sum()
scoreD = scoreD.rename(columns={'caars_rating.response': 'D'})

scoreE = rawE.groupby(['UIN', 'Gender(m/f/o)','Age'])[["caars_rating.response"]].sum()
scoreE = scoreE.rename(columns={'caars_rating.response': 'E'})

scoreF = rawF.groupby(['UIN', 'Gender(m/f/o)','Age'])[["caars_rating.response"]].sum()
scoreF = scoreF.rename(columns={'caars_rating.response': 'F'})

scoreH = rawH.groupby(['UIN', 'Gender(m/f/o)','Age'])[["caars_rating.response"]].sum()
scoreH = scoreH.rename(columns={'caars_rating.response': 'H'})

scoreIN = result.groupby(['UIN', 'Gender(m/f/o)','Age'])[["IN"]].sum()

frames = [scoreA, scoreB, scoreC, scoreD, scoreE, scoreF, scoreH, scoreIN]
finalscore_key  = pd.concat(frames, axis=1, join_axes=[scoreA.index])
finalscore_key['G'] = finalscore_key['E'] + finalscore_key['F']

finalscore2 = finalscore_key[['A','B','C','D','E','F','G','H', 'IN']]
key_caars_scors = finalscore2.reset_index()
key_caars_scors = key_caars_scors.set_index('UIN')
key_caars_scors.to_csv("key_caars_scors_spring2018.csv")