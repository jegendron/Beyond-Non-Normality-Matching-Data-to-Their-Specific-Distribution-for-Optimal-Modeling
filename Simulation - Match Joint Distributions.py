#%%                  Import libraries and prepare data                  ###

import numpy as np
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Set the random seed for reproducibility
np.random.seed(42)

# Sample size
n = 500

# Generate normal X
X = np.random.normal(0, 1, n)

"""Different y's generated to show the success of identifying each type 
of non-normal joint distribution"""

# Generate y that's Normal
yNorm = np.random.normal(0, 1, n)
reg = sm.OLS(yNorm, X).fit()
residNorm = reg.resid

# Generate y that's Student's t
yStudT = stats.t.rvs(df=4, loc=5, scale=2, size=n) 
reg = sm.OLS(yStudT, X).fit()
residStudT = reg.resid

# Generate y that's Beta (left skew)
    #(For right skew swap a and b, make a=b for symmetric)
yBeta = stats.beta.rvs(a=5, b=1, size=n)
reg = sm.OLS(yBeta, X).fit()
residBeta = reg.resid



###########################################################
#%%         Compare to CONTINUOUS distributions         ###
###########################################################

# ---------------------------------------------------------
#                      SYMMETRIC
# ---------------------------------------------------------

# --- Compare Data to Normal distribution ---         (ELLIPTICALLY SYMMETRIC)

# --- Plot the data ---
fig, ax = plt.subplots()
sns.histplot(x=residNorm, ax=ax, stat="density", linewidth=0, kde=True, label='Data Distribution')
ax.set(title="Normal Distribution Testing", xlabel="Residual Values")
xmin, xmax = plt.xlim() # the maximum x values from the histogram above
x = np.linspace(xmin, xmax, len(residNorm)) # generate some x values

# --- Plot the Normal distribution --- 
muNorm, varNorm = stats.norm.fit(residNorm)
pNorm = stats.norm.pdf(x, muNorm, varNorm) # calculate the y values for the normal curve
sns.lineplot(x=x, y=pNorm, color="black", ax=ax,label="Normal Distribution")
plt.show()



# --- Compare Data to Normal distribution ---         (ELLIPTICALLY SYMMETRIC)

# --- Plot the data ---
fig, ax = plt.subplots()
sns.histplot(x=residStudT, ax=ax, stat="density", linewidth=0, kde=True, label='Data Distribution')
ax.set(title="Student's t Distribution Testing", xlabel="Residual Values")
xmin, xmax = plt.xlim() # the maximum x values from the histogram above
x = np.linspace(xmin, xmax, len(yStudT)) # generate some x values

# --- Plot the Normal distribution --- 
muNorm, varNorm = stats.norm.fit(residStudT)
pNorm = stats.norm.pdf(x, muNorm, varNorm) # calculate the y values for the normal curve
sns.lineplot(x=x, y=pNorm, color="black", ax=ax,label="Normal Distribution")
plt.show()



# --- Compare Data to Student's t Distribution ---    (ELLIPTICALLY SYMMETRIC)

# --- Plot the data ---
fig, ax = plt.subplots()
sns.histplot(x=residStudT, ax=ax, stat="density", linewidth=0, kde=True, label='Data Distribution')
ax.set(title="Student's t Distribution Testing", xlabel="Residual Values")
xmin, xmax = plt.xlim() # the maximum x values from the histogram above
x = np.linspace(xmin, xmax, len(yStudT)) # generate some x values



# --- Plot the Student's t Distribution --- 
v, mu, var = stats.t.fit(residStudT)
# v = degrees of freedom   
    # If your distribution shape looks off, you can manually adjust the values of v 
    
pStudT = stats.t.pdf(x, df=v, loc=mu, scale=var) # calculate the y values for this distribution
sns.lineplot(x=x, y=pStudT, color="red", ax=ax,label="Students t Distribution (v="+str(round(v,2))+")")

# --- Plot the Normal distribution --- 
muNorm, varNorm = stats.norm.fit(residStudT)
pNorm = stats.norm.pdf(x, muNorm, varNorm) # calculate the y values for the normal curve
sns.lineplot(x=x, y=pNorm, color="black", ax=ax,label="Normal Distribution")
plt.show()



# ---------------------------------------------------------
#                      SKEWED
# ---------------------------------------------------------

# --- Compare Data to Beta distribution ---

# --- Plot the data ---
fig, ax = plt.subplots()
sns.histplot(x=residBeta, ax=ax, stat="density", linewidth=0, kde=True, label='Data Distribution')
ax.set(title="Beta Distribution Testing", xlabel="Residual Values")
xmin, xmax = plt.xlim() # the maximum x values from the histogram above
x = np.linspace(xmin, xmax, len(yBeta)) # generate some x values



# --- Plot the Beta distribution --- 
a, b, mu, var = stats.beta.fit(residBeta)
# a, b = shape parameters
    # If your distribution shape looks off, you can manually adjust the values of a & b (i.e. shape parameters)

pBeta = stats.beta.pdf(x, a=a, b=b, loc=mu, scale=var) # calculate the y values for this distribution
sns.lineplot(x=x, y=pBeta, color="green", ax=ax,label="Beta Distribution (a="+str(round(a,2))+", b="+str(round(b,2)))

# --- Plot the Normal distribution --- 
muNorm, varNorm = stats.norm.fit(residBeta)
pNorm = stats.norm.pdf(x, muNorm, varNorm) # calculate the y values for the normal curve
sns.lineplot(x=x, y=pNorm, color="black", ax=ax,label="Normal Distribution")
plt.show()
