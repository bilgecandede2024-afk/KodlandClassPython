import random

LettersMaybe = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

SpecificThingy = input("Özel bir şeyi giriniz: ")
Pleng = int(input("Lütfen parolanın uzunluğunu giriniz: "))

Password = ""


half_length = Pleng // 2

first_half = ""
second_half = ""

for i in range(half_length):
    first_half += random.choice(LettersMaybe)

for i in range(Pleng - half_length):
    second_half += random.choice(LettersMaybe)

Password = first_half + SpecificThingy + second_half

print(Password)
