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
#     data = comm.gather(data, root=0)
#     # print("########")
#     # print(data)
# else:
#     comm.gather(data,root=0)


# data = [np.random.permutation(24) for _ in range(120)]
# np.savetxt("data.txt",data,fmt="%d")

# load_data = np.loadtxt("data.txt")

# for i, d in enumerate(load_data):
#     print(111)

cities = np.random.rand(24, 2)
np.savetxt("cities.txt",cities)