import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from datetime import datetime


#################################################task 1
df = pd.read_csv("marketing_campaign.csv", delimiter="\t")
df.sample(10)


#################################################task 2
df.info()


#################################################task 3
df[df.isnull().T.any()]



#################################################task 4
df.drop(["Z_CostContact", "Z_Revenue"], axis=1, inplace=True)



#################################################task 5
df.rename({"Year_Birth": "Age"}, axis=1, inplace=True)


#################################################task 6
ms_df_c = df["Marital_Status"].value_counts().to_frame()
ms_df = ms_df_c[ms_df_c["Marital_Status"] > 50]
ed_df = df["Education"].value_counts().to_frame()
ms_df[ms_df["Marital_Status"] > 50].plot(
    kind='pie',
    autopct='%1.1f%%',
    legend=None,
    ylabel="",
    subplots=True,
    shadow=False,
    explode=(0.13, 0.1, 0.1, 0.25, 0.15),
    title="Marital Status",
    figsize = (6,6)
)
plt.show()
ed_df.plot(
    y="Education",
    kind='pie',
    autopct='%1.1f%%',
    legend=None,
    ylabel="",
    shadow=False,
    explode=(0.13, 0.1, 0.1, 0.25, 0.15),
    title="Education",
    figsize = (6,6)

)
plt.show()
sns.histplot(data=df, x="Marital_Status", stat='percent', hue="Response")
plt.show()
sns.histplot(data=df, x="Education", stat='percent', hue="Response")
plt.show()


#################################################task 7
def calculate_age(born) -> int:
    return int(datetime.today().strftime("%Y")) - int(born)

df["Age"] = df["Age"].apply(calculate_age)
filtered_df = df[df["Age"] < 100]
sns.histplot(x=filtered_df["Age"], kde=True)
plt.show()


#################################################task 8
def show_bar(data_name: str) -> None:
    df[data_name].value_counts(normalize=True).mul(100).to_frame().plot(
        kind='bar',
        legend=None,
        xlabel=data_name,
        ylabel="Percent"
    )
    plt.show()

show_bar("Kidhome")
show_bar("Teenhome")
show_bar("Response")
sns.kdeplot(df["Income"], shade=True, clip=(10**0, 10**5.1))
plt.show()

#################################################task 9
def show_kde(hue: str, clip: tuple = (10**0, 10**5.05)):
    plt.figure(figsize = (7, 7))
    sns.kdeplot(data=df, x="Income", hue=hue, shade=True, clip=clip)
    plt.show()

show_kde("Response")
show_kde("Marital_Status")
show_kde("Education")
show_kde("Kidhome")

#################################################task 10
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
newdf = df.select_dtypes(include=numerics)
plt.figure(figsize = (20,20))
sns.heatmap(newdf.corr(), cmap='coolwarm', annot=True, fmt='.1g')
plt.show()