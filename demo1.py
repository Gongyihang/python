from mpi4py import MPI
import random
import numpy as np

# comm = MPI.COMM_WORLD
# comm_rank = comm.Get_rank()
# comm_size = comm.Get_size()

# DNA_size = 12
# pop_size = 12


# if comm_rank == 0:
#     pop = np.vstack([np.random.permutation(DNA_size) for _ in range(pop_size)])
#     # print(pop)
#     pop_div = np.split(pop,comm_size,axis = 0)
#     data = pop_div
# else:
#     data = None 
# data = comm.scatter(data,root = 0)
# print(data)

# print(random.random())
# print("$$$$$$$$$$")


# if comm_rank == 0:
#     data = comm.gather(comm_rank, root=0)
#     print("########")
#     print(data)
# else:
#     comm.gather(comm_rank,root=0)

POP = [np.random.permutation(20) for _ in range(120)]
np.savetxt("data.txt",POP)

p = np.loadtxt("data.txt")