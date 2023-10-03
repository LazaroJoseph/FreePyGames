"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot? """#A FIGURA É SOBREPOSTA
"""3. How would you detect when someone has won?""" # LINHA 64-72
"""4. How could you create a computer player?""" # LINHA 50-62


from turtle import *

from freegames import line

import random

def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    width(4) # (1. ADICIONANDO ESPESSURA AO X)
    color('blue') #(1.)ADICIONANDO UMA COR PARA O DEMARCADOR X
    line(x, y, x + 133, y + 133) 
    line(x, y + 133, x + 133, y) 


def drawo(x, y):
    """Draw O player."""
    width(4) # (1. ADICIONANDO ESPESSURA AO O)
    color('green') #(1.)ADICIONANDO UMA COR PARA O DEMARCADOR O
    up()
    goto(x + 67, y + 5)
    down()
    circle(62)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200




#CRIANDO (4. CRIANDO UM COMPUTER PLAYER)
def MaquinaNPC():
    local_vazio = [] #PARTE AINDA NÃO JOGADA
    for i in range(3):
        for j in range(3):
            if grid2[i][j] == -1: 
                local_vazio.append((i, j))

    if local_vazio:
        linha, coluna = random.choice(local_vazio)
        x = linha * 133 - 200 
        y = coluna * 133 - 200 
        tap(x, y)

#VERIFICAR SE HOUVE VENCEDOR
def vencedor(player):
    for i in range(3):
        if all(grid2[i][j] == player for j in range(3)) or all(grid2[j][i] == player for j in range(3)):
            return True
    if all(grid2[i][i] == player for i in range(3)) or all(grid2[i][2 - i] == player for i in range(3)):
        return True

    return False

def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']

    linha = int((x + 200) // 133) 
    coluna = int((y + 200) // 133)

    if grid2[linha][coluna] == -1:
        draw = players[player]
        draw(x, y)
        grid2[linha][coluna] = player
        update()

        if vencedor(player):
            print(f"Jogador(a) {player + 1} fez uma linha/diagonal seguida!")

        state['player'] = not player

        if state['player'] == 1:
            MaquinaNPC()


state = {'player': 0}
players = [drawx, drawo]
grid2= [[-1, -1, -1], 
        [-1, -1, -1], 
        [-1, -1, -1]]



setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
