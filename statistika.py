import pandas

data = pandas.read_csv("house_prices.csv")
print(data.head())

# průměr a medián

# jaká je cenová úroveň 
# print(data["SalePrice"].mean())

# najde prostřední hodnotu - median
#print(data["SalePrice"].median())
           
# rozptyl - jak různorodé (variability) hodnoty jsou v rámci skupiny
# Načteme data
data_RM = data[data["MSZoning"] == "RM"]
data_RH = data[data["MSZoning"] == "RH"]
# Zjistíme průměry
# print(data_RM["SalePrice"].mean())
# print(data_RH["SalePrice"].mean())
# Zjistíme rozptyly var()-variance
# print(data_RH["SalePrice"].var())
# print(data_RM["SalePrice"].var())

# kvantil - např. když chceme vědět jaká je hodnota pro 10%, taková
# čísla označujeme jako kvantily - tzn. 10% je menších a zbylých 90 % je větších
# můžeme použít i jiný poměr(median je poměr 50% na 50%)
# print(data["SalePrice"].quantile(0.9))

# inverzní kvantilová funkce - inverzní=opačný, kolik procent hodnot je menších než
# nějaká vybraná hodnota

from scipy import stats
# print(stats.percentileofscore(data["SalePrice"], 200_000))

# histogram - graf
import matplotlib.pyplot as plt
# data["SalePrice"].hist(bins=25)
# plt.show()

# funkce hustoty:
# data["SalePrice"].plot.kde()
# plt.show()

# korelace - závislost
import seaborn
# seaborn.scatterplot(data=data, x="GrLivArea", y="SalePrice")
# plt.show()
# korelační koeficient - blízko 0 jsou realivně nezávislý, je-li to blízko 1 - hodnoty současně
# rostou - jsou lineárně závislý, je-li tam -1 - nepřímá lineární závislost, tj. jedna hodnota roste a 
# současně druhá klesá
data_vybrane_sloupce = data[["GrLivArea", "SalePrice"]]
print(data_vybrane_sloupce.corr())



