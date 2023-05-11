import pandas

# zda uspěli v maturitě
def evaluate_results(row):
    row = row.iloc[2:]
    if row.mean()<= 1.5 and row.max()<= 2:
        return "Prospěl(a) s vyznamenáním"
    elif row.max()== 5:
        return "Neprospěl(a)"
    else:
        return "Prospěl(a)"
    
data = pandas.read_csv("vysledky.csv")
# přidání sloupce(kde bude výsledek) a použití funkce apply
# axis = 1, chceme spustit po řádcích
# axis = 0, chceme spusti po sloupcích

data["vysledek"] = data.apply(evaluate_results, axis=1)
# print(data)

# zda je zaplacený poplatek a zda musí dělat přijímací zkoušky
def evaluate_application(row):
    # row = row.iloc[1:] - číselné označení sloupečků ze kterých bude funkce iloc vycházet 
    if pandas.isnull(row["Poplatek"]):
        return "Vyřazen - nezaplatil(a)"
    # elif row.iloc[2:6].mean()<=2: při využití označení iloc - číselné označení sloupců od:do
    # alternativa pro výpočet průměru ze známek - jako v loc - slovní  označení sloupců
    elif row["Matematika"] == 1 and row["Český jazyk":"Matematika"].mean() <= 2:
        return "Přijat bez PZ"
    else:
        return "Musí absolvovat PZ"
    
data["prijimaci_zkouska"] = data.apply(evaluate_application, axis=1)
print(data)


