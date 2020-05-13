class Point(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y


class MAP(object):
	def __init__(self):
        pass
	def draw_init_map(self):
        pass
	def draw_path_open(self):
        pass
	def draw_path_closed(self):
        pass
    def draw_direction_point(self):
        pass
    def draw_axes(self):
        pass
	
#modle:
class Voronoi(object):
    def __init__(self):
        pass
#path algorithm
class Dijkstra(object)：
	def __init__(self,num_of_point,map,start,end):
        self.pre = [0]*(point+1)#previous point
        self.visit = [0]*(point+1)#flag
        self.dist=[_ for i in range(num_of_points+1)]
        self.road=[0] * (num_of_points+1)
        self.roads=[]
        self.map = map
        
        for i in range(num_of_points+1):
            if i == start:
                dist[i] = 0
            else:
                dist[i] = map[start][i]
            if map[start][i] != inf:
                pre[i] == start
            else:
                pre[i] == -1
        visit[start] = -1
					
    def return_dist_road(self,m):
        map = m
        s,e=input("start and end:").split()
        dist,road = Dijkstra.main(num_of_points,map,s,e)
        return dist,road
			
    def main(self):
        for i in range(num_of_points):
            min = inf
            for j in range(num_of_points):
                if vis[j] == 0 and dist[j] < min:
                    t = j
                    min = dist[j]
            visit[t] = 1
            for j  in range(num_of_points+1):
                if visit[j] == 0 and dist[j] > dist[t] + map[t][j]:
                    dist[j] = dist[t] + map[t][j]
                    pre[j] = t
        #inverse
        p = end
        len = 0
        while p >=1 and len < num_of_points:
            road[len] = p
            p = pre[p]
            len+=1
            if p == start:
                break
        roads.append(start)
        len-=1
        while len >= 0:
            roads.append(road[len])
            len-=1
        return dist[end],roads
			

class AStar(object)：
	def __init__(self):
        pass
	def	caculate_h(self):
        pass
    def	g_accumulation(self):
        pass
    def	caculate_g(self):
        pass
    def	caculate_f(self):
        pass
    def	child_point(self):
        pass
    def	judge_location(self):
        pass
    def	direction(self):
        pass
    def	path_backtrace(self):
		
class GA(object)：
	def __init__(self,dna_size,cross_size,mutation_rate):
        pass
    def	translate_dna(self,dna):
        pass
    def	get_fitness(self):
        pass
    def	select(self):
        pass
    def	crossover(self):
        pass
    def	mutate(self):
        pass
    def	evolve(self):
        pass