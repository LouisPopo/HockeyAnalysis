import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("./data/cap_hit/18-19caphit.csv")


avg_cap = []
ages = range(20,42)
count = []

for age in ages:
    count.append(data[data['Age'] == age].shape[0])
    avg_cap.append(data['Cap Hit'][data['Age'] == age].mean())

print(count)
plt.scatter(ages, avg_cap, s=count)
plt.xticks(ages)
plt.show()