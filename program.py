import pandas

ioef = pandas.read_csv("ioef.csv")
# print(ioef.head())

# vybrali jsem jen pár sloupečků, abychom viděle dle čeho se to seřadilo
ioef = ioef[["Name", "Index Year", "Overall Score"]]

# chceme určit pořadí a to přidáme jako nový sloupeček - pořadí dle Overall Score
# chcem pro každý rok porovnání samostatně - groupby
ioef["Rank"] = ioef.groupby(["Index Year"])["Overall Score"].rank(method="min", ascending=False)

# seřazení dle států a roku:
ioef = ioef.sort_values(["Name", "Index Year"], ascending=[True, False])

# výběr jednoho státu:
# ioef = ioef[ioef["Name"]=="Czech Republic"]

# chceme porovna výsledek z předchozím rokem a dát na jeden řádek
# pomocí groupby("Name") posouvej řádky jen u stejných států
ioef["Rank Previous Year"] = ioef.groupby("Name")["Rank"].shift(-1)

# porovnání výsledků akatuálních s předchozím rokem v novém sloupci:
ioef["Rank Change"] = ioef["Rank"] - ioef["Rank Previous Year"]


print(ioef.head(35))

     
