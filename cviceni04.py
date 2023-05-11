# Uchazeči a uchazečky musejí absolvovat tři písemné testy: test z anglického jazyka, matematiky a českého jazyka. 

# je jeho skóre rovno součtu bodů ze všech tří testů. Dále uvažujeme, že za aktivity uchazeče přičítáme bonusové body:

# 
# za účast na letní škole dostane 5 bonusových bodů.



import pandas
# row - po řádcích
def get_points(row):
    # pokud dostane z některého testu méně než 60 bodů dostane hodnocení 0
    if row["body_aj":"body_cj"].min() < 60:
        points = 0
    # pokud více než 60 bodů, je jeho skóre rovno součtu bodů ze všech tří testů.
    else:
        points = row["body_aj":"body_cj"].sum()
        # pokud hodnota ve sloupečeku souteže není prázdná
        if not pandas.isnull(row["souteze"]):
            # pokud se uchazeč hlásí na obor elektro či informatika
            if row["obor"] in ["Elektrotechnika", "Informatika"]:
                # přidělené bonusové body za fyzickální nebo matematicku olympiádu
                if "matematická" in row["souteze"] or "fyzikální" in row["souteze"]:
                    points = points + 10
            # za 1. až 10. místo v některé z olympiád 10 bonusových bodů
            points = points + 10
        # pokud hodnota ve sloupečku letní škole je ano
        if row["letni_skola"] == "ano":
            points = points + 5
    return points

    # if row[3:6].min() < 60:
        # return 0
    # elif row[3:6].sum():
        # return 

def decision(row):
    if row["poradi"] <= 30:
        decision = "ano"
    else:
        decision = "ne"
    return decision

   
zkousky = pandas.read_csv("prijimaci_zkousky.csv")
zkousky["body"] = zkousky.apply(get_points,axis=1)
# axis=1 - procházet řádek po řádku
# novou tabulku, která obsahuje pouze uchazeče a uchazečky, kteří mají nenulové hodnocení.
zkousky = zkousky[zkousky["body"]> 0]
# využij metodu rank() k výpočtu pořadí uchazeče v rámci daného oboru
zkousky["poradi"] = zkousky.groupby("obor")["body"].rank(ascending=False, method="min")
# data seřaď podle oboru a počtu bodů
zkousky = zkousky.sort_values(["obor", "poradi"])
zkousky["prijat"] = zkousky.apply(decision, axis=1)
zkousky_prijati = zkousky[zkousky["prijat"] == "ano"]
print(zkousky.head(15))



