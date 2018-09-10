def transition(state, symbol):

    if state == "q1":
        if symbol == 'a':
            return "q1"
        elif symbol == 'b':
            return "q2"
        else:
            return "q3"

    elif state == "q2":
        if symbol == 'a':
            return "q4"
        elif symbol == 'b':
            return "q2"
        else:
            return "q3"

    elif state == "q3":
        if symbol == 'c':
           return "q3"
        else:
           return "q4"

    else:
        return "q4"

def AFD(states, word):
    state = states[0]
    acceptableWord = []
    for symbol in word:
        state = transition(state, symbol)
        acceptableWord.append(symbol)
        if state == "q1" or state == "q2" or state == "q3":
            print(acceptableWord)

if __name__ == "__main__":
    a = 'a'
    b = 'b'
    c = 'c'
    word1 = [b, a, a, b, b, a]
    word2 = [a, b, a, c, a, b, c]
    states = ["q1", "q2", "q3", "q4"]
    for i in range(len(word1)):
        AFD(states, word1[i:])
    for i in range(len(word2)):
        AFD(states, word2[i:])