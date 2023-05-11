import pandas
titanic = pandas.read_csv("titanic.csv")

# porovná závislost mezi pohlavím cestujícího (sloupec Sex) 
# a tím, jesti přežil potopení Titanicu (sloupec Survived).

titanic_pivot_table = pandas.pivot_table(data=titanic, values="Name", index="Sex", columns=["Survived"],aggfunc=len)
# print(titanic_pivot_table)




# 4 Skupiny:
titanic["group"] = pandas.cut(titanic["Age"], [0, 15, 20, 60, float("inf")], labels=["child", "teenager", "adults", "senior"])

print(titanic.head())


