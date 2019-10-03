from time import sleep as wait
import random


# ни трогадь! АПАСНА! УБЕТ!

license_key = "43bfuiАЮ_k0p4t1ch"
pro_version = True
goldenLitvin = 0

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
name_list = ["Борис", "Петрович", "Гопатыч", "Я", "Александр Литвин", "Алеша", "Патриарх Кирилл", "Макс", "Иван", "Ольга", "Аллах Бабаха", "Пчелка Майа"]

def AddBaikal():
	pass

def cleanQueue():
	global counter
	if pro_version == True:
	  	print("Вы пригласили вышибалу и он выпнул всех из магазина.")
	    counter = []
  	else:
  		print("Вы не используете про-версию, поэтому не можете нанять вышибалу.")

def AddCustomer():
	global counter
	global goldenLitvin
  shallbaikal = random.randint(1, 100)
	chance = random.randint(1, 1000)
  shahid_aggro = random.randint(1, 100)
	wait(random.randint(1, 5))
	if chance > 0 and chance < 500:
		if goldenLitvin == 0:
			if pro_version == True:
				print("Поздравляем! К вам пришел и благославил Вас золотой А. Литвин!!!\n Это бывает лишь раз в жизни!")
				counter.append("Золотой Александр Литвин")
        print(f"Сейчас {counter} покупателей.")
        goldenLitvin = True
        if shahid_aggro < 50 and shahid_aggro > 0 and :
        		print("аллах бабаха вышел вместе с литвином, ему не понравилось что он золотой а он сам нет и от завести взорвал всех посетителей, после чего литвин дематерилизовался с вашей территорий")
				if shallbaikal < 50 and shallbaikal > 0:
            print("Златой литвин благодать вам святый байкал водица")
            counter.append("бутылочка полулитровая байкала")
            if shallbaikal < 50 and shallbaikal > 0 and shahid_aggro < 50 and shahid_aggro > 0:
            		"аллах бабаха посмотрев на бутылку засунул туда динамит и бутылка лопнула, убивая всех покупателей"
              	counter = []
              	print(f"Сейчас {counter} покупателей")
        		else:
            	 "златой литвин подумал что аллах бабаха сунет взрывчатку в бутылку, но он был неправ"
        else:
        	print("Золотой Алессандро Литвин материализовался в пространстве вашего терроториального субъекта и заподозрив что-то, он выпил весь байкал сам.")
        
			else:
				print("Вы не купили ПРО-ВЕРСИЮ, поэтому Золотой Александр Литвин прошел Ваш магазин! ПОДДЕРЖИТЕ РАЗРАБОТЧИКА!!!")
		else:
			print("Золотой А. Литвин проходил около вашего магазина, но он уже в него заходил, следовательно он просто прошел мимо.")
	else:
		counter.append(random.choice(name_list))
    if counter[-1] == name_list[6]:
    	print("К Вашей персоне лично пришёл Патриарх Кирилл и побрызгал Вас святый водицей!")
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
