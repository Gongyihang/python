import matplotlib.pyplot as plt
import numpy as np
import random
from mpiutil import MPIUtil
from mpi4py import MPI
import original_tsp

comm = MPI.COMM_WORLD
comm_rank = comm.Get_rank()
comm_size = comm.Get_size()


ga = GA(DNA_size=N_CITIES, cross_rate=CROSS_RATE, mutation_rate=MUTATE_RATE, pop_size=POP_SIZE)
#环境
env = TravelSalesPerson(N_CITIES)

if comm_rank == 0:
    data = self.pop_div.copy()
else:
    data = None
data = comm.scatter(data,root = 0)
fit = np.split(fitness,self.pop_mpi, axis = 0)
pop = self.select(fit[comm_rank],data)
pop_copy = pop.copy()
for parent in pop:  # for every parent
    child = self.crossover(parent, pop_copy)
    child = self.mutate(child)
    parent[:] = child
if comm_rank == 0:
    data = comm.gather(data, root=0)
    self.pop_div = data
else:
    comm.gather(data,root=0)