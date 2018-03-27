
# coding: utf-8

# In[10]:


import pandas as pd
import matplotlib.pyplot as plt
url = "https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv"
titanic_data = pd.read_csv(url)
labelData = titanic_data["sex"].unique()
by_sex = titanic_data.groupby(["sex"])["pclass"].sum()
print(by_sex)
colors = ["#d62728", "#8c564b"]
plt.pie(by_sex, autopct = "%1.1f%%", shadow = True, colors = colors, labels = {"male", "female"})
plt.title("Presenting the male/female Proportion")
plt.show()
titanic_sampleData = titanic_data.drop(["pclass","survived","name","sex","age","sibsp","parch","ticket","fare","cabin","embarked","boat","body","home.dest"])
colors = ["#d62728", "#8c564b"]
plt.scatter(titanic_sampleData["fare"], titanic_sampleData["age"], s = 60, c = colors, marker = "^")
plt.xlim(0,300)
plt.ylim(0,100)
plt.title("Relationship between Fare and Age")

