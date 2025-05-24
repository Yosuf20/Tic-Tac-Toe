
def logic(xstate, zstate):
    zero = 'X' if xstate[0] else ('O' if zstate[0] else 0)
    one = 'X' if xstate[1] else ('O' if zstate[1] else 1)
    two = 'X' if xstate[2] else ('O' if zstate[2] else 2)
    three = 'X' if xstate[3] else ('O' if zstate[3] else 3)
    four = 'X' if xstate[4] else ('O' if zstate[4] else 4)
    five = 'X' if xstate[5] else ('O' if zstate[5] else 5)
    six = 'X' if xstate[6] else ('O' if zstate[6] else 6)
    seven = 'X' if xstate[7] else ('O' if zstate[7] else 7)
    eight = 'X' if xstate[8] else ('O' if zstate[8] else 8)
    # nine = 'X' if xstate[9] else ('O' if zstate[9] else 9)
    print(f"{zero} | {one} | {two}")
    print(f"--|---|--")
    print(f"{three} | {four} | {five}")
    print(f"--|---|--")
    print(f"{six} | {seven} | {eight}")

def checkwins(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in wins:
        if xState[i[0]] == xState[i[1]] == xState[i[2]] == 1:
            print("\n----X WINS!!!----\n")
            return 1
        elif zState[i[0]] == zState[i[1]] == zState[i[2]] == 1:
            print("\n----O WINS!!!----\n")
            return 1
    return -1


xState = [0,0,0,0,0,0,0,0,0]
zState = [0,0,0,0,0,0,0,0,0]
turn = 0
print("\n ---Welcome to Tic Tac Toe Game---\n\n")
logic(xState, zState)
while(True):
    if(turn == 0):
        print("\nX's Chance\n")
        value = int(input("Enter a Value: "))
        xState[value] = 1
        logic(xState, zState)
        turn = 1
    else:
        print("\nO Chance\n")
        value = int(input("Enter a Value: "))
        zState[value] = 1
        logic(xState, zState)
        turn = 0
    if(checkwins(xState, zState) == 1):
        break
