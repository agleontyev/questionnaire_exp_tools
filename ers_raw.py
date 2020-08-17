# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 13:56:11 2020

@author: agleo
"""
import pandas as pd
#path to the upps template and raw data
ers_data = pd.read_csv('C:/Users/agleo/Documents/Programming_projects/TAMU/emotional_impulsivity_web_mouse/ers_responses.csv')
path = r'C:\Users\agleo\iCloudDrive\Documents\templates\ers_template.xlsx'                     # use the path

ers_template = pd.read_excel(path)

#path to the upps questions
#path2 = r'/Users/agleontiev/Documents/templates/caars.xlsx'
path2 = r'C:\Users\agleo\iCloudDrive\Documents\templates\ers.xlsx'
ers = pd.read_excel(path2)

ers_total = pd.merge(ers, ers_template, on ='N')

ers_total = ers_total.set_index('N')



scalePERS = ers_total[ers_total['Scale'] == "PERS"]
listPERS = scalePERS['ers_q'].tolist()

scaleSENS = ers_total[ers_total['Scale'] == "SENS"]
listSENS = scaleSENS['ers_q'].tolist()

scaleAI = ers_total[ers_total['Scale'] == "AI"]
listAI = scaleAI['ers_q'].tolist()



#select rows from upps raw data
rawPERS = ers_data[ers_data['ers_q'].isin(listPERS)]

rawSENS = ers_data[ers_data['ers_q'].isin(listSENS)]

rawAI = ers_data[ers_data['ers_q'].isin(listAI)]




scorePERS = rawPERS.groupby(['File'])[["ers_response.keys"]].sum()
scorePERS = scorePERS.rename(columns={'ers_response.keys': 'PERS'})

scoreSENS = rawSENS.groupby(['File'])[["ers_response.keys"]].sum()
scoreSENS = scoreSENS.rename(columns={'ers_response.keys': 'SENS'})

scoreAI = rawAI.groupby(['File'])[["ers_response.keys"]].sum()
scoreAI = scoreAI.rename(columns={'ers_response.keys': 'AI'})


frames = [scorePERS, scoreSENS, scoreAI]

finalscore  = pd.concat(frames, axis=1)

ers_scors = finalscore.reset_index()
ers_scors = ers_scors.set_index('File')
ers_scors.to_csv('ERS_scores.csv')