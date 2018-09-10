def transition(states, symbol):
    lenght = len(states)
    for i in range(lenght):
        if states[i] == "q0":
            if symbol == 'a':
                states.append("q3")
            elif symbol == 'b':
                states.append("q5")
            else:
                states.append("q6")

        elif states[i] == "q2":
            if symbol == 'a':
                states.append("q7")
            elif symbol == 'b':
                states.append("q5")
            else:
                states.append("q6")

        elif states[i] == "q3":
            if symbol == 'a':
                states.append("q3")
                states.append("q2")
                states.append("q4")
                states.append("q6")
                states.append("q5")
                states.append("q1")
            elif symbol == 'b':
                states.append("q5")
            else:
                states.append("q6")

        elif states[i] == "q4":
            if symbol == 'c':
                states.append("q6")
            else:
                states.append("q7")

        elif states[i] == "q5":
            if symbol == 'a':
                states.append("q7")
            elif symbol == 'b':
                states.append("q5")
                states.append("q1")
                states.append("q4")
                states.append("q6")
            else:
                states.append("q6")

        elif states[i] == "q6":
            if symbol == 'c':
                states.append("q6")
                states.append("q1")
            else:
                states.append("q7")

        else:
            states.append("q7")

    for i in range(lenght):
        states.pop(0)

def AFN(states, word):
    possibleStates = []
    possibleStates.append(states[0])
    acceptableWord = []
    for symbol in word:
        if possibleStates.count("q0") > 0:
            print(acceptableWord)
        transition(possibleStates, symbol)
        acceptableWord.append(symbol)
        if len(possibleStates) - possibleStates.count("q7") > 0:
            print(acceptableWord)

if __name__ == "__main__":
    a = 'a'
    b = 'b'
    c = 'c'
    word1 = [b, a, a, b, b, a]
    word2 = [a, b, a, c, a, b, c]
    states = ["q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7"]
    for i in range(len(word1)):
        AFN(states, word1[i:])
    for i in range(len(word2)):
        AFN(states, word2[i:])