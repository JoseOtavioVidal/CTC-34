def transition(states, symbol):
    lenght = len(states)
    for i in range(lenght):
        if states[i] == "q0":
            if symbol == 'a':
                states.append("q4")
                states.append("q1")
            else:
                states.append("q1")
                states.append("q5")

        elif states[i] == "q2":
            if symbol == 'a':
                states.append("q6")
            else:
                states.append("q1")

        elif states[i] == "q3":
            if symbol == 'a':
                states.append("q1")
            else:
                states.append("q6")

        elif states[i] == "q4":
            if symbol == 'a':
                states.append("q4")
                states.append("q2")
            else:
                states.append("q1")

        elif states[i] == "q5":
            if symbol == 'b':
                states.append("q5")
                states.append("q3")
            else:
                states.append("q1")

        else:
            states.append("q6")

    for i in range(lenght):
        states.pop(0)

def AFN(states, word):
    possibleStates = []
    possibleStates.append(states[0])
    acceptableWord = []
    for symbol in word:
        state = transition(possibleStates, symbol)
        acceptableWord.append(symbol)
        if possibleStates.count("q1")>0:
            print(acceptableWord)

if __name__ == "__main__":
    a = 'a'
    b = 'b'
    c = 'c'
    word1 = [b, a, a, b, b, a]
    states = ["q0", "q1", "q2", "q3", "q4", "q5", "q6"]
    for i in range(len(word1)):
        AFN(states, word1[i:])