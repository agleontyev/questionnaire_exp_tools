# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 18:34:42 2017

@author: agleo
"""
import pandas as pd

df.1 = pd.rea
from scipy.interpolate import UnivariateSpline
from scipy import interpolate
from scipy.interpolate import interp1d
from scipy.interpolate import InterpolatedUnivariateSpline

def SmootheSplinesBaby(x):
    x1 = x['variable'].values
    x2 = x1[::-1]
    y1 = x['value'].values
    y2 = y1[::-1]
    s = InterpolatedUnivariateSpline(x1, y1)
    return s

splinedf = df_1.groupby('UIN').apply(SmootheSplinesBaby)

def EvaluateSpline(h):
    q = h(0.5)
    return q
spline_evals = splinedf.apply(EvaluateSpline) 

