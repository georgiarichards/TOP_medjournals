#!/usr/bin/env python
# coding: utf-8

# # Data analysis for our study on the transparency and open science standards in the policies of medical and health science journals

# The protocol and details of our study is openly availble via the OSF [here](https://osf.io/h2xud/).

# In[1]:


# import libraries required for analysis 
import numpy as np 
import pandas as pd
from pylab import savefig
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# import data 
df1=pd.read_csv("TOP_medj_totals.csv",thousands=',')
df1.head()


# In[3]:


# adding new columns to prepare for analysis - summing total score 
sum_total = df1['Data citation'] + df1['Data transparency'] + df1['Code transparency'] + df1['Materials transparency'] + df1['Design & analysis'] + df1['Study prereg'] + df1['Analysis prereg'] + df1['Replication'] + df1['TOP signatory'] + df1['Reg reports'] + df1['OS badges']
df1['grand_total'] = sum_total


# In[4]:


sum_extras = df1['TOP signatory']+df1['Reg reports']+df1['OS badges']
df1['extra_total'] = sum_extras


# In[5]:


sum_total_TOP = df1['Data citation'] + df1['Data transparency'] + df1['Code transparency'] + df1['Materials transparency'] + df1['Design & analysis'] + df1['Study prereg'] + df1['Analysis prereg'] + df1['Replication'] 
df1['TOP_8'] = sum_total_TOP


# In[6]:


sum_total_COI = df1['COI1'] + df1['COI2'] + df1['COI3'] + df1['COI4']
df1['COI_total'] = sum_total_COI
df1.head()


# # Analysis of total score for journal policies (TOP score + 3 extra items)

# In[7]:


# descriptive stats for grand total score (TOP + extras), out of 29 
df1.groupby('year', as_index=False).agg({"grand_total": "describe"})


# In[8]:


# Calculating the difference in total scores pre-pandemic (Feb 2020) and 'during' (May 2021)
table=pd.pivot_table(df1,index='Journal',columns='year',values='grand_total',aggfunc='mean')
table['diff']=table[2021]-table[2020]
table


# In[9]:


# examining what's driving change in scores - how many extra items, out of 5 
# (i.e. TOP signatory: no=0, yes=1; registered reports: no=0, yes=2; and open science badges: no=0, yes=2)
table=pd.pivot_table(df1,index='Journal',columns='year',values='extra_total',aggfunc='mean')
table['diff']=table[2021]-table[2020]
table


# In[10]:


# determining whether any new TOP signatories (no=0, yes=1)
table=pd.pivot_table(df1,index='Journal',columns='year',values='TOP signatory',aggfunc='mean')
table['diff']=table[2021]-table[2020]
table


# In[11]:


# determining whether any journals have started registered reports (no=0, yes=2) since Feb 2020 audit
table=pd.pivot_table(df1,index='Journal',columns='year',values='Reg reports',aggfunc='mean')
table['diff']=table[2021]-table[2020]
table


# In[12]:


# determining whether any journals have implemented open science badges (no=0, yes=2) since Feb 2020 audit
table=pd.pivot_table(df1,index='Journal',columns='year',values='OS badges',aggfunc='mean')
table['diff']=table[2021]-table[2020]
table


# In[13]:


df2 = df1.sort_values(by=['grand_total', 'Journal'],
                      ascending=[False, True])
df2.head()


# In[14]:


# plotting the grand total score (TOP 8 + 3 extras) for 2020 & 2021, score out of 29 
plt.figure(figsize=(10,12))
sns.set_color_codes("colorblind")
ax = sns.barplot(data=df2, x="grand_total", y="Journal", hue="year")
plt.xlabel('Total policy scores, out of 29', fontsize=15)
plt.xticks(fontsize=15)
plt.ylabel('Journals', fontsize=15)
plt.legend(title='year', title_fontsize=15, fontsize=15)
degrees=0
plt.yticks(fontsize=15, rotation=degrees)
ax.set(xlim=(0, 29))

plt.savefig("fig_totalTOP_20-21.png", dpi=600)


