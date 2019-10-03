from time import sleep as wait
import random

# ни трогадь! АПАСНА! УБЕТ!

license_key = "43bfuiАЮ_k0p4t1ch"
pro_version = True
goldenLitvin = False

# фсо можишь трогать

if pro_version == True:
	license_key_check = str(input("Введите лицензионный код		"))
	if license_key_check == license_key:
		print("Отлично! Вы авторизованы в системе DankSim")
	else:
		while True:
			print("ТЫ ЛОХ (только если ты не А. Литвин и ты сейчас не тестируещь программу)")

else:
	print("ВЫ ИСПОЛЬЗУЕТЕ БЕСПЛАТНУЮ ВЕРСИЮ ПРОГРАММЫ, ПОЖАЛУЙСТА, ПОДДЕРЖИТЕ РАЗРАБОТЧИКА И КУПИТЕ ПРО-ВЕРСИЮ. СПАСИБО")

counter = []
name_list = ["Борис", "Петрович", "Гопатыч", "Я", "Александр Литвин"]

def AddCustomer():
	global counter
	global goldenLitvin
	chance = random.randint(1, 1000)
	wait(random.randint(1, 5))
	if chance > 0 and chance < 500:
		if goldenLitvin == False:
			if pro_version == True:
				print("Поздравляем! К вам пришел и благославил Вас золотой А. Литвин!!!\n Это бывает лишь раз в жизни!")
				counter.append("Золотой Александр Литвин")
				print(f"Сейчас {counter} покупателей.")
				goldenLitvin = True
			else:
				print("Вы не купили ПРО-ВЕРСИЮ, поэтому Золотой Александр Литвин прошел Ваш магазин! ПОДДЕРЖИТЕ РАЗРАБОТЧИКА!!!")
		else:
			print("Золотой А. Литвин проходил около вашего магазина, но он уже в него заходил, следовательно он просто прошел мимо.")
	else:
		counter.append(random.choice(name_list))
		print(f"Сейчас {counter} покупателей. (1 пришел)")

def RemoveCustomer():
	global counter
	wait(random.randint(2, 4))
	counter.pop(0)
	print(f"1 посетитель ушел. Остались только {counter}")

while True:
	inp = str(input("введите команду:        "))
	if inp == "add":
		AddCustomer()
	elif inp == "del":
		RemoveCustomer()
	elif inp == "info":
		print(counter)
	else:
		print("НЕПРАВИЛЬНЫЙ ВВОД ОШИБКА 0000000")
