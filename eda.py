import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def heatMap(df):
    #Create Correlation df
    corr = df.corr()
    #Plot figsize
    fig, ax = plt.subplots(figsize=(10, 10))
    #Generate Color Map
    colormap = sns.diverging_palette(220, 10, as_cmap=True)
    #Generate Heat Map, allow annotations and place floats in map
    sns.heatmap(corr, cmap=colormap, annot=True, fmt=".2f")
    #Apply xticks
    plt.xticks(range(len(corr.columns)), corr.columns);
    #Apply yticks
    plt.yticks(range(len(corr.columns)), corr.columns)
    #show plot
    plt.show()

df = pd.read_csv("./data/stats/on_ice.csv")


f = []

forwards = df[df['Position'].isin(['C','L','R'])]
defenses = df[df['Position'] == 'D']


f_stats = forwards.drop(columns=['Player','Season','Team','Position'])

heatMap(defenses)