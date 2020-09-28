import random as r
import f as f


class chromosome:
    def __init__(self, ngene, range_genes, fitness):
        self.genes = []
        self.n = ngene
        self.range = range_genes
        self.fitness = -1
        self.function_fitness = fitness

        for i in range(0, self.n):
            self.genes.append(0)

    def set(self, arr):
        self.genes.clear()
        for i in range(0, self.n):
            self.genes.append(arr[i])
        self.fitness = self.function_fitness(self.genes)
        return self

    def set_rand(self):
        i = 0
        mrange = -1 * self.range
        for i in range(0, self.n):
            self.genes[i] = r.randint(mrange, self.range)
        self.fitness = f.s_fitness(self.genes)
        return self

    def print(self):
        print(self.genes)

    def __eq__(self, other):
        k = 0
        for i in range(0, len(self.genes)):
            if self.genes[i] != other.genes[i]:
                k += 1
        if k == 0:
            return True
        else:
            return False
