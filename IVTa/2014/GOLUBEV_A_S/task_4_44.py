# Задача 4. Вариант 44.
# Напишите программу, которая выводит имя, под которым скрывается Борис Николаевич Бугаев. 
# Дополнительно необходимо вывести область интересов указанной личности, место рождения, 
# годы рождения и смерти (если человек умер), вычислить возраст на данный момент (или момент смерти). 
# Для хранения всех необходимых данных требуется использовать переменные. После вывода информации 
# программа должна дожидаться пока пользователь нажмет Enter для выхода.

# Golubev A. S.
# 31.03.2016

print("Борис Николаевич Бугаев более известен, как русский писатель Андрей Белый.")

year_of_birth = 1880
year_of_death = 1934 
age_of_death = year_of_death - year_of_birth
birthplace = "Москва, Российская империя"
interess = "писатель, поэт, критик, мемуарист, стиховед"

print("Место рождения:", birthplace)
print("Год рождения:", year_of_birth)
print("Возраст при смерти: ", age_of_death)
print("Область интересов: ", interess)

input("\n\nНажмите Enter для выхода.")
