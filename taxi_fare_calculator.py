
from num2words import num2words

masofa = float(input("Masofani kiriting (km): "))

total = 3 + (masofa * 1.2)
total = round(total, 2)

eng_res = num2words(total, lang="en", to="currency", currency = "USD")
ru_res = num2words(total, lang="ru", to="currency", currency = "USD")

result = f"Taxi narxi: ${total} ({eng_res}, {ru_res})"

print(result)

