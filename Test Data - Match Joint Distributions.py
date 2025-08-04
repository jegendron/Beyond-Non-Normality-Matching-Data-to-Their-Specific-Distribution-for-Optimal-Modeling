#%%                  Import libraries and prepare data                  ###

import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt

# IMPORT DATA TO TEST HERE
filepath = "C:/Users/jegendron/Downloads/Sample Data.xlsx"
resid = pd.read_excel(filepath)
resid = resid.squeeze()



###########################################################
#%%         Compare to CONTINUOUS distributions         ###
###########################################################

# ---------------------------------------------------------
#                      SYMMETRIC
# ---------------------------------------------------------

# --- Compare Data to Normal distribution ---         (ELLIPTICALLY SYMMETRIC)

# --- Plot the data ---
fig, ax = plt.subplots()
sns.histplot(x=resid, ax=ax, stat="density", linewidth=0, kde=True, label='Data Distribution')
ax.set(title="Normal Distribution Testing", xlabel="Residual Values")
xmin, xmax = plt.xlim() # the maximum x values from the histogram above
x = np.linspace(xmin, xmax, len(resid)) # generate some x values

# --- Plot the Normal distribution --- 
muNorm, varNorm = stats.norm.fit(resid)
pNorm = stats.norm.pdf(x, muNorm, varNorm) # calculate the y values for the normal curve
sns.lineplot(x=x, y=pNorm, color="black", ax=ax,label="Normal Distribution")
plt.show()



# --- Compare Data to Student's t Distribution ---    (ELLIPTICALLY SYMMETRIC)

# --- Plot the data ---
fig, ax = plt.subplots()
sns.histplot(x=resid, ax=ax, stat="density", linewidth=0, kde=True, label='Data Distribution')
ax.set(title="Student's t Distribution Testing", xlabel="Residual Values")
xmin, xmax = plt.xlim() # the maximum x values from the histogram above
x = np.linspace(xmin, xmax, len(resid)) # generate some x values



# --- Plot the Student's t Distribution --- 
v, mu, var = stats.t.fit(resid)
# v = degrees of freedom   
    # If your distribution shape looks off, you can manually adjust the values of v 

pStudT = stats.t.pdf(x, df=v, loc=mu, scale=var) # calculate the y values for this distribution
sns.lineplot(x=x, y=pStudT, color="red", ax=ax,label="Students t Distribution (v="+str(round(v,2))+")")

# --- Plot the Normal distribution --- 
muNorm, varNorm = stats.norm.fit(resid)
pNorm = stats.norm.pdf(x, muNorm, varNorm) # calculate the y values for the normal curve
sns.lineplot(x=x, y=pNorm, color="black", ax=ax,label="Normal Distribution")
plt.show()



# ---------------------------------------------------------
#                      SKEWED
# ---------------------------------------------------------

# --- Compare Data to Beta distribution ---

"""Ensure the residual are in the range [0,1], 
otherwise you can't compare with the Beta distribution"""
maxResid = max(resid)
minResid = min(resid)
if(minResid<0 or maxResid>1):
    for i in range(len(resid)):
        resid[i] = (resid[i]-minResid)/(maxResid-minResid)

# --- Plot the data ---
fig, ax = plt.subplots()
sns.histplot(x=resid, ax=ax, stat="density", linewidth=0, kde=True, label='Data Distribution')
ax.set(title="Beta Distribution Testing", xlabel="Residual Values")
xmin, xmax = plt.xlim() # the maximum x values from the histogram above
x = np.linspace(xmin, xmax, len(resid)) # generate some x values



# --- Plot the Beta distribution --- 
a, b, mu, var = stats.beta.fit(resid)
# a, b = shape parameters
    # If your distribution shape looks off, you can manually adjust the values of a & b (i.e. shape parameters)

pBeta = stats.beta.pdf(x, a=a, b=b, loc=mu, scale=var) # calculate the y values for this distribution
sns.lineplot(x=x, y=pBeta, color="green", ax=ax,label="Beta Distribution (a="+str(round(a,2))+", b="+str(round(b,2)))

# --- Plot the Normal distribution --- 
muNorm, varNorm = stats.norm.fit(resid)
pNorm = stats.norm.pdf(x, muNorm, varNorm) # calculate the y values for the normal curve
sns.lineplot(x=x, y=pNorm, color="black", ax=ax,label="Normal Distribution")
plt.show()
