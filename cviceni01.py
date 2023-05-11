import pandas

# Načtení dat
inventory = pandas.read_csv("inventory.csv")
# print(inventory)

# Pomocí kumulativního součtu vytvoř v tabulce sloupec, 
# který udává množství každého z produktů na skladě:
inventory = inventory.sort_values(["product_code", "date"]) 
# seřadíme tabulku dle produktů a datum (nunté dodržet pořadí)
inventory["quantity_cumsum"] = inventory.groupby("product_code")["quantity"].cumsum()
# seskupíme dle produktů, abychom měli ke každému produktu jedno datum a uděláme kumulativní součet množství
# print(inventory.head())
                                  
# V daném období zažíval obchod problémy se zásobováním a některé zboží tak bylo vyprodané. 
# Zjisti pro každý z produktů, kolik dní v roce byl vyprodaný, tj. kolik dní v roce byl stav zásob 0.

vyprodano = inventory[inventory["quantity_cumsum"] == 0]
# vybereme řádky kde je vyprodáno a uložíme do nové tabulky vyprodano
vyprodano = vyprodano.groupby("product_code").size()
# zjistíme kolikrát bylo zboží vyprodané podle produktu
# print(vyprodano)

# s funkcí count() by to ukázalo hodnoty pro každý sloupeček, 
# s funkcí size() ukáže jeden sloupec pro každý produkt a ukáže kolikrát se vyskytla hodnota

# Vytvoř novou tabulku, kde ponecháš pro dané zboží pouze dny, kdy zboží nebylo vyprodáno. 
# Z této tabulky pak spočítej průměrný počet prodaných kusů zboží za den. 

zbozi = inventory[inventory["quantity"]<=0] # nechceme započítat doplňované zásoby, ale jen prodané produkty
zbozi = zbozi[zbozi["quantity_cumsum"]!=0] # odstraníme řádky kde kumulativní součet je nula, kdy není zboží vyprodáno
zbozi = zbozi.groupby("product_code")["quantity"].mean() # průměr prodaných kusů
print(zbozi)

# Pomocí agregace spočítej, kolik bylo v průměru prodáno každého zboží - viz. průměr nahoře








