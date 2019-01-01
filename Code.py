import pandas as pd
import seaborn as sns

data = pd.read_csv(r'https://raw.githubusercontent.com/McGillAISociety/mais-202-coding-challenge/master/data.csv')

average = data.groupby(data.purpose).int_rate.mean()
average = average.reset_index()

figure = sns.barplot(x = 'purpose', y = 'int_rate', data = average)
figure.set_xticklabels(figure.get_xticklabels(), rotation = 'vertical')

print(average.to_string())
