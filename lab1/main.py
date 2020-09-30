from lab1 import f
from lab1.classes import chromosome as c
from lab1.classes import population as p
import random as r
import lab1.functions as func


"""Размерность популяции"""
n = 8
"""Количество генов"""
k = 4
"""Диапазон значений для генов"""
r = 30

pop = p.population(k, f.s_fitness, n, r).setStart()

for i in range(0, 10):
    print("start ",i," cicle")
    pop.parents_population().crossover().mutation()
    print("end ", i, " cicle")
    pop.print()

k, n = pop.search_best()
print(n)





"""В конструктор популяции передаётся функция являющаяся функцией приспособленности, 
в которую передается массив с генами
"""

#TODO реализовать условие выхода


