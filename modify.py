from mpi4py import MPI
import random
import numpy as np
from original_tsp import GA,TravelSalesPerson
import matplotlib.pyplot as plt
import numpy as np

comm = MPI.COMM_WORLD
comm_rank = comm.Get_rank()
comm_size = comm.Get_size()

#城市的数量
N_CITIES = 24  # DNA size
#交叉配对的比率
CROSS_RATE = 0.1
#变异的概率
MUTATE_RATE = 0.02
#种群的数量
POP_SIZE = 120
#变异的代数
N_GENERATIONS = 99999999

if comm_rank == 0:
    #遗传算法的实体
    ga = GA(DNA_size=N_CITIES, cross_rate=CROSS_RATE, mutation_rate=MUTATE_RATE, pop_size=POP_SIZE)
    #环境
    env = TravelSalesPerson(N_CITIES)
    #把这个ga数组按照进程的数量平均分成pop_divsize份
    pop_div = np.split(ga.pop,comm_size,axis = 0)
else:
    pop_div = None
pop_div = comm.scatter(pop_div,root = 0)

for generation in range(N_GENERATIONS):
    #翻译DNA,env.city_position表示城市所在的位置，并打印其坐标
    lx, ly = ga.translateDNA(ga.pop, env.city_position)
    #整个路线的长度
    fitness, total_distance = ga.get_fitness(lx, ly)
    #进化DNA
    ga.evolve(fitness)


if comm_rank == 0:
    data = comm.gather(data, root=0)
else:
    comm.gather(data,root=0)


#可视化
best_idx = np.argmax(fitness)

print('Gen:', generation, '| best fit: %.2f' % fitness[best_idx],)

env.plotting(lx[best_idx], ly[best_idx], total_distance[best_idx])


plt.ioff()
plt.show()