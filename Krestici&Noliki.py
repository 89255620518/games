'''
import pygame
import random

pygame.init()

# Функция, которая рисует сетку для игры
def draw_grid(scr):
    pygame.draw.line(scr, (0, 0, 0), (100, 0), (100, 300), 3)
    pygame.draw.line(scr, (0, 0, 0), (200, 0), (200, 300), 3)
    pygame.draw.line(scr, (0, 0, 0), (0, 100), (300, 100), 3)
    pygame.draw.line(scr, (0, 0, 0), (0, 200), (300, 200), 3)

# функция, которая отрисовывет кресты и нолики на поле
def draw_tic_tac_toe(scr, items):
    for i in range(3):
        for j in range(3):
            if items[i][j] == '0':
                pygame.draw.circle(scr, (255, 0, 0), (j*100 + 50, i*100 + 50), 45)
            elif items[i][j] == 'x':
                pygame.draw.line(scr, (0, 0, 255), (j*100 + 5, i*100 +5),(j*100 + 95, i*100 + 95), 3)
                pygame.draw.line(scr, (0, 0, 255), (j*100 + 95, i*100 +5),(j*100 + 5, i*100 + 95), 3)

# Проверяет все победные исходы
def get_win_chek(fd, symbol):
    flag_win = False
    for line in fd:
        if line.count(symbol) == 3:
            flag_win = True
        for i in range(3):
            if fd[1][i] == fd[0][i] == fd[2][i] == symbol:
                flag_win = True
            if fd[0][0] == fd[1][1] == fd[2][2] == symbol:
                flag_win = True
            if fd[0][2] == fd[1][1] == fd[2][0] == symbol:
                flag_win = True
            return flag_win



# Размер экрана игры
SCREEN_SIZE = (300, 300)
window = pygame.display.set_mode(SCREEN_SIZE)
screen = pygame.Surface(SCREEN_SIZE)

# Название игры и цвет
pygame.display.set_caption("Крестики_Нолики")
screen.fill((255, 255, 255))

# Знач для каждой конкретной клетки
field = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]
mainloop = True
game_over = False

# Игровой цикл
while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Если нажали завершить, то будет завершен
            mainloop = False
        # Проверка на клик мыши
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            # будем добавлять "Х"
            pos = pygame.mouse.get_pos()
            if field[pos[1] // 100][pos[0] // 100] == "":
                field[pos[1] // 100][pos[0] // 100] = "x"

                # Создаем бота
                x, y = random.randint(0, 2), random.randint(0, 2)
                while field[x][y] != "":
                    x, y = random.randint(0, 2), random.randint(0, 2)
                field[x][y] = '0'

            player_win = get_win_chek(field, "x")
            ai_win = get_win_chek(field, "0")
            # Проверка на победу каждый из сторон
            if player_win or ai_win:
                game_over = True
                if player_win:
                    pygame.display.set_caption("Вы победили")
                else:
                    pygame.display.set_caption('Бот выиграл')
            # Или ничья, если было сделано 8 ходов
            elif field[0].count("x") + field[0].count("0") + field[0].count("x") + field[0].count("0") + \
                field[0].count("x") + field[0].count("0") == 0:
                pygame.display.set_caption("Ничья")



            draw_tic_tac_toe(screen, field)




    draw_grid(screen)
    window.blit(screen, (0, 0))
    pygame.display.update()
'''

