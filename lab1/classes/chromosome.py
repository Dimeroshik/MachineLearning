import random as r
from lab1 import f as f


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

    def mutation_gene(self, delta = 10):
        """Проверка на вероятность мутации р=0.3 если меньше 4 то мутации не будет"""
        a = 1
        if r.randint(1, 10) < 4:
            return
        """Изменение коэффициента перед числом из интервалаа"""
        if r.randint(0, 1) == 1:
            a = -1
        """Наша дельта"""
        k = r.randint(1, delta)
        """Номер изменяемого гена"""
        n = r.randint(0, self.n - 1)
        self.genes[n] += a * k

    def get_fitness(self):
        res = self.function_fitness(self.genes)
        self.fitness = res
        return res

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
