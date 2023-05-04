import matplotlib.pyplot as plt
import pandas as pd
import sys
import seaborn as sns
import numpy as np

df = pd.read_csv("./results/1.training_results_experiments.csv")
df = df[['workflow','autoscalerArgs','makespan','totalCost','totalReward','episode']]
df['aggMC'] = np.sqrt(df['makespan']/3600**2 + df['totalCost']**2)
df['config'] = [":".join(row[1]['autoscalerArgs'].split(':')[1:6]).replace("w100:500:", "") for row in df.iterrows()]
df['best'] = ((df['workflow'] == 'CyberShake-100') & df['config'].isin(['QL:exp:0.1','SA:exp:0.15'])) | ( (df['workflow'] == 'SIPHT-97') & df['config'].isin(['QL:exp:0.15','SA:exp:0.2'])) | ( (df['workflow'] == 'Montage-100') & df['config'].isin(['QL:exp:0.1','SA:exp:0.1'])) | ( (df['workflow'] == 'LIGO-100') & df['config'].isin(['QL:exp:0.1','SA:exp:0.15']))
df = df[df['best'] == True]
df['Algorithm'] = [row[1]['config'].split(':')[0] for row in df.iterrows()]

df_CS = df[df['workflow'].isin(['CyberShake-100'])]
df_LI = df[df['workflow'].isin(['LIGO-100'])]
df_MO = df[df['workflow'].isin(['Montage-100'])]
df_SP = df[df['workflow'].isin(['SIPHT-97'])]

palette ={"QL:exp:0.1": "C0", "QL:exp:0.15": "C0", "QL:exp:0.2": "C0", "SA:exp:0.1": "C1", "SA:exp:0.15": "C1", "SA:exp:0.2": "C1"}

fig, axs = plt.subplots(4, sharex=False, sharey=False)

metric = "aggMC" #aggMC totalReward

plotCS  = sns.lineplot(ax=axs[0], x="episode", y=metric, data=df_CS, hue="config", palette=palette);
axs[0].set(xlabel='', ylabel="CyberShake")
axs[0].legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0)


plotCS  = sns.lineplot(ax=axs[1], x="episode", y=metric, data=df_LI, hue="config" , palette=palette);
axs[1].set(xlabel='', ylabel="LIGO")
axs[1].legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0)


plotCS  = sns.lineplot(ax=axs[2], x="episode", y=metric, data=df_MO, hue="config", palette=palette);
axs[2].set(xlabel='', ylabel="Montage")
axs[2].legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0)

plotCS  = sns.lineplot(ax=axs[3], x="episode", y=metric, data=df_SP, hue="config", palette=palette);
axs[3].set(xlabel='episode', ylabel="SIPHT")
axs[3].legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0)

plt.show()