# # Analysis of TOP guidelines, 8 standards 

# In[15]:


# descriptive stats for total TOP score (8 standards), out of 24
df1.groupby('year', as_index=False).agg({"TOP_8": "describe"})


# In[16]:


table=pd.pivot_table(df1,index='Journal',columns='year',values='TOP_8',aggfunc='mean')
table['diff']=table[2021]-table[2020]
table


# In[17]:


# sorting the order of the journals 
df3 = df1.sort_values(by=['TOP_8', 'Journal'],
                      ascending=[False, True])
df3.head()


# In[18]:


# plotting the total TOP score for 2020 & 2021

plt.figure(figsize=(10,12))
sns.set_color_codes("colorblind")
ax = sns.barplot(data=df3, x="TOP_8", y="Journal", hue="year")
plt.xlabel('Total TOP scores, out of 24', fontsize=15)
plt.xticks(fontsize=15)
plt.ylabel('Journals', fontsize=15)
plt.legend(title='year', title_fontsize=15, fontsize=15)
degrees=0
plt.yticks(fontsize=15, rotation=degrees)
ax.set(xlim=(0, 24))

plt.savefig("fig_TOP_20-21.png", dpi=600)


# In[20]:


f, ax = plt.subplots(figsize=(13, 16))

# Plot grand total
sns.set_color_codes("pastel")
sns.barplot(data=df2, x="grand_total", y="Journal", hue="year", color='b')

# Plot TOP 8 standards
sns.set_color_codes("colorblind")
sns.barplot(data=df2, x="TOP_8", y="Journal", hue="year", color='b')

# Add a legend and informative axis label
ax.set(xlim=(0, 29))
degrees=0
plt.xticks(fontsize=15)
plt.yticks(fontsize=15, rotation=degrees)
plt.ylabel('Journals', fontsize=15)
plt.xlabel("Total policy scores", fontsize=15)
plt.legend(title='year', title_fontsize=15, fontsize=15)

plt.savefig("TOPcombined_20-21.png", dpi=600)


# # Descriptive stats for each measure of TOP standards 

# In[21]:


# Citation summary - a score out of 0 to 3 
df1.groupby('year', as_index=False).agg({"Data citation": "describe"})


# In[22]:


# difference in citation scores 
table=pd.pivot_table(df1,index='Journal',columns='year',values='Data citation',aggfunc='mean')
table['diff']=table[2021]-table[2020]
table


# In[23]:


# Data transparency summary - a score out of 0 to 3 
df1.groupby('year', as_index=False).agg({"Data transparency": "describe"})


# In[24]:


# difference in Data transparency scores 
table=pd.pivot_table(df1,index='Journal',columns='year',values='Data transparency',aggfunc='mean')
table['diff']=table[2021]-table[2020]
table


# In[25]:


# Analystic methods (code) summary - a score out of 0 to 3 
df1.groupby('year', as_index=False).agg({"Code transparency": "describe"})


# In[26]:


# difference in Analytical methods (code) scores 
table=pd.pivot_table(df1,index='Journal',columns='year',values='Code transparency',aggfunc='mean')
table['diff']=table[2021]-table[2020]
table


# In[27]:


# Materials summary - a score out of 0 to 3 
df1.groupby('year', as_index=False).agg({"Materials transparency": "describe"})


# In[28]:


# difference in Materials scores 
table=pd.pivot_table(df1,index='Journal',columns='year',values='Materials transparency',aggfunc='mean')
table['diff']=table[2021]-table[2020]
table


# In[29]:


# Design & analysis summary - a score out of 0 to 3
df1.groupby('year', as_index=False).agg({"Design & analysis": "describe"})


# In[30]:


# difference in Design & analysis scores 
table=pd.pivot_table(df1,index='Journal',columns='year',values='Design & analysis',aggfunc='mean')
table['diff']=table[2021]-table[2020]
table


# In[31]:


# Study prereg summary - a score out of 0 to 3 
df1.groupby('year', as_index=False).agg({"Study prereg": "describe"})


