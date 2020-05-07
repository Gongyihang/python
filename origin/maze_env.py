import numpy as np
import time
import sys
if sys.version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk

UNIT = 40   # pixels
MAZE_H = 10  # grid height
MAZE_W = 10  # grid width

class Maze(tk.Tk, object):
    def __init__(self):
        super(Maze, self).__init__()
        self.action_space = ['u', 'd', 'l', 'r']
        self.n_actions = len(self.action_space)
        self.n_features = 2
        self.cell = MAZE_H * MAZE_W
        self.map_visit = np.zeros([MAZE_H,MAZE_W])
        self.title('maze')
        self.geometry('{0}x{1}'.format(MAZE_H * UNIT, MAZE_W * UNIT))#窗口大小
        self._build_maze()

    def _build_maze(self):
        self.canvas = tk.Canvas(self, bg='white',
                           height=MAZE_H * UNIT,
                           width=MAZE_W * UNIT)
        # create grids
        for c in range(0, MAZE_W * UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, MAZE_H * UNIT
            self.canvas.create_line(x0, y0, x1, y1)
        for r in range(0, MAZE_H * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, MAZE_W * UNIT, r
            self.canvas.create_line(x0, y0, x1, y1)


        # create origin
        origin = np.array([20, 20])
        # start
        self.start_center = origin
        self.start = self.canvas.create_oval(
            self.start_center[0] - 5, self.start_center[1] - 5,
            self.start_center[0] + 5, self.start_center[1] + 5,
            fill='red')
        # end
        self.end_center = origin + np.array([UNIT,0])
        self.end = self.canvas.create_oval(
            self.end_center[0] - 5, self.end_center[1] - 5,
            self.end_center[0] + 5, self.end_center[1] + 5,
            fill='blue')       
        self.canvas.pack()

    def reset(self):
        pass
    def step(self,action):
        s = self.canvas.coords(self.start_center)
        base_action = np.array([0,0])
        if action == 0:#斜左上
            if s[0] > UNIT and s[1] > UNIT:
                base_action[0] -= UNIT
                base_action[1] -= UNIT
                reward = 5
        elif action == 1:#上
            if s[1] > UNIT:
                base_action[1] -= UNIT
                reward = 10
        elif action == 2:#斜右上
            if s[0] < (MAZE_W - 1) * UNIT and s[1] > UNIT:
                base_action[0] += UNIT
                base_action[1] -= UNIT
                reward = 5
        elif action == 3:#左
            if s[0] > UNIT:
                base_action -= UNIT
                reward = 10
        elif action == 4:#右
            if s[0] < (MAZE_W - 1) * UNIT:
                base_action += UNIT
                reward = 10
        elif action == 5:#斜左下
            if s[1] < (MAZE_H - 1) * UNIT and s[0] > UNIT:
                base_action[0] -= UNIT
                base_action[1] += UNIT
                reward = 5
        elif action == 6:#下
            if s[1] < (MAZE_H - 1) * UNIT:
                base_action += UNIT
                reward = 10
        elif action == 7:#斜右下
            if s[0] < (MAZE_W - 1) * UNIT and s[1] < (MAZE_H - 1) * UNIT:
                base_action += UNIT
                base_action += UNIT
                reward = 5

        self.canvas.create_line(self.start_center[0],self.start_center[1],self.start_center[0]+base_action[0],self.start_center[1]+base_action[1])
        next_coords = self.canvas.coords(self.start_center[0]+base_action[0],self.start_center[1]+base_action[1])

        #reward function
        if self.judge_done(next_coords):
            done = True
        else:
            done = False

        s_ = (np.array(next_coords[:2]))

        return s_,reward,done

    def judge_done(self,next_coords):
        for i in range(MAZE_H):
            for j in  range(MAZE_W):
                if self.map_visit[i][j] == 0:
                    return False
        return True


if __name__ == "__main__":
    # maze game
    env = Maze()
    env.mainloop()