# coding=utf-8
import numpy as np
import gym
import time
import random

CELL, BLOCK, AGENT, GOAL = range(4)
UNIT = 40
random.seed(0)


class Env(gym.Env):
    # playground = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    #               1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    #               1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    #               1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    #               1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    #               1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    #               1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    #               1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    #               1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    #               1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1,
    #               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,]

    playground = [1, 1, 1, 1, 1, 1,
                1, 3, 0, 0, 0, 1,
                1, 0, 0, 0, 0, 1,
                1, 0, 0, 0, 0, 1,
                1, 0, 0, 0, 2, 1,
                1, 1, 1, 1, 1, 1,]

    # [0: Hold, 1: Up, 2: Right, 3: Down, 4: Left]
    action_map = [np.array([0, 0]), np.array([-1, 0]), np.array([0, 1]), np.array([1, 0]), np.array([0, -1])]

    def __init__(self):
        super(Env, self).__init__()

        # general
        self.size_r = 6  # row
        self.size_c = 6  # column
        self.grids = np.array(self.playground).reshape(self.size_r, self.size_c)
        self.agent = np.array([4, 4])
        self.goal = np.array([1, 1])
        self.reach_goal = 0
        self.viewer = None  # to render

    def step(self, act):

            reward, done, s = 0, False, []
            reward -= 0.01  # every step counts, time is limited

            # agent step
            new_pos_a = self.agent + self.action_map[act]

            # validation check for agent step
            # check for whether agent get out of the grids
            if new_pos_a[0] > self.size_r - 1 or new_pos_a[1] > self.size_c - 1:
                new_pos_a = self.agent
                reward -= 0.1
            # check for whether agent step into the block area
            if self.grids[tuple(new_pos_a)] in [1, ]:
                new_pos_a = self.agent
                reward -= 0.1

            self.agent = new_pos_a

            # reach goal
            if self.grids[tuple(new_pos_a)] == 3:
                self.reach_goal = 1
                reward = 1
                done = True

            # generate the states
            s_ = np.concatenate([self.agent / 5, [self.reach_goal]])
            return s_, reward, done

    def reset(self):
        self.agent = np.array([4, 4])
        self.reach_goal = 0
        s0 = np.concatenate([self.agent / 5, [self.reach_goal]])
        return s0

    def render(self, mode='human', close=False):
        if close:
            if self.viewer is not None:
                self.viewer.close()
                self.viewer = None
            return

        from gym.envs.classic_control import rendering
        if self.viewer is None:
            self.viewer = rendering.Viewer(self.size_c * UNIT, self.size_r * UNIT)

        # render playground
        m = np.copy(self.grids)
        g = 0  # the gap between grids
        for x in (range(self.size_c)):
            for y in (range(self.size_r)):
                # the coordinates of 4 angle of the grid
                v = [(x * UNIT + g, y * UNIT + g),
                     ((x + 1) * UNIT - g, y * UNIT + g),
                     ((x + 1) * UNIT - g, (y + 1) * UNIT - g),
                     (x * UNIT + g, (y + 1) * UNIT - g)]
                grid = rendering.FilledPolygon(v)

                if m[(self.size_r-1)-y, x] == 1:  # the block, notice the correspondence between numpy and pyglet
                    grid.set_color(0, 0, 0)  # black
                else:
                    grid.set_color(0, 0.5, 0)  # green

                if m[(self.size_r-1)-y, x] == 3:  # goal
                    grid.set_color(135/255, 206/255, 235/255)  # sky blue
                self.viewer.add_geom(grid)

                # draw outline
                v_outline = v
                outline = rendering.make_polygon(v_outline, False)
                outline.set_linewidth(1)
                outline.set_color(0, 0, 0)
                self.viewer.add_geom(outline)

        # render agent
        self.agent_render = rendering.make_circle(UNIT / 2, 30, True)
        self.agent_render.set_color(1.0, 1.0, 1.0)  # white
        self.viewer.add_geom(self.agent_render)
        self.agent_trans = rendering.Transform()
        self.agent_render.add_attr(self.agent_trans)  # agent position change update
        agent_r, agent_c = self.agent[0], self.agent[1]  # the row and column of agent
        agent_x, agent_y = agent_c, (self.size_r-1)-agent_r  # the relationship between array and coordinates
        self.agent_trans.set_translation((agent_x+0.5) * UNIT, (agent_y+0.5) * UNIT)

        return self.viewer.render(return_rgb_array=mode == 'rgb_array')


if __name__ == '__main__':
    env = Env()
    for i in range(100):  # episode
        s0 = env.reset()
        print('s0', s0)
        for j in range(50):  # step
            a = np.random.randint(5)
            a_map = ['Hold', 'Up', 'Right', 'Down', 'Left']
            print('a:{},{}'.format(a, a_map[a]))

            s_, r, done,  = env.step(a)
            env.render()
            # time.sleep(0.5)

            print('s_:{}, r:{}, done:{}'.format(s_, r, done))
            print()

            if done:
                break
    print('train done')