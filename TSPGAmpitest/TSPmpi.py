from mpi4py import MPI
import random
import numpy as np
from original_tsp import GA,TravelSalesPerson
import matplotlib.pyplot as plt
import time


start = time.clock()

comm = MPI.COMM_WORLD
comm_rank = comm.Get_rank()
comm_size = comm.Get_size()

#城市的数量
N_CITIES = 48  # DNA size
#交叉配对的比率
CROSS_RATE = 0.15
#变异的概率
MUTATE_RATE = 0.03
#种群的数量
POP_SIZE_ALL = 7680
#变异的代数
N_GENERATIONS = 1500

POP_SIZE = POP_SIZE_ALL // comm_size


if comm_rank == 0:
    #遗传算法的实体
    ga = GA(DNA_size=N_CITIES, cross_rate=CROSS_RATE, mutation_rate=MUTATE_RATE, pop_size=POP_SIZE)
    #环境
    env = TravelSalesPerson(N_CITIES)

else:
    #遗传算法的实体
    ga = GA(DNA_size=N_CITIES, cross_rate=CROSS_RATE, mutation_rate=MUTATE_RATE, pop_size=POP_SIZE)
    #环境
    env = TravelSalesPerson(N_CITIES)

# temp = [0]

for generation in range(N_GENERATIONS):
    #翻译DNA,env.city_position表示城市所在的位置，并打印其坐标
    lx, ly = ga.translateDNA(ga.pop, env.city_position)
    #整个路线的长度
    fitness, total_distance = ga.get_fitness(lx, ly)
    #进化DNA
    ga.evolve(fitness)
    #可视化
    best_idx = np.argmax(fitness)

    print(comm_rank,' Gen:', generation, '| best fit: %.2f' % fitness[best_idx],)

    env.plotting(lx[best_idx], ly[best_idx], total_distance[best_idx])
    # temp.append(fitness[best_idx])

    # if total_distance[best_idx] - 6.462503133636991 < 0:
    #     break
plt.ioff()
plt.show()

end = time.clock()
print('Time: ', end - start, 's | total_distance: ',total_distance[best_idx])