# BME 235 Data Analysis

# reorganized data excel sheet

# pip install pingouin

import pandas as pd # handles data
import seaborn as sea # for plotting
import pingouin as pg # for anova
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

from scipy.stats import ttest_ind

from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# import data
data = pd.read_csv('bme235organized.csv')

                        # base, powder, liquid (conditions)
# average ECG amplitude
# average ECG duration
# average pulse ox
# average respiration rate
# average percent of resting heart rate after 3 minutes
pinks = ['orchid', 'pink', 'palevioletred']
#sea.palplot(sea.color_palette('pastel'))
#my_colors = ListedColormap(sea.color_palette(pinks))
my_colors = sea.color_palette(['orchid', 'pink', 'palevioletred'])
sea.palplot(my_colors)

# average ECG amplitude
aov_amp = pg.anova(data=data, dv='ECG_amplitude_mV', between = 'Trial', detailed = True)
print('ecg amplitude')
pg.print_table(aov_amp)
pg.print_table(data)
plt.title('Average ECG Amplitude') # title
plt.ylabel('ECG Amplitude (mV)') # label
plt.xlabel('Trial') # label
plt.ylim(80, 100)
plt.show()
# boxplot
ax = sea.barplot(x='Trial', y='ECG_amplitude_mV', data = data, palette = my_colors, estimator=np.mean, capsize=.2)
#                                                            add violet and pink
#ax = sea.swarmplot(x='Trial', y='ECG_amplitude_mV', data = data, color = '#4B0082')
plt.title('Average ECG Amplitude') # title

# average ECG duration
aov_sec = pg.anova(data=data, dv='ECG_duration_seconds', between = 'Trial', detailed = True)
print('ecg duration')
pg.print_table(aov_sec)
plt.title('Average ECG Duration') # title
plt.ylabel('ECG Duration (seconds)') # label
plt.xlabel('Trial') # label
plt.show()
# boxplot
ax = sea.barplot(x='Trial', y='ECG_duration_seconds', data = data, palette = my_colors, estimator=np.mean, capsize=.2)
#ax = sea.swarmplot(x='Trial', y='ECG_duration_seconds', data = data, color = '#4B0082')
plt.title('Average ECG Duration') # title

print('Tukey PostHoc Test')
pg.pairwise_tukey(data=data, dv='ECG_duration_seconds', between='Trial').round(3)

#df = pg.read_dataset('penguins')
#df.pairwise_tukey(dv='body_mass_g', between='species').round(3)





# load dataset
#tips = sns.load_dataset("tips")

# Set the figure size
#plt.figure(figsize=(14, 8))

# plot a bar chart
#ax = sns.barplot(x="day", y="total_bill", data=tips, estimator=np.mean, ci=85, capsize=.2, color='lightblue')

#a = 'base'
#b = 'powder'
#c = 'liquid'
#f_oneway(a, b, c)
# statstically significant, but how, p=0.022
#ttest_ind(data.loc[data.loc[:,'Trial']==0, 'powder'], data.loc[data.loc[:,'Trial']==2, 'liquid'])




# average SPO2 Percentage
aov_spo2 = pg.anova(data=data, dv='Oxygen', between = 'Trial', detailed = True)
print('spo2 percentage')
pg.print_table(aov_spo2)
plt.ylabel('SPO2 Percentage') # label
plt.xlabel('Trial') # label
# plt.ylim(80, 100) # TRIED
# plt.yticks([80,90,100]) # NO CHANGE
#plt.yticks([80, 90, 100])
#ax.set_ylim(80, 100)

plt.show()
# boxplot
ax = sea.barplot(x='Trial', y='Oxygen', data = data, palette = my_colors, estimator=np.mean, capsize=.2)
#ax = sea.swarmplot(x='Trial', y='Oxygen', data = data, color = '#4B0082')
ax.set_ylim(90, 100)
plt.title('Average SPO2 Concentration Percentage') # title

# average heart rate recovery percentage after 3 minutes
aov_heartrec = pg.anova(data=data, dv='Recovery_percentage', between = 'Trial', detailed = True)
print('percent of heart rate recovery')
pg.print_table(aov_heartrec)
plt.ylabel('Heart Rate Recovery Percentage') # label
plt.xlabel('Trial') # label
plt.show()
# boxplot
ax = sea.barplot(x='Trial', y='Recovery_percentage', data = data, palette = my_colors, estimator=np.mean, capsize=.2)
#ax = sea.swarmplot(x='Trial', y='Recovery_percentage', data = data, color = '#4B0082')
ax.set_ylim(80, 120)
plt.title('Average Resting Heart Rate Recovery Percentage') # title

# average SPO2 recovery rate percentage
aov_oxygenrec = pg.anova(data=data, dv='Recovery_percentage', between = 'Trial', detailed = True)
print('spo2 recovery percentage')
pg.print_table(aov_oxygenrec)
plt.ylabel('SPO2 Concentration Recovery Percentage') # label
plt.xlabel('Trial') # label
plt.show()
# boxplot
ax = sea.barplot(x='Trial', y='Respiratory_Recovery_percentage', data = data, palette = my_colors, estimator=np.mean, capsize=.2)
#ax = sea.swarmplot(x='Trial', y='Respiratory_Recovery_percentage', data = data, color = '#4B0082')
ax.set_ylim(96, 102)
plt.title('Average SPO2 Concentration Recovery Percentage') # title

# significant (p<0.05) ONLY, ecg duration, powder is signifcantly significant
# need to run the ttest to determine how it was SS

six = pd.read_csv('tiredd.csv')
aov_tiredd = pg.anova(data=six, dv='Subject', between = 'Choice', detailed = True)
print('Survey: Which trial felt more tiring?')
pg.print_table(aov_tiredd)
plt.ylabel('Quantity') # label
plt.xlabel('Trial') # label
plt.show()
# boxplot
ax = sea.barplot(x='Choice', y='Subject', data = six, estimator=np.mean, capsize=.2)
#ax = sea.swarmplot(x='Trial', y='Respiratory_Recovery_percentage', data = data, color = '#4B0082')
#ax.set_ylim(96, 102)
plt.title('Survey: Which trial felt more tiring?') # title
plt.ylabel('Quantity') # label
plt.xlabel('Trial') # label

print('Tukey PostHoc Test')
pg.pairwise_tukey(data=six, dv='Subject', between='Choice').round(3)
