def transition(states, symbol):
    lenght = len(states)
    for i in range(lenght):
        if states[i] == "q1":
            if symbol == 'a':
                states.append("q4")
            else:
                states.append("q5")

        elif states[i] == "q2":
           states.append("q5")

        elif states[i] == "q3":
            if symbol == 'a':
                states.append("q4")
            else:
                states.append("q5")

        elif states[i] == "q4":
            if symbol == 'a':
                states.append("q5")
            else:
                states.append("q2")
                states.append("q3")
        else:
            states.append("q5")
    for i in range(lenght):
        states.pop(0)

def AFN(states, word):
    possibleStates = []
    possibleStates.append(states[0])
    acceptableWord = []
    for symbol in word:
        if possibleStates.count("q1") > 0:
            print(acceptableWord)
        transition(possibleStates, symbol)
        acceptableWord.append(symbol)
        if possibleStates.count("q2") > 0 or possibleStates.count("q3") > 0:
            print(acceptableWord)


if __name__ == "__main__":
    a = 'a'
    b = 'b'
    c = 'c'
    word1 = [b, a, a, b, b, a]
    word2 = [a, b, a, c, a, b, c]
    states = ["q1", "q2", "q3", "q4", "q5"]
    for i in range(len(word1)):
        AFN(states, word1[i:])
    for i in range(len(word2)):
        AFN(states, word2[i:])