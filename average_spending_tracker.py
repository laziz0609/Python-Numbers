from num2words import num2words

print("Haftalik harajatlarni kiriting:")
day1 = float(input("1-kun: "))
day2 = float(input("2-kun: "))
day3 = float(input("3-kun: "))
day4 = float(input("4-kun: "))
day5 = float(input("5-kun: "))
day6 = float(input("6-kun: "))
day7 = float(input("7-kun: "))

total = day1 + day2 + day3 + day4 + day5 + day6 + day7

eng_res = num2words(total, lang="en", to="currency", currency = "USD")
ru_res = num2words(total, lang="ru", to="currency", currency = "USD")

result = f"O‘rtacha harajat: ${total} ({eng_res}, {ru_res})"

print(result)



