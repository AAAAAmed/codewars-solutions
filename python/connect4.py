# Kata: https://www.codewars.com/kata/56882731514ec3ec3d000009
def who_is_winner(pieces_position_list):
    # --- Parse moves ---
    column = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6}
    player = {'Red':1,'Yellow':2}
    moveList = [[column[i.split("_")[0]], player[i.split('_')[1]]] for i in pieces_position_list]

    # --- Generate board from moves ---
    board = [[0 for i in range(6)] for i in range(7)]
    winner = 0
    moveNum = 1
    for move in moveList:
        board[move[0]][5 - list(reversed(board[move[0]])).index(0)] = move[1]

    # --- Find winner from board ---
        lastMovePosi = [[move[0]+x, board[move[0]].index(move[1])+y] for x,y in [(-1,0), (1,0), (0,-1), (0,1), (1,1), (1,-1), (-1,1), (-1,-1), (0,0)]]
        for offset in [(-1,0), (1,0), (0,-1), (0,1), (1,1), (1,-1), (-1,1), (-1,-1)]:
            for lastMovePos in lastMovePosi:
                posList = [(lastMovePos[0]+offset[0]*i, lastMovePos[1]+offset[1]*i) for i in range(4)]
                fail = False
                for pos in posList:
                    if pos[0] < 0 or pos[0] > 6 or pos[1] < 0 or pos[1] > 5:
                        fail = True
                if fail: continue

                pieceList = [board[pos[0]][pos[1]] for pos in posList]
                if len(set(pieceList)) == 1 and pieceList[0] != 0:
                    winner = move[1]

        if winner:
            break

        moveNum += 1

    return 'Yellow' if winner == 2 else 'Red' if winner == 1 else 'Draw'

print(who_is_winner(
    ["F_Yellow", "G_Red", "D_Yellow", "C_Red", "A_Yellow", "A_Red", "E_Yellow", "D_Red", "D_Yellow", "F_Red",
    "B_Yellow", "E_Red", "C_Yellow", "D_Red", "F_Yellow", "D_Red", "D_Yellow", "F_Red", "G_Yellow", "C_Red",
    "F_Yellow", "E_Red", "A_Yellow", "A_Red", "C_Yellow", "B_Red", "E_Yellow", "C_Red", "E_Yellow", "G_Red",
    "A_Yellow", "A_Red", "G_Yellow", "C_Red", "B_Yellow", "E_Red", "F_Yellow", "G_Red", "G_Yellow", "B_Red",
    "B_Yellow", "B_Red"]
))
print('Expected: Red')
