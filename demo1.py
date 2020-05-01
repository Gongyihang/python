from mpi4py import MPI
import random
import numpy as np

comm = MPI.COMM_WORLD
comm_rank = comm.Get_rank()
comm_size = comm.Get_size()

DNA_size = 12
pop_size = 12


if comm_rank == 0:
    pop = np.vstack([np.random.permutation(DNA_size) for _ in range(pop_size)])
    print(pop)
    pop_div = np.split(pop,comm_size,axis = 0)
    data = pop_div
else:
    data = None
data = comm.scatter(data,root = 0)
print(comm_rank)

print(random.random())


if comm_rank == 0:
    data = comm.gather(comm_rank, root=0)
else:
    comm.gather(comm_rank,root=0)