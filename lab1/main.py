import f
from classes import chromosome as c
from classes import population as p
import random as r
import functions as func


"""Размерность популяции"""
n = 4
"""Количество генов"""
k = 4
"""Диапазон значений для генов"""
r = 30

pop = p.population(k, f.s_fitness, n, r).setStart()
pop.parents_population().crossover()

