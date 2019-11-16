'''

20191110 Sikorskiy Yuriy V.
cs.yury.v@pm.me

coursera.org
Введение в машинное обучение, Неделя 1, Предобработка данных в Pandas


'''
import numpy as np
import pandas
from pandas import Series, DataFrame
pandas.set_option('display.notebook_repr_html', False)
pandas.set_option('display.max_columns', 8)
pandas.set_option('display.max_rows', 10)
pandas.set_option('display.width', 80)

import matplotlib.pyplot as plt
# %matplotlib inline

# Открываю csv файл с данными о пассажирах титаника
passengers_with_titanic = pandas.read_csv('titanic.csv', index_col='PassengerId')

total_passengers = len(passengers_with_titanic)
print(f'Всего пассажиров: {total_passengers}')

# Вопрос 1
# Какое количество мужчин и женщин ехало на корабле?
# В качестве ответа приведите два числа через пробел.
print('Вопрос 1')

# По колонке 'Sex' статиска: количетво мужчин ('male') и женщин ('female')

male_and_female = passengers_with_titanic['Sex'].value_counts()

value_sex = male_and_female.keys()

# value_sex[0] == 'male'
# value_sex[1] == 'female'
# сохраняю результат в текстовый вайл

with open('1.txt', 'w', encoding='utf-8') as fileOut:
    fileOut.writelines(f'{str(male_and_female[value_sex[0]])} {str(male_and_female[value_sex[1]])}')

# --------------------------------------------------------------------------
# Вопрос 2
# Какой части пассажиров удалось выжить?
# Посчитайте долю выживших пассажиров.
# Ответ приведите в процентах (число в интервале от 0 до 100, знак процента не нужен),
# округлив до двух знаков.
print('\nВопрос 2.\n')

# # По колонке 'Survived' статиска: количетво погибших ('0') и выживших ('1')
how_many_survivors_and_deceased = passengers_with_titanic['Survived'].value_counts()
value_Survived = how_many_survivors_and_deceased.keys()

# value_Survived[0] == 0
# value_Survived[1] == 1

print(f'Погибло: {how_many_survivors_and_deceased[value_Survived[0]]}')
print(f'Выжило: {how_many_survivors_and_deceased[value_Survived[1]]}')

percentage_of_survivors = (how_many_survivors_and_deceased[value_Survived[1]] / total_passengers) * 100

print(f'Процент выживших: {percentage_of_survivors:.2f}')

with open('2.txt', 'w', encoding='utf-8') as fileOut:
    fileOut.writelines(f'{percentage_of_survivors:.2f}')

# --------------------------------------------------------------------------
# Вопрос 3
# Какую долю пассажиры первого класса составляли среди всех пассажиров?
# Ответ приведите в процентах (число в интервале от 0 до 100, знак процента не нужен),
# округлив до двух знаков.
print('\nВопрос 3\n')

number_pss_in_each_class = passengers_with_titanic['Pclass'].value_counts()
number_of_pss_in_first_class = number_pss_in_each_class[1]

print(f'Пассажиров в первом классе: {number_of_pss_in_first_class}')
print(f'Пассажиров во втором классе: {number_pss_in_each_class[2]}')
print(f'Пассажиров в третьем классе: {number_pss_in_each_class[3]}')

percentage_of_first_class_passengers = number_of_pss_in_first_class / total_passengers * 100
print(f'Процент пассажжиров первого класса: {percentage_of_first_class_passengers:.2f}')

with open('3.txt', 'w', encoding='utf-8') as fileOut:
    fileOut.writelines(f'{percentage_of_first_class_passengers:.2f}')

# --------------------------------------------------------------------------
# Вопрос 4
# Какого возраста были пассажиры? Посчитайте среднее и медиану возраста пассажиров.
# В качестве ответа приведите два числа через пробел.
print('\nВопрос 4\n')

passengers_age = passengers_with_titanic['Age']
average_age_of_passengers = passengers_age.mean(axis=0)
median_age_of_passengers = passengers_age.median(axis=0)

print(f'Среднее значение возраста пассажиров: {average_age_of_passengers:.2f}')
print(f'Медиана возрасаита пассажиров: {median_age_of_passengers:.2f}')

with open('4.txt', 'w', encoding='utf-8') as fileOut:
    fileOut.writelines(f'{average_age_of_passengers:.2f} {median_age_of_passengers}')

# --------------------------------------------------------------------------
# Вопрос 5
# Коррелируют ли число братьев/сестер/супругов с числом родителей/детей?
# Посчитайте корреляцию Пирсона между признаками SibSp и Parch.
print('\nВопрос 5\n')
corr_SibSp_Parch = passengers_with_titanic.SibSp.corr(passengers_with_titanic.Parch)

with open('5.txt', 'w', encoding='utf-8') as fileOut:
    fileOut.writelines(f'{corr_SibSp_Parch:.2f}')


# --------------------------------------------------------------------------
# Вопрос 6
# Какое самое популярное женское имя на корабле?
# Извлеките из полного имени пассажира (колонка Name) его личное имя (First Name).
# Это задание — типичный пример того, с чем сталкивается специалист по анализу данных.
# Данные очень разнородные и шумные, но из них требуется извлечь необходимую информацию.
# Попробуйте вручную разобрать несколько значений столбца Name и выработать правило для извлечения имен,
# а также разделения их на женские и мужские.
print('\nВопрос 6\n')


name_and_sex = passengers_with_titanic[['Name', 'Sex']]
print(type(name_and_sex))

name_female = name_and_sex[name_and_sex.Sex == 'female']['Name']
names = []

for i in list(name_female):
    temp = i.split(', ')
    temp1 = temp[1].split('. ')[1]
    temp2 = temp1
    if '(' in temp2:
        temp2 = temp2.split('(')[1][:-1]
        temp2 = temp2.split()[:-1]
    else:
        temp2 = temp2.split()
    names.extend(temp2)
    names2 = []
    for i in names:
        if i[0] == '\"':
            i = i[1:]
        if i[-1] == '\"':
            i = i[:-1]
        if i == 'Mrs':
            continue
        if len(i) > 1:
            names2.append(i)
    names = names2
    names.sort()


series_names_female = pandas.Series(names)

print(series_names_female.value_counts().index[0], series_names_female.value_counts().values[0],len(series_names_female.value_counts()))

with open('6.txt', 'w', encoding='utf-8') as fileOut:
    fileOut.writelines(f'{series_names_female.value_counts().index[0]}')


with open('6_1.txt', 'w', encoding='utf-8') as fileOut:
    for i in names:
        if '(' in i:
            i = i.split('(')[1]
        i = i.split()[0]
        fileOut.writelines(f'{i}\n')


print('\n->')
