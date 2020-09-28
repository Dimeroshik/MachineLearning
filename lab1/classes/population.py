
from classes import chromosome as c
import functions as f
import random as rand


class population:
    def __init__(self,  ngene, fitness, count = 0, range = 30, ):
        self.chromosomes = []
        self.count = count
        self.ngene = ngene
        self.range = range
        self.fitness = fitness

    def setStart(self):
        self.chromosomes.clear()
        for i in range(0, self.count):
            e = c.chromosome(self.ngene, self.range, self.fitness).set_rand()
            self.chromosomes.append(e)
        return self

    def parents_population(self):
        par_pop = []

        sum = 0
        for i in range(0, self.count):
            sum += self.chromosomes[i].fitness

        i = 0
        while i < self.count:
            a = f.change_parent(self, sum)
            b = f.change_parent(self, sum)
            if (a != b):
                k = f.check_clone_pair(par_pop, a, b)
                if (k == 1):
                    par_pop.append(a)
                    par_pop.append(b)
                    i += 2

        self.chromosomes = par_pop
        self.count = len(par_pop)
        return self

    def set_with_arr(self, genes):
        self.chromosomes = genes

    def crossover(self):
        i = 0
        while i < self.count:
            r = rand.randint(0, self.ngene)
            self.chromosomes[i], self.chromosomes[i+1] = \
                f.swap_genes(self.chromosomes[i], self.chromosomes[i+1], r)
            i += 2

    def print(self):
        for i in range(0, self.count):
            self.chromosomes[i].print()
