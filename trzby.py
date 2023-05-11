import pandas

# Načtení souboru - plánované tržby
df_plan = pandas.read_csv("sales_plan.csv")
# print(df_plan.head())

# kumulativní součet - přidání sloupečku kumulativního součtu:
# zobrazí součty za celé období - za všechny měsíce i roky
# df_plan["sales_plan_cumsum"] = df_plan["sales"].cumsum()
# print(df_plan.tail())

# uprava programu tak, aby sčítal hodnoty podle jednotlivých roků:
# metoda groupby()-dle čeho chceme sdružovat
df_plan["sales_plan_cumsum"] = df_plan.groupby("year")["sales"].cumsum()
# print(df_plan)

# načtení souboru skutečných tržeb
df_actual = pandas.read_csv("sales_actual.csv")
# print(df_actual)

# seřadíme data dle datumu ("date") -jak nabíhají tržby:
df_actual = df_actual.sort_values("date")
# print(df_actual.head())

# agregovat data dle měsíce a roku - z více čísel agregovat do jednoho čísla
# bere data jako obyčejný text a musíme tedy převést hodnoty
# to_datetime - převod na typ datum a čas: přepisujeme/nahrazujeme původní sloupeček "date"
df_actual["date"] = pandas.to_datetime(df_actual["date"]) 
# vytvořím/přidám sloupeček month, kde bude číslo měsíce-zjisti měsíc
df_actual["month"] = df_actual["date"].dt.month
# vytvořím/přidám sloupeček year, kde bude číslo roku-zjisti rok
df_actual["year"] = df_actual["date"].dt.year
# print(df_actual.head())


# agregace podle roku a měsíce - součet
# df_actual = df_actual.drop(columns="date")
df_actual_grouped = df_actual.groupby(["year", "month"]).sum()
# groupby - sečte tržeb za každý měsíc dle roků - méně řádku, 
# např. součet za měsíc únor, roku 2020, každý měsíc jiné číslo
# print(df_actual_grouped)

# kumulativní součet
df_actual_grouped["sales_actual_cumsum"] = df_actual_grouped.groupby("year")["contract_value"].cumsum()
print(df_actual_grouped["sales_actual_cumsum"])

# propojení obou tabulek
df_merged = pandas.merge(df_plan, df_actual_grouped, on=["month", "year"])

# print(df_merged)








