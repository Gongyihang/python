from mpi4py import MPI
import random
import numpy as np

comm = MPI.COMM_WORLD
comm_rank = comm.Get_rank()
comm_size = comm.Get_size()

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
#     data = comm.bcast("1111")
#     print(data)
#     # print("########")
#     # print(data)
# else:
#     data = comm.bcast("1111")
#     print(data)


data = [np.random.permutation(96) for _ in range(960)]
np.savetxt("data960.txt",data,fmt="%d")

# # load_data = np.loadtxt("data.txt")

# # for i, d in enumerate(load_data):
# #     print(111)

# cities = np.random.rand(96, 2)
# np.savetxt("cities.txt",cities)