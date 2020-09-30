from lab1.classes import population as p
import random as r


"""Функцией change_parent выбираются 2 родителя, затем идет проверка на копию пары
    если копий нет, то выбирается следующая пара
    Возвращает массив с хромосомами?"""


"""Выбор колеса рулетки"""
def change_parent(population, sum):
    p = r.uniform(0, sum-1)
    k = 0
    i = -1
    while k <= p:
        k += population.chromosomes[i].fitness
        i+=1
    return population.chromosomes[i]

"""Проверка на наличие пары в массиве"""
def check_clone_pair(par_pop, a, b):
    i = 0
    while i < (len(par_pop)):
        if (par_pop[i]== a and par_pop[i+1] == b or par_pop[i]== b and par_pop[i+1] == a ):
            return 0
        i+=2
    return 1

"""Свап генов двух родителей"""
def swap_genes(par1, par2, divider):
    res1 = par1.genes[0:divider] + par2.genes[divider:len(par2.genes)]
    res2 = par2.genes[0:divider] + par1.genes[divider:len(par1.genes)]
    par2.genes = res1
    par2.genes = res2
    return par1,par2

""""Рандомный тест"""
def random_from_me():
    k = r.randint(0,2)
    return k

