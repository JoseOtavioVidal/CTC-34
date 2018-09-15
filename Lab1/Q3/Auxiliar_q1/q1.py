from graphviz import Digraph
import os
os.environ["PATH"] += os.pathsep + r'C:\Program Files\graphviz-2.38\release\bin'

def thereIsUnion(elementGraph, graph):
    initParen = 0
    finalParen = 0
    expression = []
    expression = elementGraph[1]
    for index in range(len(expression)):
        if expression[index] == '(':
            initParen = initParen+1
        if expression[index] == ')':
            finalParen = finalParen + 1
        if expression[index] == '+' and initParen == finalParen:
            elementGraph1 = (elementGraph[0], elementGraph[1][:index], elementGraph[2])
            elementGraph2 = (elementGraph[0], elementGraph[1][index + 1:], elementGraph[2])
            graph.append(elementGraph1)
            graph.append(elementGraph2)
            graph.remove(elementGraph)
            return True
    return False


def thereIsCon(elementGraph, graph, stage):
    initParen = 0
    finaParen = 0
    expression = elementGraph[1]
    elementExpression = expression[0]
    if elementExpression == '(':
        for index in range(len(expression)):
            if expression[index] == '(':
                initParen = initParen+1
            if expression[index] == ')':
                finaParen = finaParen + 1
                if finaParen == initParen:
                    if index != len(expression)-1:
                        if expression[index+1] == '*':
                           index = index+1
                        if index != len(expression)-1:
                            elementGraph1 = (elementGraph[0], elementGraph[1][:index+1], stage+1)
                            elementGraph2 = (stage+1, elementGraph[1][index + 1:], elementGraph[2])
                            graph.append(elementGraph1)
                            graph.append(elementGraph2)
                            graph.remove(elementGraph)
                            return stage+1
                    return stage
    else:
        if expression[1] == '*':
            if len(expression)> 2:
                elementGraph1 = (elementGraph[0], elementGraph[1][:2], stage + 1)
                elementGraph2 = (stage + 1, elementGraph[1][2:], elementGraph[2])
                graph.append(elementGraph1)
                graph.append(elementGraph2)
                graph.remove(elementGraph)
                return stage+1
        else:
            elementGraph1 = (elementGraph[0], elementGraph[1][:1], stage + 1)
            elementGraph2 = (stage + 1, elementGraph[1][1:], elementGraph[2])
            graph.append(elementGraph1)
            graph.append(elementGraph2)
            graph.remove(elementGraph)
            return stage + 1

    return stage


def thereIsKleene(elementGraph, graph, stage):
    expression = elementGraph[1]
    initParen = 0
    finalParen = 0
    for index in range(len(expression)):
        if expression[index] == '*':
            if expression[index-1] != ')':
                elementGraph1 = (elementGraph[0], ['&'], stage + 1)
                graph.append(elementGraph1)
                elementGraph1 = (stage + 1, elementGraph[1][index - 1:index], stage + 1)
                graph.append(elementGraph1)
                elementGraph1 = (stage + 1, ['&'], elementGraph[2])
                graph.append(elementGraph1)
                graph.remove(elementGraph)
                return stage+1
            else:
                finalParen = finalParen+1
                for aux in range(index-2, -1, -1):
                    if expression[aux] == '(':
                        initParen = initParen+1
                    if expression[aux] == ')':
                        finalParen = finalParen + 1
                    if initParen == finalParen:
                        newStage = stage + 1
                        elementGraph1 = (elementGraph[0], ['&'], newStage)
                        graph.append(elementGraph1)
                        elementGraph1 = (newStage, elementGraph[1][aux:index], newStage)
                        graph.append(elementGraph1)
                        elementGraph1 = (newStage, ['&'], elementGraph[2])
                        graph.append(elementGraph1)
                        graph.remove(elementGraph)
                        return stage + 1
    return stage


def thereIsParentheses(elementGraph, graph):
    expression = elementGraph[1]
    lenght = len(expression)
    if expression[0] == '(' and expression[lenght-1] == ')':
        elementGraph1 = (elementGraph[0], elementGraph[1][1:lenght-1],elementGraph[2])
        graph.append(elementGraph1)
        graph.remove(elementGraph)
        return True
    return False




def algorithm(regularExpression):
    #Cria o automato inicial
    graph = []
    initialStage = 0
    finalStage = 1
    elementGraph = (initialStage, regularExpression, finalStage)
    graph.append(elementGraph)
    graphNotOk = True
    stage = finalStage
    #Realiza os passos do Algoritmo
    while graphNotOk:
        for elementGraph in graph:
            if len(elementGraph[1]) > 1:

                if not thereIsUnion(elementGraph, graph):

                    #Há concatenação
                    stageAux = thereIsCon(elementGraph, graph, stage)

                    if stageAux == stage:
                        #Há fecho de Kleene
                        stageAux = thereIsKleene(elementGraph, graph, stage)
                        if stageAux == stage:
                            #Há parênteses
                            if not thereIsParentheses(elementGraph, graph):
                                graphNotOk = False
                            else:
                                graphNotOk = True
                                break
                        else:
                            graphNotOk = True
                            stage= stageAux
                            break
                    else:
                        graphNotOk = True
                        stage = stageAux
                        break
                else:
                    graphNotOk = True
                    break
            else:
                graphNotOk = False
    return graph

if __name__ == "__main__":
    word = "(a+b)*bb(b+a)*"
    regularExpression = []
    for symbol in word:
        regularExpression.append(symbol)
    graph = algorithm(regularExpression)
    print(graph)

    drawGraph = Digraph('Automatum', filename = 'automata4',format = 'jpg')
    drawGraph.attr(rankdir = 'LR', size = '8,5')
    drawGraph.attr('node', shape = 'doublecircle')
    drawGraph.node('1')
    drawGraph.attr('node', shape = 'circle')
    for element in graph:
        init = str(element[0])
        final = str(element[2])
        label = ""
        for symbol in element[1]:
            label += (symbol)
        drawGraph.edge(init, final, label = label)
    drawGraph.view()



