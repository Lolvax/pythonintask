#Задача №5
#Вариант 21.
#Напишите программу, которая бы при запуске случайным
#образом отображала название одной из
#двадцати восьми стран, входящих в Европейский союз.

#Pchelintsev M.A.
#11.04.16

import random

print("Напишите программу, которая бы при запуске случайным образом отображала название одной из двадцати восьми стран, входящих в Европейский союз.")

country = random.randint(1,27)

print('\nСтрана', end=' ')

if country == 1 :
    print('Хорватия')
elif country == 2 :
    print('Чехия') 
elif country == 3 :
    print('Швеция')
elif country == 4 :
    print('Австрия')
elif country == 5 :
    print('Бельгия')
elif country == 6 :
    print('Болгария')
elif country == 7 :
    print('Венгрия')
elif country == 8 :
    print('Великобритания')
elif country == 9 :
    print('Греция')
elif country == 10 :
    print('Германия')
elif country == 11 :
    print('Дания')
elif country == 12 :
    print('Италия')
elif country == 13 :
    print('Ирландия')
elif country == 14 :
    print('Испания')
elif country == 15 :
    print('Республика Кипр')
elif country == 16 :
    print('Люксембург')
elif country == 17 :
    print('Латвия')
elif country == 18 :
    print('Литва')
elif country == 19 :
    print('Мальта')
elif country == 20 :
    print('Нидерланды')
elif country == 21 :
    print('Португалия')
elif country == 22 :
    print('Польша')
elif country == 23 :
    print('Румыния')
elif country == 24 :
    print('Словения')
elif country == 25 :
    print('Словакия')
elif country == 26 :
    print('Франция')
elif country == 27 :
    print('Финляндия')
else :
    print('Эстония')



input("\n\nНажмите Enter для выхода.")