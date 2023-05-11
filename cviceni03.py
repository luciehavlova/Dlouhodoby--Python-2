import pandas

pulmaraton = pandas.read_csv("half_marathon.csv")

pulmaraton = pulmaraton.sort_values(["Jmeno", "Rok zavodu"])

pulmaraton["Cas zavodnika"] = pandas.to_datetime(pulmaraton["Cas zavodnika"])
pulmaraton["Cas zavodnika 2020"] = pulmaraton.groupby("Jmeno")["Cas zavodnika"].shift(-1)
# vymaže řádky kde jsou 0 a vyresetuje index
pulmaraton = pulmaraton.dropna().reset_index()
pulmaraton["Rozdil"] = pulmaraton["Cas zavodnika 2020"] - pulmaraton["Cas zavodnika"] 
pulmaraton["Rozdil"] = pulmaraton["Rozdil"].dt.total_seconds()

print(pulmaraton)
