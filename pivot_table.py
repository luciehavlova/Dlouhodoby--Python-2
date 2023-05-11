# Kontingenční tabulky (pivot): 

import pandas
df_actual = pandas.read_csv("sales_actual.csv")
# print(df_actual.head())

# můžeme tržby vydělit proto, aby čísla byla menší(není nutné, ale je to přehlednější)
# df_actual["contract_value"] = df_actual["contract_value"] / 1_000_000
# ukazuje tržby: funkce: aggfunc=sum 
df_actual_pivot = pandas.pivot_table(data=df_actual, index="country", columns="sales_manager", values="contract_value", aggfunc=sum, fill_value=0)
# fill_value = 0, nejsou-li hodnoty, tak by se vypsalo NaN, proto se zadává fill_value=0, pak vypíše nulu


# ukazuje počet uzavřených obchodů: len, změna funkce aggfunc=len
# df_actual_pivot = pandas.pivot_table(data=df_actual, index="country", columns="sales_manager", values="contract_value", aggfunc=len, fill_value=0)

# Relativní hodnoty: 
# součet všech sloupečků i řádků pomocí parametru: margins=True, součet každé země u každého obchodníka
df_actual_pivot = pandas.pivot_table(data=df_actual, index="country", columns="sales_manager", values="contract_value", aggfunc=sum, fill_value=0, margins=True)

# jaké procent z tržeb udělal obchodník: div() - dělení, .iloc[: - všechny řádky, -1 - poslední sloupeček],
# axis - jakým způsobem chci pracovat s dělením, 0 "směr", jakým budeme dělit(sloupce)
# 0 nejdřív vezmi první sloupeček a vyděl posledním, pak druhý sloupeček a vyděl posledním atd.
# 1 nejdřív vezmi první řádek a vyděl posledním, pak druhý řádek...atd.
# kolik % dělá který tým v té konkrétní zemi:
# df_actual_pivot = df_actual_pivot.div(df_actual_pivot.iloc[:, -1], axis=0)

# chci poslední řádek, chci všechny sloupce, dělíme jednotlivý řádky axis=1,
# procento všech tržeb v jedntlivých zemích, % úspěšnost týmů
df_actual_pivot = df_actual_pivot.div(df_actual_pivot.iloc[-1, :], axis=1)
print(df_actual_pivot)


# Skupiny:
# df_actual["group"] vytovřím nový sloupeček, ["contract_value"] dle čeho dělím na skupiny
# float("inf") inf infinity nekonečno, float - převod na desetinné číslo
df_actual["group"] = pandas.cut(df_actual["contract_value"], [0, 300_000, 1_000_000, float("inf")], labels=["small", "medium", "big"])

print(df_actual)
