import numpy
import pandas
import datetime
today_date = datetime.datetime(2021, 9, 1)

invoices = pandas.read_csv("invoices.csv")
# print(invoices.dtypes) # zjištění jaké datové typy tabulka obsahuje

# převedení datového typu invoice_date z objectu na datum, datum se převedl špatně měsíc a den,
# musíme nastavit parametr dayfirst=True, aby se datum správně nastavilo - zadávat vždy
invoices["invoice_date_converted"] = pandas.to_datetime(invoices["invoice_date"], dayfirst=True)
# přidání sloupce splatnosti faktur za 60 dní pomocí funkce pandas.Timedelta ("Period x-číslo Day")
# při odčítání dáme místo + pandas.Timedelta/ - pandas.Timedelta
invoices["due_date"] = invoices["invoice_date_converted"] + pandas.Timedelta("P60D")
# zadání podmínky, zda je faktura po splatnosti nebo před splatností, první je hodnota když podmínka platí a druhá hodnota když podmínka neplatí
invoices["status"] = numpy.where(invoices["due_date"] < today_date, "overdue", "before due date")
# jaké množství peněz je na fakturách po splatnosti a před splatností
invoices.groupby("status")["amount"].sum()

print(invoices.head())



