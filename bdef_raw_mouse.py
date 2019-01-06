# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 18:23:45 2017

@author: agleo
"""

import pandas as pd
bdef = bdef_real
#path to the caars template
path = r'C:\Users\agleo\Desktop\bdefs_template.xlsx'                     # use the path
#path = r'/Users/agleontiev/Documents/templates/template_CAARS_SL.csv'
bdefs_template = pd.read_excel(path)

#path to the caars questions
#path2 = r'/Users/agleontiev/Documents/templates/caars.xlsx'
path2 = r'C:\Users\agleo\Desktop\bdefs.xlsx'
bdefs_key = pd.read_excel(path2)

bdefs_total = pd.merge(bdefs_key, bdefs_template, on ='stimID')

scale1 = bdefs_total[bdefs_total['key'] == 1]
list1 = scale1['bdefq'].tolist()

scale2 = bdefs_total[bdefs_total['key'] == 2]
list2 = scale2['bdefq'].tolist()

scale3 = bdefs_total[bdefs_total['key'] == 3]
list3 = scale3['bdefq'].tolist()

scale4 = bdefs_total[bdefs_total['key'] == 4]
list4 = scale4['bdefq'].tolist()

scale5 = bdefs_total[bdefs_total['key'] == 5]
list5 = scale5['bdefq'].tolist()

scaleIND = bdefs_total[bdefs_total['ind'] == "A"]
listIND = scaleIND['bdefq'].tolist()

raw1 = bdef[bdef['bdefq'].isin(list1)]
raw2 = bdef[bdef['bdefq'].isin(list2)]
raw3 = bdef[bdef['bdefq'].isin(list3)]
raw4 = bdef[bdef['bdefq'].isin(list4)]
raw5 = bdef[bdef['bdefq'].isin(list5)]
rawIND =bdef[bdef['bdefq'].isin(listIND)]

score1 = raw1.groupby(['UIN', 'Gender(m/f/o)','Age'])[["rating_3.response"]].sum()
score1 = score1.rename(columns={'rating_3.response': 'Section 1'})

score2 = raw2.groupby(['UIN', 'Gender(m/f/o)','Age'])[["rating_3.response"]].sum()
score2 = score2.rename(columns={'rating_3.response': 'Section 2'})

score3 = raw3.groupby(['UIN', 'Gender(m/f/o)','Age'])[["rating_3.response"]].sum()
score3 = score3.rename(columns={'rating_3.response': 'Section 3'})

score4 = raw4.groupby(['UIN', 'Gender(m/f/o)','Age'])[["rating_3.response"]].sum()
score4 = score4.rename(columns={'rating_3.response': 'Section 4'})

score5 = raw5.groupby(['UIN', 'Gender(m/f/o)','Age'])[["rating_3.response"]].sum()
score5 = score5.rename(columns={'rating_3.response': 'Section 5'})

scoreIND = rawIND.groupby(['UIN', 'Gender(m/f/o)','Age'])[["rating_3.response"]].sum()
scoreIND = scoreIND.rename(columns={'rating_3.response': 'ADHD Index'})


frames = [score1, score2, score3, score4, score5, scoreIND]
finalscore_mouse  = pd.concat(frames, axis=1, join_axes=[score1.index])

finalscore_mouse['Total'] = finalscore_mouse['Section 1'] + finalscore_mouse['Section 2'] + finalscore_mouse['Section 3']+finalscore_mouse['Section 4'] + finalscore_mouse['Section 5']
mouse_bdefs_scors = finalscore_mouse.reset_index()
mouse_bdefs_scors = mouse_bdefs_scors.set_index('UIN')

mouse_bdefs_scors.to_csv('mouse_bdefs_scors.csv')