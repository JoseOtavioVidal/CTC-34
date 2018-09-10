def transition(states, symbol):
    lenght = len(states)
    for i in range(lenght):
        if states[i] == "q1":
            if symbol == 'b':
                states.append("q1")
                states.append("q2")
            else:
                states.append("q1")


        elif states[i] == "q2":
            if symbol == 'b':
                states.append("q3")
            else:
                states.append("q4")

        elif states[i] == "q3":

            states.append("q3")

        else:
            states.append("q4")

    for i in range(lenght):
        states.pop(0)




def AFN(states, word):
    possibleStates = []
    possibleStates.append(states[0])
    acceptableWord = []
    for symbol in word:
        transition(possibleStates, symbol)
        acceptableWord.append(symbol)
        if possibleStates.count("q3") > 0:
            print(acceptableWord)

if __name__ == "__main__":
    a = 'a'
    b = 'b'
    word = [b,a,a,b,b,a]
    states = ["q1", "q2", "q3", "q4"]
    for i in range(len(word)):
        AFN(states, word[i:])
