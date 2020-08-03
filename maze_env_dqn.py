import pygame
import time
import sys
import numpy as np

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

SQUARE = 30 # pixels
MARGIN = 5
PIX_PLUS = SQUARE + MARGIN
MAZE_H = 7  # grid height                               #包含黑色边框，实际map的大小为5*5，上下左右各减1
MAZE_W = 7  # grid width
PIX_HALF = MARGIN + SQUARE//2
WINDOW_WIDTH = MAZE_W * SQUARE + (MAZE_W + 1) * MARGIN
WINDOW_HEIGHT = MAZE_H * SQUARE + (MAZE_H + 1) * MARGIN

class Maze:
    def __init__(self):
        self.action_space = ['u', 'd', 'l', 'r']        #按下标来索引action，0,1,2,3,分别代表上下左右
        self.n_actions = len(self.action_space)         #动作空间大小
        self.screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
        self.map_arr = np.ones((MAZE_H,MAZE_W))         #map的矩阵表示，初试值全为1，值为1表示自由，值为0表示边界或者障碍区域
        pygame.display.set_caption("MAZE")
        self.start = [1,1]
        self.end = [1,2]

    def _build_maze(self):
            self.start = [1,1]
            self.map_arr[1][1] = 0
            self.screen.fill(BLACK)             #更新整个待显示的 Surface 对象到屏幕上#底色是黑的#画白色网格块

            for i in range(0 , MAZE_H):         #将上下左右边界区域置为0
                self.map_arr[i][0] = 0
                self.map_arr[MAZE_W - 1][i] = 0
            for i in range(0 , MAZE_W):
                self.map_arr[0][i] = 0
                self.map_arr[i][MAZE_H - 1] = 0

            for row in range(1 , MAZE_H - 1):       #自由区域设置为1，并画上白色方格    
                for column in range(1 , MAZE_W - 1):
                    self.map_arr[row][column] = 1   #等于1，则没有访问
                    pygame.draw.rect(self.screen, WHITE,[PIX_PLUS * column + MARGIN, PIX_PLUS * row + MARGIN, SQUARE, SQUARE])
            pygame.draw.circle(self.screen, RED, [PIX_PLUS * self.start[0] + PIX_HALF,PIX_PLUS * self.start[1] + PIX_HALF], 3, 3)
            pygame.draw.circle(self.screen, GREEN, [PIX_PLUS * self.end[0] + PIX_HALF,PIX_PLUS * self.end[1] + PIX_HALF], 3, 3)
            pygame.display.update()

    def reset(self):
        self._build_maze()
        pygame.display.update()
        # time.sleep(0.05)
        return self.start

    def step(self, action):
        self.map_arr[1][1] = 0
        s = self.start
        s_ = None
        done = None
        base_action = np.array([0, 0])
        reward = -1
        if action == 0:   # up
            if self.map_arr[s[0]][s[1]-1]:
                base_action[1] -= 1
                reward = 2
        elif action == 1:   # down
            if self.map_arr[s[0]][s[1]+1]:
                base_action[1] += 1
                reward = 2
        elif action == 2:   # right
            if self.map_arr[s[0]+1][s[1]]:
                base_action[0] += 1
                reward = 10
        elif action == 3:   # left
            if self.map_arr[s[0]-1][s[1]]:
                base_action[0] -= 1
                reward = 2
        if self.map_arr[s[0]-1][s[1]] == 0 and self.map_arr[s[0]+1][s[1]] == 0 and self.map_arr[s[0]][s[1]+1] == 0 and self.map_arr[s[0]][s[1]-1] == 0:
            s_ = [9,9]
            done = True
            reward = -1
            if (self.map_arr == 0).all():
                reward = 100
                print(self.map_arr)
            return s_, reward, done , 1
        old = s.copy()
        new = s
        new[0] += base_action[0]
        new[1] += base_action[1]
        self.map_arr[new[0]][new[1]] = 0
        pygame.draw.line(self.screen, RED, [old[0] * PIX_PLUS + PIX_HALF,old[1] * PIX_PLUS + PIX_HALF], [new[0] * PIX_PLUS + PIX_HALF,new[1] * PIX_PLUS + PIX_HALF], 5)
        s_ = new  # next state

        # done function
        if (self.map_arr == 0).all():
            done = True
            s_ = [9,9]
            reward = 100
            print(self.map_arr)
        return s_, reward, done, 0

    def render(self):
        # time.sleep(0.1)
        pygame.display.update()

# if __name__ == '__main__':
#     env = Maze()
#     while True:
#         env.reset()
#     env.after(100, update)
#     env.mainloop()

