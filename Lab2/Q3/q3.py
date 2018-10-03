import os
from graphviz import Digraph
os.environ["PATH"] += os.pathsep + r'C:/Program Files (x86)/release/bin'

class DFA:
    ''' Classe para representar um automato finito determinístico. '''
    def __init__(self, states, alphabet, delta, start, accepts):
        """Construtor recebe uma lista com estados iniciais, lista com alfabeto,
            lista de tuplas com os arcos, e também as listas relacionadas a estados iniciais e finais"""
        self.states = states
        self.start = start
        self.delta = delta
        self.accepts = accepts
        self.alphabet = alphabet
        self.current_state = start

    def complemento(self):
        auxiliary = []
        for element in self.states:
            if (element not in self.accepts) and (element not in self.start):
                auxiliary.append(element)
        self.accepts = auxiliary

def union(AFD_one, AFD_two):
    ''' Função que realiza a união entre dois AFDs'''
    initial = AFD_one.start + AFD_two.start
    alpha = AFD_one.alphabet
    states = []
    grafo = []
    for element_one in AFD_one.states:
        for element_two in AFD_two.states:
            states.append(element_one+element_two)
            for arco_one in AFD_one.delta:
                for arco_two in AFD_two.delta:
                    if arco_one[0] == element_one and arco_two[0] == element_two and arco_one[1] == arco_two[1]:
                        grafo.append((arco_one[0]+arco_two[0], arco_one[1], arco_one[2]+arco_two[2]))
    finals = []
    for element_one in AFD_one.accepts:
        for element_two in AFD_two.accepts:
            finals.append(element_one+element_two)
    return DFA(states, alpha, grafo, initial, finals)

def interseccao(AFD_one, AFD_two):
    ''' Função que realiza a intersecção entre dois AFDs a partir da lei de Morgan '''
    AFD_one.complemento()
    AFD_two.complemento()
    AFD_union = union(AFD_one, AFD_two)
    AFD_union.complemento()
    AFD_one.complemento()
    AFD_two.complemento()
    return AFD_union

if __name__ == "__main__":
    ''' Main a partir da qual se pode interagir com as funções acima implementadas. Atentar ao fato de que as entradas
    das funções devem ser auômatos finitos determinísticos'''
    AFD_one = DFA(['q0', 'q1', 'q2'], ['a'], [('q0', 'a', 'q1'), ('q1', 'a', 'q2'), ('q2', 'a', 'q3')], 'q0', ['q2'])
    AFD_two = DFA(['p0', 'p1', 'p2', 'p3'], ['a'], [('p0', 'a', 'p1'), ('p1', 'a', 'p2'), ('p2', 'a', 'p3'), ('p3', 'a', 'p1')], 'p0',
                  ['p3'])
    result = interseccao(AFD_one, AFD_two)
    print(result.delta)

    drawGraph = Digraph('Automatum', filename='automataCERTO2', format='pdf')
    drawGraph.attr(rankdir='LR', size='8,5')
    drawGraph.attr('node', shape='doublecircle')
    for stage in result.accepts:
        drawGraph.node(stage)
    drawGraph.attr('node', shape='circle')
    for element in result.delta:
        init = str(element[0])
        final = str(element[2])
        label = ""
        for symbol in element[1]:
            label += (symbol)
        drawGraph.edge(init, final, label=label)
    drawGraph.view()




