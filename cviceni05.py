import pandas
from scipy import stats
import matplotlib.pyplot as plt
import seaborn

data = pandas.read_csv("house_prices.csv")
# print(data.head())

# Plocha Garáže
data_sloupce = data[["GarageArea", "SalePrice"]]
print(data_sloupce.corr())

seaborn.scatterplot(data=data_sloupce, x="GarageArea", y="SalePrice")
plt.show()

seaborn.scatterplot(data=data[data["GarageArea"]>0], x="GarageArea", y="SalePrice")
plt.show()

# Plocha Pozemku
data_pozemek = data[["LotArea", "SalePrice"]]
print(data_pozemek.corr())

seaborn.scatterplot(data=data_pozemek, x="LotArea", y="SalePrice")
plt.show()

# Plocha pozemku x obytná plocha domu
data_pozemek_dum = data[["LotArea", "GrLivArea"]]
print(data_pozemek_dum.corr())

seaborn.scatterplot(data=data_pozemek_dum, x="LotArea", y="GrLivArea")
plt.show()
# decribe() - vydíme základní statistické údaje buď pro všechny sloupce nebo jen na vybrané
# např. count(), mena(), std()....
print(data["GrLivArea"].describe())

data["GrLivArea"].hist(bins=25)
data["GrLivArea"].plot.kde()
plt.boxplot(data["GrLivArea"])
plt.show()
# vetšina známek je menší než 3
znamky = pandas.Series([1, 1, 2, 2, 3, 4, 5, 100])
znamky.median()
znamky.mean()

znamky.plot.kde()
plt.boxplot(data["GrLivArea"])
plt.show()







