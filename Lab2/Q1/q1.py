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
    return DFAfinalStages


if __name__ == "__main__":
    NFAinitialStages = ['q0']
    NFAfinalStages = ['q2', 'q4']
    NFAgraph = [('q0', '0','q0'),('q0', '1','q0'), ('q0', '0','q1'), ('q1', '0','q2'), ('q0', '1','q3'), ('q3', '1','q4')]
    DFAinitialStages = []
    DFAfinalStages = []
    DFAgraph = []
    alphabet = ['1', '0']
    DFAgraph = DFAg(NFAgraph, NFAinitialStages, alphabet)
    print(DFAgraph)
    DFAinitialStages = NFAinitialStages
    DFAfinalStages = DFAf(DFAgraph, NFAfinalStages)
    print(DFAfinalStages)

    drawGraph = Digraph('Automatum', filename='automata', format='pdf')
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
