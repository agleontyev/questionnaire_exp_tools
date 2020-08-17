# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 18:59:35 2020

@author: agleo
"""
import pandas as pd
#path to the upps template and raw data
upps_data = pd.read_csv('C:/Users/agleo/Documents/Programming_projects/TAMU/emotional_impulsivity_web_mouse/upps_responses.csv')
path = r'C:\Users\agleo\iCloudDrive\Documents\templates\upps_template.xlsx'                     # use the path

upps_template = pd.read_excel(path)

#path to the upps questions
#path2 = r'/Users/agleontiev/Documents/templates/caars.xlsx'
path2 = r'C:\Users\agleo\iCloudDrive\Documents\templates\upps.xlsx'
upps = pd.read_excel(path2)

upps_total = pd.merge(upps, upps_template, on ='N')

upps_total = upps_total.set_index('N')



scaleNU = upps_total[upps_total['scale'] == "NU"]
listNU = scaleNU['upps_q'].tolist()

scalePU = upps_total[upps_total['scale'] == "PU"]
listPU = scalePU['upps_q'].tolist()

scaleSS = upps_total[upps_total['scale'] == "SS"]
listSS = scaleSS['upps_q'].tolist()

scalePR = upps_total[upps_total['scale'] == "PR"]
listPR = scalePR['upps_q'].tolist()

scalePE = upps_total[upps_total['scale'] == "PE"]
listPE = scalePE['upps_q'].tolist()



### reverse coding the necessary rows
scale_RevCode = upps_total[upps_total['RevCode'] == 1]
listRevCode = scale_RevCode['upps_q'].tolist()

upps_new = upps_data.copy()
upps_new.loc[upps_new['upps_q'].isin(listRevCode), 'upps_resp.keys'] = 5 - upps_new['upps_resp.keys']

#select rows from upps raw data
rawNU = upps_new[upps_new['upps_q'].isin(listNU)]

rawPU = upps_new[upps_new['upps_q'].isin(listPU)]

rawSS = upps_new[upps_new['upps_q'].isin(listSS)]

rawPR = upps_new[upps_new['upps_q'].isin(listPR)]

rawPE = upps_new[upps_new['upps_q'].isin(listPE)]



scoreNU = rawNU.groupby(['File'])[["upps_resp.keys"]].sum()
scoreNU = scoreNU.rename(columns={'upps_resp.keys': 'NU'})

scorePU = rawPU.groupby(['File'])[["upps_resp.keys"]].sum()
scorePU = scorePU.rename(columns={'upps_resp.keys': 'PU'})

scoreSS = rawSS.groupby(['File'])[["upps_resp.keys"]].sum()
scoreSS = scoreSS.rename(columns={'upps_resp.keys': 'SS'})

scorePR = rawPR.groupby(['File'])[["upps_resp.keys"]].sum()
scorePR = scorePR.rename(columns={'upps_resp.keys': 'PR'})

scorePE = rawPE.groupby(['File'])[["upps_resp.keys"]].sum()
scorePE = scorePE.rename(columns={'upps_resp.keys': 'PE'})

frames = [scoreNU, scorePU, scoreSS, scorePR, scorePE]

finalscore  = pd.concat(frames, axis=1)

upps_scors = finalscore.reset_index()
upps_scors = upps_scors.set_index('File')
upps_scors.to_csv('UPPS_scores.csv')