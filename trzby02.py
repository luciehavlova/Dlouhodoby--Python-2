import pandas

# Tento kód je z minulé lekce
# Načtení tabulek s plánem
df_plan = pandas.read_csv("sales_plan.csv")
# Kumulativní součet za rok - groupby("year")
df_plan["sales_plan_cumsum"] = df_plan.groupby("year")["sales"].cumsum()
# Načtení tabulky se skutečnými tržbami
df_actual = pandas.read_csv("sales_actual.csv")
# SEřazení podle data - sort.values("date")
df_actual = df_actual.sort_values("date")
# Vytvoření sloupečku dat - převedení řetězce na typu hodnoty datum a čas
df_actual["date"] = pandas.to_datetime(df_actual["date"])
# uložení měsíce do samostatného sloupce - dt.month
df_actual["month"] = df_actual["date"].dt.month
# uložení roku do samostatného sloupce - dt.year
df_actual["year"] = df_actual["date"].dt.year
# Vytvoření tabulky s agrogovanými/sečtenými tržbami po měsících
df_actual_grouped = df_actual.groupby(["year", "month"]).sum(numeric_only=True)
# Vytvoření kumulativního součtu pro skutečné tržby
df_actual_grouped["sales_actual_cumsum"] = df_actual_grouped.groupby("year")["contract_value"].cumsum()
# Propojední obou tabulek
df_merged = pandas.merge(df_plan, df_actual_grouped, on=["month", "year"])
# vypsání výsledků
# print(df_merged.head())

# vizualizace grafu za rok
year = 2022
# Výběr řádku, které mají ve sloupci year hodnotu 2022, hodnotu můžeme měnit v proměnné year =
# Výběr provedeme pomocí dotazu
df_merged_plot = df_merged[df_merged["year"] == year]
# Reset index - řádky jsou číslovaný od 0
df_merged_plot = df_merged_plot.reset_index() 
# print(df_merged_plot.head())


import matplotlib.pyplot as plt
# Převedení na řetězec: .astype(str)
df_merged_plot["period"] = df_merged_plot["month"].astype(str) + "/" + df_merged_plot["year"].astype(str)
# přidání indexu: nastavení indexu .set_index() dle kterého sloupečku
# přidali se popisky jednotlivých časových úseků 1/2022 - dle indexu
df_merged_plot = df_merged_plot.set_index("period")
# graf pro planovny kumulativní součet s parametry, barvy, název - title(titulek)
ax = df_merged_plot["sales_plan_cumsum"].plot(color ="red", kind ="line", title="Skutečné vs. plánované tržby")
# zadani parametru proměnné ax pro vytvoření jednoho grafu pro obě tabulky dohromady
# grap pro skutečné kumulativní tržby, parametry - kind - "bar" - sloupcový graf
df_merged_plot["sales_actual_cumsum"].plot(kind="bar", ax=ax)

# popisky pro legendu grafu, legendy - dodržet pořadí popisu  
# ylabel - osa y a xlabel - osa x -vodorovná 
plt.legend(["Plán tržeb", "Skutečné tržby"])
plt.ylabel("Miliony EUR")
plt.xlabel("Období")
plt.show()










