def transition(state, symbol):

    if state == "q1":
        if symbol == 'a':
            return "q2"
        else:
            return "q3"

    elif state == "q2":
        if symbol == 'a':
            return "q4"
        else:
            return "q6"

    elif state == "q3":
        if symbol == 'a':
           return "q6"
        else:
           return "q5"

    elif state == "q4":
        if symbol == 'a':
            return "q4"
        else:
            return "q6"

    elif state == "q5":
        if symbol == 'a':
            return "q6"
        else:
            return "q5"

    else:
        return "q7"

def AFD(states, word):
    state = states[0]
    acceptableWord = []
    for symbol in word:
        state = transition(state, symbol)
        acceptableWord.append(symbol)
        if state == "q2" or state == "q3" or state == "q6" :
            print(acceptableWord)

if __name__ == "__main__":
    a = 'a'
    b = 'b'
    c = 'c'
    word1 = [b, a, a, b, b, a]
    states = ["q1", "q2", "q3", "q4", "q5", "q6", "q7"]
    for i in range(len(word1)):
        AFD(states, word1[i:])