def transition(state, symbol):

    if state == "q1":
        if symbol == 'b':
            return "q2"
        else:
            return "q1"

    elif state == "q2":
            if symbol == 'b':
                return "q3"
            else:
                return "q1"
    else:
        return "q3"

def AFD(states, word):
    state = states[0]
    acceptableWord = []
    for symbol in word:
        state = transition(state, symbol)
        acceptableWord.append(symbol)
        if state == "q3":
            print(acceptableWord)

if __name__ == "__main__":
    a = 'a'
    b = 'b'
    word = [b,a,a,b,b,a]
    states = ["q1", "q2", "q3"]
    for i in range(len(word)):
        AFD(states, word[i:])