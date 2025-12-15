

from num2words import num2words


money = float(input("Pul miqdorini kiriting ($): "))

total = money

fifty_doll = money // 50
money = money % 50

ten_doll = money // 10
money = money % 10

five_doll = money // 5
money = money % 5

result = f"$50 kupyuradan: {int(fifty_doll)} ta\n"
result += f"$10 kupyuradan: {int(ten_doll)} ta\n"
result += f"$5 kupyuradan: {int(five_doll)} ta\n"
result += f"$1 kupyuradan: {round((money))} ta\n"  # bunga round qilishimni sababi chunki mijoz biror narsa sotib olayotganda mahsulot narxidan kam berishi mumkin emas (ko'proq berib qaytim olishi mumkin)
result += f"Umumiy summa: {total} ({num2words(total)}, {num2words(total)})"

print(result)

