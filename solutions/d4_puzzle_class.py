import re
from math import sqrt

class Puzzle4:

    def __init__(self, matrix:list[list[str]]):
        self.matrix = matrix
        self.n = len(matrix)

    def count(self, word:str):
        return sum([len(re.compile(word).findall("".join(line))) for line in self.matrix])

    def rotate_90(self):
        new_matrix = [[" " for _ in range(self.n)] for _ in range(self.n)]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                new_matrix[j][self.n-i-1] = self.matrix[i][j]
        self.matrix = new_matrix

    def rotate_45(self):

        # new_dim = int(self.n * sqrt(2))+1
        new_dim = 2 * self.n
        new_matrix = [['' for _ in range(new_dim)] for _ in range(new_dim)]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                new_matrix[i+j][new_dim//2-i+j] = self.matrix[i][j]
        self.matrix = new_matrix
        self.n = new_dim

    def count_X_mas(self):
        total = 0
        for i in range(1,self.n-1):
            for j in range(1,self.n-1):
                if self.matrix[i][j] == 'A':
                    if ((self.matrix[i-1][j-1] == 'M' and self.matrix[i+1][j+1] == 'S') or (self.matrix[i-1][j-1] == 'S' and self.matrix[i+1][j+1] == 'M')):
                        if ((self.matrix[i+1][j-1] == 'M' and self.matrix[i-1][j+1] == 'S') or (self.matrix[i+1][j-1] == 'S' and self.matrix[i-1][j+1] == 'M')):
                            total +=1
        return total
        