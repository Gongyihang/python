from maze_env_modify import Maze
from RL_brain import QLearningTable
import pygame
import time
import sys
import numpy as np

def update():
    # 学习 100 回合
    for episode in range(100):
        # 初始化 state 的观测值
        observation = env.reset()
        print(episode)  
        while True:
            # 更新可视化环境
            env.render()
    #         # RL 大脑根据 state 的观测值挑选 action
            action = RL.choose_action(str(observation))
            # print(observation)

    #         # 探索者在环境中实施这个 action, 并得到环境返回的下一个 state 观测值, reward 和 done (是否是掉下地狱或者升上天堂)
            observation_, reward, done, flag = env.step(action)

    #         # RL 从这个序列 (state, action, reward, state_) 中学习
            RL.learn(str(observation), action, reward, str(observation_))

    #         # 将下一个 state 的值传到下一次循环
            observation = observation_
            
    #         # 如果掉下地狱或者升上天堂, 这回合就结束了
            if done:
                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:   #先退出pygame窗口，再退出程序
                    pygame.quit()
                    sys.exit(0)

    # 结束游戏并关闭窗口
    print('game over')

if __name__ == "__main__":
    # 定义环境 env 和 RL 方式
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)))
    update()