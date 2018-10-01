from graphviz import Digraph
import os
os.environ["PATH"] += os.pathsep + r'C:\Program Files\graphviz-2.38\release\bin'


def DFAg(NFAgraph, NFAinitialStages, alphabet):
    DFAgraph = []
    possibleStages = []
    deathStage = 'q'
    newStages = []
    for element in NFAinitialStages:
        newStages.append(element)
        possibleStages.append(element)
    while(len(newStages)> 0):
        #print(newStages)
        primaryStagesFin = []

        # Estado a ser computado
        stages = newStages[0]
        # Dividi o estado novo nos estados conhecidos do NFA
        primaryStagesInit = stages.split(',')
        for symbol in alphabet:
            #print(symbol)
            primaryStagesFin = []
            stageFinal = ''
            #print(primaryStagesInit)
            for stage in primaryStagesInit:
                #print(stage)
                for element in NFAgraph:
                    if element[0] == stage:
                        if symbol == element[1]:
                            if primaryStagesFin.count(element[2]) == 0:
                                primaryStagesFin.append(element[2])
                        else:
                            primaryStagesFin.append(deathStage)

            #print(primaryStagesFin)

            # Constroi o estado final daquela transição
            if primaryStagesFin.count(deathStage) == len(primaryStagesFin):
                stageFinal = deathStage
            else:
                while primaryStagesFin.count(deathStage)>0:
                    primaryStagesFin.remove(deathStage)
                for element in primaryStagesFin:
                    if element == primaryStagesFin[0]:
                        stageFinal = stageFinal + element
                    else:
                        stageFinal = stageFinal + ',' +element
            #print(stageFinal)

            graphElement = (stages, symbol, stageFinal)
            #print(graphElement)
            if stageFinal not in possibleStages:
                #print(stageFinal)
                possibleStages.append(stageFinal)
                newStages.append(stageFinal)
            DFAgraph.append(graphElement)
        newStages.pop(0)
        #print(possibleStages)
    return DFAgraph




def DFAf(DFAgraph, NFAfinalStages):
    DFAfinalStages = []
    for element in DFAgraph:
        primaryFinalStages = element[2].split(',')
        for stage in NFAfinalStages:
            if stage in primaryFinalStages and DFAfinalStages.count(element[2]) == 0:
                DFAfinalStages.append(element[2])
        primaryInitialStages = element[0].split(',')
        for stage in NFAfinalStages:
            if stage in primaryInitialStages and DFAfinalStages.count(element[0]) == 0:
                DFAfinalStages.append(element[0])
    return DFAfinalStages


if __name__ == "__main__":
    NFAinitialStages = ['q0']
    NFAfinalStages = ['q1', 'q2', 'q0']#, 'q2', 'q3', 'q5']

    NFAgraph = [('q0', 'a', 'q3'), ('q3', 'b', 'q1'), ('q3', 'c', 'q1'), ('q3', 'b', 'q2'), ('q3', 'c', 'q2'), ('q2', 'a', 'q3')]

        #         Automato 4
        #        [('q3', 'a', 'q3'), ('q5', 'b', 'q5'), ('q6', 'c', 'q6'), ('q0', 'a', 'q3'), ('q0', 'b', 'q5'),
        #        ('q0', 'c', 'q6'), ('q2', 'b', 'q5'), ('q2', 'c', 'q6'), ('q3', 'a', 'q2'), ('q3', 'a', 'q5'),
        #        ('q3', 'a', 'q4'), ('q3', 'a', 'q6'), ('q3', 'a', 'q1'), ('q3', 'b', 'q5'), ('q3', 'c', 'q6'), ('q4', 'c', 'q6'), ('q5', 'b', 'q4'), ('q5', 'b', 'q6'), ('q5', 'b', 'q1'), ('q5', 'c', 'q6'), ('q6', 'c', 'q1')]

        #        Automato 1
        #        [('q2', 'b', 'q3'), ('q3', 'b', 'q4'), ('q5', 'a', 'q5'), ('q6', 'a', 'q6'), ('q5', 'b', 'q5'), ('q6', 'b', 'q6'),
        #        ('q0', 'b', 'q3'), ('q0', 'a', 'q5'), ('q0', 'b', 'q5'), ('q3', 'b', 'q6'), ('q3', 'b', 'q1'), ('q4', 'a', 'q6'),
        #        ('q4', 'b', 'q6'), ('q5', 'b', 'q3'), ('q5', 'a', 'q2'), ('q5', 'b', 'q2'), ('q6', 'a', 'q1'), ('q6', 'b', 'q1')]

        #           Automato 2
         #          [('q0', 'a', 'q3'), ('q3', 'b', 'q1'), ('q3', 'c', 'q1'), ('q3', 'b', 'q2'), ('q3', 'c', 'q2'), ('q2', 'a', 'q3')]

        #           Automato 3
        #           [('q0', 'a','q4'),('q4', 'a','q4'), ('q4', 'a','q2'), ('q2', 'b','q1'), ('q4', 'b','q1'), ('q0', 'a','q1')
        #           ,('q0', 'b','q1'),('q0', 'b','q5'),('q5', 'b','q5'),('q5', 'b','q3'),('q3', 'a','q1'),('q5', 'q','q1')]
    DFAinitialStages = []
    DFAfinalStages = []
    DFAgraph = []
    alphabet = ['a', 'b', 'c']
    DFAgraph = DFAg(NFAgraph, NFAinitialStages, alphabet)
    print(DFAgraph)
    DFAinitialStages = NFAinitialStages
    DFAfinalStages = DFAf(DFAgraph, NFAfinalStages)
    print(DFAfinalStages)

    drawGraph = Digraph('Automatum', filename='automata2', format='pdf')
    drawGraph.attr(rankdir='LR', size='8,5')
    drawGraph.attr('node', shape='doublecircle')
    for stage in DFAfinalStages:
        drawGraph.node(stage)
    drawGraph.attr('node', shape='circle')
    for element in DFAgraph:
        init = str(element[0])
        final = str(element[2])
        label = ""
        for symbol in element[1]:
            label += (symbol)
        drawGraph.edge(init, final, label=label)
    drawGraph.view()
