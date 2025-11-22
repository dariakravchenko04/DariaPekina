import random
import string

print("Генератор паролей")
print("=" * 20)

length = int(input("Длина пароля: ") or "12")
count = int(input("Количество паролей: ") or "3")

chars = string.ascii_letters + string.digits + "!@#$%"

print("\n Ваши пароли:")
for i in range(count):
    password = ''.join(random.choice(chars) for j in range(length))
    print(f"{i+1}. {password}")

print("\n Готово!")
