def transition(states, symbol, graph):
    deathState = 10
    lenght = len(states)
    for i in range(lenght):
        if states[i] == deathState:
            states.append(deathState)
        else:
            for element in graph:
                if element[0] == states[i]:
                    if element[1].count(symbol) > 0:
                        states.append(element[2])
                    else:
                        states.append(deathState)

    for i in range(lenght):
        states.pop(0)
    #print(states)




def AFN(graph, initialStage, finalStages, word):
    possibleStates = []
    possibleStates.append(initialStage)
    acceptableWord = []

    if initialStage in finalStages:
        print(acceptableWord)
    #print(word)
    for symbol in word:
        transition(possibleStates, symbol, graph)
        acceptableWord.append(symbol)
        for state in possibleStates:
            if state in finalStages:
                print(acceptableWord)
                break

if __name__ == "__main__":
    a = 'a'
    b = 'b'
    c= 'c'
    word1 = [b, a, a, b, b, a]
    word2 = [a, b, a, c, a, b, c]
    finalStages = [0, 1, 2]
    initialStage = 0
    graph = [(0, ['a'], 3), (3, ['b'], 2), (3, ['c'], 2), (2, ['a'], 3), (3, ['b'], 1), (3, ['c'], 1)]
    for i in range(len(word1)):
        AFN(graph, initialStage, finalStages, word1[i:])
    for i in range(len(word2)):
        AFN(graph, initialStage, finalStages, word2[i:])