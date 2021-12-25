import pandas as pd
import seaborn as sns
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
from sklearn import preprocessing
from scipy.stats import norm

def main():
    df = pd.read_csv('marketing_campaign.csv', delimiter='\t')
    if not df.empty:
        print("DataFrame is accessible")
    num_task = -1
    while (num_task != 0):
        print("|0| Выход")
        print("|1| Задание 1")
        print("|2| Задание 2")
        print("|3| Задание 3")
        print("|4| Задание 4")
        print("|5| Задание 5")
        print("|6| Задание 6")
        print("|7| Задание 7")
        print("|8| Задание 8")
        num_task = int(input("Вевдите номер задания: "))
        if num_task == 1:
            print(df[df.isnull().any(axis=1)])
        elif num_task == 2:
            print(df.drop(columns = ['Z_CostContact', 'Z_Revenue']))
        elif num_task == 3:
            df.rename(columns={'Year_Birth': 'Age'}, inplace=True)
            print(df)
        elif num_task == 4:
            explode = (0.1, 0.05, 0.15, 0.1, 0.2)
            df["Marital_Status"].value_counts(normalize=True).head().plot.pie(explode=explode)
            plt.ylabel('')
            plt.legend()
            plt.show()

            df.loc[df['Response'] == 0]["Marital_Status"].value_counts().head().plot.bar(label="Response 0")
            df.loc[df['Response'] != 0]["Marital_Status"].value_counts().head().plot.bar(color="#f3e151", label="Response 1")
            plt.xlabel('Marital_Status')
            plt.legend()
            plt.show()

            df["Education"].value_counts(normalize=True).head().plot.pie(explode=explode)
            plt.ylabel('')
            plt.legend()
            plt.show()

            df.loc[df['Response'] == 0]["Education"].value_counts().head().plot.bar(label="Response 0")
            df.loc[df['Response'] != 0]["Education"].value_counts().head().plot.bar(color="#f3e151", label="Response 1")
            plt.xlabel('Education')
            plt.legend()
            plt.show()
        elif num_task == 5:
            df.rename(columns={'Year_Birth': 'Age'}, inplace=True)
            data=2021-df['Age']
            ages=data
            mean_plus = ages.mean()
            mean_minus = mean_plus
            sns.distplot(ages, fit=norm, kde = False)
            plt.plot([mean_plus, mean_plus],[0.0,norm.pdf(mean_plus, ages.mean(), ages.std())], color='black')
            for i in range(4):
                mean_plus += ages.std()
                mean_minus -= ages.std()
                plt.plot([mean_plus, mean_plus],[0.0,norm.pdf(mean_plus, ages.mean(), ages.std())], color='black')
                plt.plot([mean_minus, mean_minus],[0.0,norm.pdf(mean_minus, ages.mean(), ages.std())], color='black')
            plt.legend()
            plt.show()
        elif num_task == 6:
            df['Kidhome'].value_counts().head().plot.bar()
            plt.legend()
            plt.show()
            df['Teenhome'].value_counts().head().plot.bar()
            plt.legend()
            plt.show()
            df['Response'].value_counts().head().plot.bar()
            plt.legend()
            plt.show()
            df['Income'].value_counts().head().plot.bar()
            plt.legend()
            plt.show()
            df['Kidhome'].value_counts().head().plot()
            plt.legend()
            plt.show()
            df['Teenhome'].value_counts().head().plot()
            plt.legend()
            plt.show()
            df['Response'].value_counts().head().plot()
            plt.legend()
            plt.show()
            sns.kdeplot(data=df['Income'], shade=True)
            plt.legend()
            plt.show()
        elif num_task == 7:
            sns.displot(df, x='Income', hue='Response', kind='kde', fill=True)
            plt.legend()
            plt.show()
            sns.displot(df, x='Income', hue='Marital_Status', kind='kde', fill=True)
            plt.legend()
            plt.show()
            sns.displot(df, x='Income', hue='Education', kind='kde', fill=True)
            plt.legend()
            plt.show()
            sns.displot(df, x='Income', hue='Kidhome', kind='kde', fill=True)
            plt.legend()
            plt.show()
        elif num_task == 8:
            sns.heatmap(df.corr(), annot=False, vmin=-1, vmax=1, center=0, cmap='coolwarm', fmt='.lg')
            plt.legend()
            plt.show()
        else:
            print("Вы ввели неправильный номер задания") 

        if (input("Хотетите продолжить? (1/0)\n") == '0'):	
            break

if __name__ == "__main__":
    main()
