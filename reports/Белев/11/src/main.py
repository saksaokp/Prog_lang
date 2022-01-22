from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

table = pd.read_csv('marketing_campaign.csv', delimiter='\t')

if table.isnull().any().any():
    print(table.isnull().any())

table.pop('Z_CostContact')
table.pop('Z_Revenue')

table.rename(columns={'Year_Birth': 'Age'}, inplace=True)
print(table)

marital_status_c = table["Marital_Status"].value_counts().to_frame()
marital_status = marital_status_c[marital_status_c["Marital_Status"] > 50]
education = table["Education"].value_counts().to_frame()

marital_status[marital_status["Marital_Status"] > 50].plot(
    kind='pie',
    autopct='%1.2f%%',
    legend=None,
    ylabel="",
    subplots=True,
    shadow=False,
    explode=(0.13, 0.1, 0.1, 0.25, 0.15),
    title="Marital Status",
    figsize=(6, 6)
)
plt.show()

education.plot(
    y="Education",
    kind='pie',
    autopct='%1.1f%%',
    legend=None,
    ylabel="",
    shadow=False,
    explode=(0.13, 0.1, 0.1, 0.25, 0.15),
    title="Education",
    figsize=(6, 6)

)
plt.show()

sns.histplot(data=table, x="Marital_Status", stat='percent', hue="Response")
plt.show()
sns.histplot(data=table, x="Education", stat='percent', hue="Response")
plt.show()


def age(born):
    return 2021 - int(born)


table["Age"] = table["Age"].apply(age)
filtered_table = table[table["Age"] < 100]
sns.histplot(x=filtered_table["Age"], kde=True)
plt.show()


def bar(data_name: str) -> None:
    table[data_name].value_counts(normalize=True).mul(100).to_frame().plot(
        kind='bar',
        legend=None,
        xlabel=data_name,
        ylabel="Percent"
    )
    plt.show()


bar("Kidhome")
bar("Teenhome")
bar("Response")
sns.kdeplot(table["Income"], shade=True, clip=(10 ** 0, 10 ** 5.1))
plt.show()


def grph(hue: str, clip: tuple = (10 ** 0, 10 ** 5.05)):
    plt.figure(figsize=(7, 7))
    sns.kdeplot(data=table, x="Income", hue=hue, shade=True, clip=clip)
    plt.show()


grph("Response")
grph("Marital_Status")
grph("Education")
grph("Kidhome")

plt.figure(figsize=(20, 20))
sns.heatmap(table.corr(), cmap='coolwarm', annot=True, fmt='.1g')
plt.show()
