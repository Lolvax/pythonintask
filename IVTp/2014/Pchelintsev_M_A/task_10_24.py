print ("""
			Добро пожаловать в "Генератор персонажей"
		Вы можете распределить 30 очков между 4 характеристиками:
	Сила,здоровье,Мудрость и Ловкость.Вы можете как и брать из общего
числа пунктов,так и возвращать. Удачи!
 """)
STR=0
HP=0
INT=0
AGL=0
point=30
chislo=0
print("Если хотите изменить Силу,то напишите 'Сила'.Если Здоровье,то 'Здоровье'.Если Мудрость,то 'Мудрость'.Если Ловкость,то 'Ловкость'")
while True:
       if STR<0 or HP<0 or INT<0 or AGL<0 or point>30:
              print("Ошибка")
              break
              #chislo=int (inpuit("Напишите слова"))
       elif point==0:
              print("Вы распределили очки. Их распределение:\nСила:",STR,"\nЗдоровье:",HP,"\nМудрость:",INT,"\nЛовкость:",AGL)
              break
       print("Ваши очки:\nСила:",STR,"\nЗдоровье:",HP,"\nМудрость:",INT,"\nЛовкость:",AGL,"\nНераспределенные очки:",point)
       user_input=input("")
       if user_input=="Сила" :
              chislo=int(input("Сколько хотите прибавить(отбавить)?"))
              if chislo <= point :
                            STR+=chislo
                            point-=chislo
              else :
                     print('Слишком много')
       elif user_input=="Здоровье":
              chislo=int(input("Сколько хотите прибавить(отбавить)?"))
              if chislo <= point :
                            HP+=chislo
                            point-=chislo
              else :
                     print("Слишком много")
       elif user_input=="Мудрость" :
              chislo=int(input("Сколько хотите прибавить(отбавить)?"))
              if chislo <= point :
                            INT+=chislo
                            point-=chislo
              else :
                     print("Слишком много")
       elif user_input=="Ловкость":
              chislo=int(input("Сколько хотите прибавить(отбавить)?"))
              if chislo <= point :
                            AGL+=chislo
                            point-=chislo
              else :
                     print("Слишком много")
inpuit ("Нажмите Enter для выхода.")
