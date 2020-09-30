
from lab1.classes import chromosome as c
import lab1.functions as f
import random as rand


class population:
    def __init__(self,  ngene, fitness, count = 0, range = 30, delta_gene_mutation = 10):
        self.chromosomes = []
        self.count = count
        self.ngene = ngene
        self.range = range
        self.fitness = fitness
        self.delta_gene_mutation = delta_gene_mutation

    def setStart(self):
        self.chromosomes.clear()
        for i in range(0, self.count):
            e = c.chromosome(self.ngene, self.range, self.fitness).set_rand()
            self.chromosomes.append(e)
        return self

    def parents_population(self):
        print("start create_population")
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
        print('1')
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
        print('2')
        return self

    def mutation(self):
        for i in range(0, self.ngene - 1):
            self.chromosomes[i].mutation_gene(self.delta_gene_mutation)
        print('3')
        return self

    def search_best(self):
        current_max_fitness = self.chromosomes[0].get_fitness()
        ik = 0
        for i in range(1, self.count - 1):
            temp_fitness = self.chromosomes[i].get_fitness()
            if  temp_fitness < current_max_fitness:
                ik = i
                current_max_fitness = temp_fitness
        return i, current_max_fitness

    def get_fitness_with_index(self, i = 0):
        res = self.chromosomes[i].fitness
        return res

    def print(self):
        for i in range(0, self.count):
            self.chromosomes[i].print()
