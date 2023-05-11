import pandas

signal_monitoring = pandas.read_csv("signal_monitoring.csv")
signal_monitoring["event_date_time"] = pandas.to_datetime(signal_monitoring["event_date_time"])
# nový sloupeček, a přidám funkci shift tak, aby se dva řádky napsali vedle sebe - ztracení signálu a obnovení
signal_monitoring["event_end_date_time"] = signal_monitoring["event_date_time"].shift(-1)
signal_monitoring["outage_lenght"] = signal_monitoring["event_end_date_time"] - signal_monitoring["event_date_time"]
# převedení na sekundy:
signal_monitoring["outage_lenght"] = signal_monitoring["outage_lenght"].dt.total_seconds()


# vybereme jen ty řádky, kdy byl výpadek signálu
signal_monitoring = signal_monitoring[signal_monitoring["event_type"] == "signal lost"]

print(signal_monitoring["outage_lenght"].mean())

