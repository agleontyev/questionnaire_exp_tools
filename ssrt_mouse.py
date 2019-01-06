# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 10:42:14 2017

@author: agleo
"""

median_go_raw = mouse_exp['RT_exp'].groupby([mouse_exp['UIN'], mouse_exp['vol']]).median().unstack()
median_go_raw = median_go_raw.reset_index()
median_go_raw = median_go_raw.set_index("UIN")
median_go =  median_go_raw['go'] 


z = spline_evals.to_frame()
w = median_go.to_frame()
ssrt = pd.concat([z, w], axis=1)
ssrt  = ssrt.drop(badpeople)
ssrt =ssrt.rename(columns = {0:'splice'})
ssrt['ssrt_nonab'] =  ssrt['go'] - ssrt['splice']

ssrt['ssrt'] = ssrt['ssrt_nonab'].abs()

ssrt.to_csv('ssrt_mouse.csv')