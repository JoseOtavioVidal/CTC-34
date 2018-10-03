from graphviz import Digraph
import os
os.environ["PATH"] += os.pathsep + r'C:\Program Files\graphviz-2.38\release\bin'

class DFA:
    def __init__(self, states, alphabet, delta, start, accepts):
        """Construtor recebe uma lista com estados iniciais, lista com alfabeto,
            lista de tuplas com os arcos, e também as listas relacionadas a estados iniciais e finais"""
        self.states = states
        self.start = start
        self.delta = delta
        self.accepts = accepts
        self.alphabet = alphabet
        self.current_state = start

    def minimize(self):
        def DIST(i, j):
            D[(i, j)] = 1
            for element in S[(i, j)]:
                DIST(element[0], element[1])

        n = len(self.states)

        D = []
        S = []
        for i in range(n):
            for j in range(i+1, n):
                D[(i, j)] = 0
                S[(i, j)] = []

        for i in range(n):
            for j in range(i+1, n):
                if self.states(i) in self.accepts:
                    if self.states(j) not in self.accepts:
                        D[(i, j)] = 1
                elif self.states(j) in self.accepts:
                    D[(i, j)] = 1

        for i in range(n):
            for j in range(i+1, n):
                if D[(i, j)] == 0:
                    for element in self.alphabet:
                        x = -1
                        y = -1
                        for arco in self.delta:
                            if arco[0] == self.states(i) and arco[1] == element:
                                x = self.states.index(arco[2])
                            elif arco[0] == self.states(j) and arco[1] == element:
                                y = self.states.index(arco[2])
                        if x != -1 and x != y and (D[(x, y)] == 1 or D[(y, x)] == 1):
                            DIST(i, j)
                        elif x < y and (i, j) != (x, y):
                            S[(x, y)].append((i, j))
                        elif y > x and (i, j) != (x, y):
                            S[(y, x)].append((i, j))



