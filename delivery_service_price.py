
from num2words import num2words

masofa = float(input("Masofani kiriting (km): "))

total = 3 + (masofa * 0.8)

eng_res = num2words(total, lang="en", to="currency", currency = "USD")
ru_res = num2words(total, lang="ru", to="currency", currency = "USD")

result = f"Yetkazib berish narxi: ${total} ({eng_res}, {ru_res})"

print(result)

# Masofani kiriting (km): 3.5
# Yetkazib berish narxi: $7.80 (seven dollars and eighty cents, семь долларов восемьдесят центов)