# In[32]:


# difference in Study prereg scores 
table=pd.pivot_table(df1,index='Journal',columns='year',values='Study prereg',aggfunc='mean')
table['diff']=table[2021]-table[2020]
table


# In[33]:


# Analysis prereg summary - a score out of 0 to 3 
df1.groupby('year', as_index=False).agg({"Analysis prereg": "describe"})


# In[34]:


# difference in Analysis prereg scores 
table=pd.pivot_table(df1,index='Journal',columns='year',values='Analysis prereg',aggfunc='mean')
table['diff']=table[2021]-table[2020]
table


# In[35]:


# Replication summary - a score out of 0 to 3 
df1.groupby('year', as_index=False).agg({"Replication": "describe"})


# In[36]:


# difference in Replication scores 
table=pd.pivot_table(df1,index='Journal',columns='year',values='Replication',aggfunc='mean')
table['diff']=table[2021]-table[2020]
table


# # Analysis of COI scores from the International Committee of Medical Journal Editors (ICMJE) disclosure form 

# In[37]:


# descriptive stats for COI total score, out of 4
df1.groupby('year', as_index=False).agg({"COI_total": "describe"})


# In[38]:


# sorting the order of the journals 
df4 = df1.sort_values(by=['COI_total', 'Journal'],
                      ascending=[False, True])
df4.head()


# In[39]:


# plotting the total COI score for 2020 & 2021, out of 4 points 

plt.figure(figsize=(10,12))
sns.set_color_codes("colorblind")
ax = sns.barplot(data=df4, x="COI_total", y="Journal", hue="year")
plt.xlabel('Total COI scores, out of 4', fontsize=15)
plt.xticks(fontsize=15)
plt.ylabel('Journals', fontsize=15)
plt.legend(title='year', title_fontsize=15, fontsize=15)
degrees=0
plt.yticks(fontsize=15, rotation=degrees)
ax.set(xlim=(0, 5))

plt.savefig("fig_COI_20-21.png", dpi=600)


# # Figures for 2020 scores

# In[8]:


# for 2020: plotting the grand total score (TOP 8 + 3 extras), out of a possible 29 points 

f, ax = plt.subplots(figsize=(13, 16))

# Plot grand total
sns.set_color_codes("pastel")
sns.barplot(x="grand_total", y="Journal", data=df,
            label="Total of 29", color="b")

# Plot TOP 8 standards
sns.set_color_codes("muted")
sns.barplot(x="TOP_8", y="Journal", data=df,
            label="TOP total of 24", color="b")

# Add a legend and informative axis label
ax.legend(ncol=1, loc="upper right", frameon=True, fontsize=13)
ax.set(xlim=(0, 18), 
       ylabel="")

degrees=50
plt.xticks(fontsize=15)
plt.yticks(fontsize=15, rotation=degrees)
plt.xlabel("Total TOP scores", fontsize=16)

plt.savefig("fig1_totalTOPcombined.png", dpi=600)


# In[9]:


# plotting the total COI scores for 2020, score out of 4 

plt.figure(figsize=(13,16))
sns.set_color_codes("muted")
ax = sns.barplot(data=df, x="COI_total", y="Journal", color="b")
plt.xlabel('Total COI scores, out of 4', fontsize=15)
plt.xticks(fontsize=15)
plt.ylabel(' ')
degrees=50
plt.yticks(fontsize=15, rotation=degrees)
ax.set(xlim=(0, 5))

plt.savefig("fig2_COI.png", dpi=600)


# In[13]:


# plotting the grand total score (TOP 8 + 3 extras) for 2020, total out of 29 

plt.figure(figsize=(8,12))
ax = sns.barplot(data=df, x="grand_total", y="Journal", color="navy")
plt.xlabel('Total TOP scores, out of 29', fontsize=15)
plt.xticks(fontsize=15)
plt.ylabel(' ')
degrees=50
plt.yticks(fontsize=11, rotation=degrees)

plt.savefig("fig1_totalTOP.png", dpi=600)


# In[ ]:




