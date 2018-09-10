from graphviz import Digraph
import os
os.environ["PATH"] += os.pathsep + r'C:/Program Files (x86)/release/bin'

# Método recursivo utilizado para definição de e-CLOSURE de cada estado
def recursao_CLOSURE(state, list_aux):
    list_aux.append(state)
    for i in range(len(grafo)):
        if grafo[i][0] == state and grafo[i][1] == '&' and (not grafo[i][2] in list_aux):
            recursao_CLOSURE(grafo[i][2], list_aux)

# Método principal para eliminação de todas as e-transições em um grafo
def grafo_q2(grafo, states, final_states):

    # I – computar o -fecho de cada estado
    list_CLOSUREs = []
    for state in states:  # Para cada um dos estados
        list_aux = []
        recursao_CLOSURE(state, list_aux)  # Incluir o estado em seu próprio e-CLOSURE
        list_CLOSUREs.append(list_aux)  # Acrescentar o e-CLOSURE do estado à lista dos e-CLOSUREs

    # II – cada arco de A em X gera um arco de A em Y para cada Y no -fecho(X)
    # III – cada arco de Y em A para qualquer Y no -fecho(X) gera um arco de X para A
    contador = 0
    n = len(grafo)
    for state in states:  # para cada um dos estados
        for i in range(n):  # para cada um dos arcos do grafo
            if (grafo[i][2] == state) and (grafo[i][1] != '&'):  # se o arco é direcionado ao estado em análise (II)
                for j in range(len(list_CLOSUREs[contador])):
                    if list_CLOSUREs[contador][j] != state:
                        grafo.append((grafo[i][0], grafo[i][1], list_CLOSUREs[contador][j]))
            if (grafo[i][0] in list_CLOSUREs[contador]) and (grafo[i][1] != '&') and (grafo[i][0] != state):  # se o arco tem origem do e-CLOSURE do estado em análise (III)
                grafo.append((state, grafo[i][1], grafo[i][2]))
        # IV – X é estado final se algum Y no -fecho(X) for final
        for j in range(len(list_CLOSUREs[contador])):
            if (list_CLOSUREs[contador][j] in final_states) and (not state in final_states):
                final_states.append(state)
        contador = contador + 1

    # Eliminação das e-transições iniciais
    k = 0
    while k < n:
        if grafo[k][1] == '&':
            grafo.remove(grafo[k])
            n = n-1
        else:
            k = k+1

if __name__ == "__main__":

    alfabeto = ['a', 'b', 'c']
    states = ['0', '1', '2', '3', '4', '5']#, '6']
    #grafo = [('0', '&', '5'), ('5', '&', '2'), ('2', 'b', '3'), ('3', 'b', '4'), ('4', '&', '6'), ('6', '&', '1'),
     #       ('5', 'a', '5'), ('6', 'a', '6'), ('5', 'b', '5'), ('6', 'b', '6')]
    #grafo = [('0', '&', '2'), ('2', '&', '1'), ('2', 'a', '3'), ('3', 'b', '2'), ('3', 'c', '2')]
    #grafo = [('0','&','4'), ('0','&','5'), ('4','&','2'), ('5','&','3'), ('2','b','1'), ('3','a','1'), ('4','a','4'),
     #       ('5', 'b', '5')]
    grafo = [('0','&','4'), ('4','&','2'), ('2','&','5'), ('5','&','3'), ('3','&','6'), ('6','&','1'), ('4','a','4'),
            ('5', 'b', '5')]
    final_states = ['1']

    grafo_q2(grafo, states, final_states)

    drawGraph = Digraph('Automatum', filename='automataq02d', format='jpg')
    drawGraph.attr(rankdir='LR', size='8,5')
    drawGraph.attr('node', shape='doublecircle')
    for x in final_states:
        drawGraph.node(x)
    drawGraph.attr('node', shape='circle')
    for element in grafo:
        init = str(element[0])
        final = str(element[2])
        label = ""
        for symbol in element[1]:
            label += (symbol)
        drawGraph.edge(init, final, label=label)
    drawGraph.view()
