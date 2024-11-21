import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
import seaborn as sns
from sklearn.preprocessing import PolynomialFeatures
import statsmodels.api as sm



# Quadratic function ax^2 + bx + c
def quadratic(x, a, b, c):
    return a*x**2 + b*x + c

# Below is function for formatting
def p_val_string(pvalue):
    if (pvalue <.001) :
        star = 'p<.001'

    elif np.round(pvalue,2) == 1:
        star = 'p=1'
    elif ((pvalue<.05) and (np.round(pvalue,2)>=.05)) or ((np.round(pvalue,2)==0)):
        star = 'p=' + '{:.3f}'.format(pvalue)[1:]
    else:
        star = 'p=' + '{:.2f}'.format(pvalue)[1:]
    return star

# Function to calculate SDT theoretical measures
def sdt(df, correct_counts):
    # counts:
    n_hit = ((df['stimulus']==1)&(df['response']==1)).sum()
    n_miss = ((df['stimulus']==1)&(df['response']==0)).sum()
    n_fa = ((df['stimulus']==0)&(df['response']==1)).sum()
    n_cr = ((df['stimulus']==0)&(df['response']==0)).sum()

    # correct counts?
    if correct_counts:
        n_hit += .5
        n_miss += .5
        n_fa += .5
        n_cr += .5

    # rates:
    hit_rate = n_hit / (n_hit + n_miss)
    fa_rate = n_fa / (n_fa + n_cr)

    # z-score:
    hit_rate_z = scipy.stats.norm.isf(1-hit_rate)
    fa_rate_z = scipy.stats.norm.isf(1-fa_rate)

    # measures:
    d = hit_rate_z - fa_rate_z
    c = -(hit_rate_z + fa_rate_z) / 2

    return pd.DataFrame({'d':[d], 'c':[c], 'hr':[hit_rate], 'far':[fa_rate]})

###########################################################

def run_model_pupilbin(x, deg, var):
    poly_feat = PolynomialFeatures(degree=deg)
    xp = poly_feat.fit_transform(x['bl_pupil_bin'].to_numpy().reshape(-1,1))
    model = sm.OLS(x[var], xp).fit()
    return model.params[deg]


def run_model_irrevbin(x, deg, var):
    poly_feat = PolynomialFeatures(degree=deg)
    xp = poly_feat.fit_transform(x['irreversibility_bin'].to_numpy().reshape(-1,1))
    model = sm.OLS(x[var], xp).fit()
    return model.params[deg]

def run_model_alphabin(x, deg, var):
    poly_feat = PolynomialFeatures(degree=deg)
    xp = poly_feat.fit_transform(x['alpha_bin'].to_numpy().reshape(-1,1))
    model = sm.OLS(x[var], xp).fit()
    return model.params[deg]

def run_model_bin(x, deg, var):
    poly_feat = PolynomialFeatures(degree=deg)
    xp = poly_feat.fit_transform(x['bin'].to_numpy().reshape(-1,1))
    model = sm.OLS(x[var], xp).fit()
    return model.params[deg]


