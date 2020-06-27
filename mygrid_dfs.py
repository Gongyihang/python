import pygame
import time
import sys
import numpy as np

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Game setting
N_SQUARE_ROW = 10
SQUARE = 30
MARGIN = 5
WINDOW = SQUARE * N_SQUARE_ROW + (MARGIN * (N_SQUARE_ROW + 1))


class Map:
    def __init__(self, window_size, square, nsr, margin):#默认是一个10*10的网格
        self.window_size = window_size
        self.square = square
        self.nsr = nsr
        self.margin = margin
        self.screen = pygame.display.set_mode((window_size, window_size))
        pygame.display.set_caption("My First Screen")
        self.start = None
        self.x_start = 20
        self.y_start = 20
        self.map_arr = np.zeros((self.nsr,self.nsr))
        self.end = [self.window_size - self.square - self.margin, self.window_size - self.square - self.margin]
        self.updateMap()
        self.ans = None

    def updateMap(self):
        while True:
            #侦听事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #先退出pygame窗口，再退出程序
                    pygame.quit()
                    sys.exit(0)
            #更新整个待显示的 Surface 对象到屏幕上
            #底色是黑的
            self.screen.fill(BLACK)
            #画白色网格块
            for row in range(self.nsr):
                for column in range(self.nsr):
                    self.map_arr[row][column] = 1
                    pygame.draw.rect(self.screen, WHITE,
                                    [(self.margin + self.square) * column + self.margin, (self.margin + self.square) * row + self.margin,
                                    self.square, self.square])
            self.map_arr[0][0] = 0
            # end = pygame.Rect(self.end[0], self.end[1], self.square, self.square)
            # pygame.draw.rect(self.screen, GREEN, end)

            self.ans = self.dfs_map(self.nsr,self.nsr,0,0)
            # pygame.draw.line(self.screen, RED, [self.x_start,self.y_start],[(self.margin + self.square) * self.ans[0][0] + self.margin,(self.margin + self.square) * self.ans[0][1] + self.margin] , 5)
            time.sleep(0.1)
            for i in range(1,len(self.ans)):
                print(self.ans[i][0],self.ans[i][1])
                # pygame.draw.rect(self.screen, GREEN,[(self.margin + self.square) * self.ans[i][0] + self.margin, (self.margin + self.square) * self.ans[i][1] + self.margin,self.square, self.square])
                pygame.draw.line(self.screen, RED, [(self.margin + self.square) * self.ans[i-1][0]+ self.margin+self.square/2,(self.margin + self.square) * self.ans[i-1][1]+ self.margin+self.square/2], [(self.margin + self.square) * self.ans[i][0]+ self.margin+self.square/2,(self.margin + self.square) * self.ans[i][1]+ self.margin+self.square/2], 5)
                time.sleep(0.1)
                pygame.display.update()
           

    def dfs(self,n, m, x, y, c, ans):
        if c == 0: return True
        dx = [0, -1, 0, 1]
        dy = [-1, 0, 1, 0]
        for k in range(4):
            tx, ty = x + dx[k], y + dy[k]
            if (tx in range(n)) and (ty in range(m)) and self.map_arr[tx][ty] == 1:
                ans.append((tx, ty))
                self.map_arr[tx][ty] = 0
                if self.dfs(n, m, tx, ty, c - 1, ans): return True
                ans.pop()
                map_arr[tx][ty] = 1

        return False


    def dfs_map(self,n, m, sx, sy):
        # Calc Rest
        cnt = 0
        for i in range(n):
            for j in range(m):
                if self.map_arr[i][j] == 1: cnt = cnt + 1

        ans = []
        self.dfs(n, m, sx, sy, cnt, ans)
        return ans
        
m = Map(WINDOW,SQUARE,N_SQUARE_ROW,MARGIN)