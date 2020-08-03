from maze_env_dqn import Maze
from DQN import DQN
import pygame
import time
import sys
import numpy as np
MEMORY_CAPACITY = 2000

def update():
    # 学习 100 回合
    # dqn.restore_net()
    for i_episode in range(1000000):
        # 初始化 state 的观测值
        s = env.reset()
        # ep_r = 0
        # print(episode)
        while True:
            # 更新可视化环境
            env.render()
    #         # RL 大脑根据 state 的观测值挑选 action
            # dqn.restore_net()
            a = dqn.choose_action(s)
            # print(observation)

    #         # 探索者在环境中实施这个 action, 并得到环境返回的下一个 state 观测值, reward 和 done (是否是掉下地狱或者升上天堂)
            s_, r, done, info = env.step(a)

    #         # RL 从这个序列 (state, action, reward, state_) 中学习
            dqn.store_transition(s, a, r, s_)

            # ep_r += r
            if dqn.memory_counter > MEMORY_CAPACITY:
                dqn.learn()
                # if done:
                #     print('Ep: ', i_episode,
                #         '| Ep_r: ', round(ep_r, 2))

    #         # 将下一个 state 的值传到下一次循环
            s = s_      
    #         # 如果掉下地狱或者升上天堂, 这回合就结束了
            dqn.save()
            if done:
                print('Episoid: ', i_episode,' |Reward: ', r)
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
    # RL = QLearningTable(actions=list(range(env.n_actions)))
    dqn = DQN()
    update()