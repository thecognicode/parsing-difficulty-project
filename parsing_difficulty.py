import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols


np.random.seed(42)
svo_times = np.random.normal(1.2, 0.2, 30)  
passive_times = np.random.normal(1.5, 0.2, 30)  
osv_times = np.random.normal(1.7, 0.2, 30)  


df = pd.DataFrame({
    'Sentence_Type': ['SVO']*30 + ['Passive']*30 + ['OSV']*30,
    'Reading_Time': np.concatenate([svo_times, passive_times, osv_times])
})


model = ols('Reading_Time ~ Sentence_Type', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)

sns.boxplot(x='Sentence_Type', y='Reading_Time', data=df)
plt.title('Simulated Parsing Difficulty by Sentence Type')


plot_filename = 'parsing_difficulty_plot.png' 
plt.savefig(plot_filename) 
print(f"Plot saved as {plot_filename}")

plt.show()
