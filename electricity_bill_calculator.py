
from num2words import num2words

begin_month = float(input("Oy boshidagi ko‘rsatkich: "))
end_month = float(input("Oy oxiridagi ko‘rsatkich: "))


spent_money = round((end_month - begin_month)*0.45, 2)

eng_res = num2words(spent_money, lang="en", to="currency", currency = "USD")
ru_res = num2words(spent_money, lang="ru", to="currency", currency = "USD")

result = f"To‘lov: ${spent_money} ({eng_res}, {ru_res})"

print(result)