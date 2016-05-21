from skimage import io
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi

class Node(object):
	def __init__(self, x, y):
		self.visited = False
		self.x = x
		self.y = y
	def check(self):
		self.visited = True
	def seen(self):
		return self.visited
	def __repr__(self):
		return "(%d, %d)" % (self.x +1, self.y+1)

def find_cluster(n_map, x, y, cluster_list, edge_img):
	node_q = [n_map[x*1024 + y]]
	cluster = []
	while node_q:
		n = node_q.pop()
		cluster.append(n)
		check_neighbors_2(n_map, n.x, n.y, node_q, edge_img,4)
	cluster_list.append(cluster)


		

def check_neighbors(n_map, x, y, node_q, edge_img):
	if x > 0:
		if edge_img[x-1][y] == 255 and n_map[(x-1)*1024+y].seen() == False:
			n_map[(x-1)*1024+y].check()
			node_q.append(n_map[(x-1)*1024+y])
	if x < 1023:		
		if edge_img[x+1][y] == 255 and n_map[(x+1)*1024+y].seen() == False:
			n_map[(x+1)*1024+y].check()
			node_q.append(n_map[(x+1)*1024+y])

	if y > 0:
		if edge_img[x][y-1] == 255 and n_map[x*1024+y-1].seen() == False:
			n_map[x*1024+y-1].check()
			node_q.append(n_map[x*1024+y-1])

	if y < 1024:
		if edge_img[x][y+1] == 255 and n_map[x*1024+y+1].seen() == False:
			n_map[x*1024+y+1].check()
			node_q.append(n_map[x*1024+y+1])
	#---------------
	if x > 0 and y > 0:
		if edge_img[x-1][y-1] == 255 and n_map[(x-1)*1024+y-1].seen() == False:
			n_map[(x-1)*1024+y-1].check()
			node_q.append(n_map[(x-1)*1024+y-1])
	if x < 1023 and y < 1024:		
		if edge_img[x+1][y+1] == 255 and n_map[(x+1)*1024+y+1].seen() == False:
			n_map[(x+1)*1024+y+1].check()
			node_q.append(n_map[(x+1)*1024+y+1])

	if y > 0 and x < 1024:
		if edge_img[x+1][y-1] == 255 and n_map[(1+x)*1024+y-1].seen() == False:
			n_map[(x+1)*1024+y-1].check()
			node_q.append(n_map[(x+1)*1024+y-1])

	if y < 1024 and x < 0:
		if edge_img[x-1][y+1] == 255 and n_map[(x-1)*1024+y+1].seen() == False:
			n_map[(x-1)*1024+y+1].check()
			node_q.append(n_map[(x-1)*1024+y+1])


def check_neighbors_2(n_map, x, y, node_q, edge_img, tol):
	for i in range(-1*tol,tol+1):
		for j in range(-1*tol,tol+1):
			if x+i >= 0 and x+i < 1024 and y+j >= 0 and y+j < 1024:
				if edge_img[x+i][y+j] == 255 and n_map[(x+i)*1024+y+j].seen() == False:
					n_map[(x+i)*1024+y+j].check()
					node_q.append(n_map[(x+i)*1024+y+j])



n_map = []
cluster_list = []
for i in range(0,1024):
	for j in range(0,1024):
		n_map.append(Node(i,j))

edge_img = io.imread("edges.png")

for i in range(0,1024):
	for j in range(0,1024):
		if edge_img[i][j] == 255 and n_map[i*1024+j].seen() == False:
			n_map[i*1024+j].check()
			find_cluster(n_map, i, j, cluster_list, edge_img)

check_cluster = np.zeros((1024, 1024))

max_l = 0

for i in cluster_list: 
	if len(i) > max_l:
		max_l = len(i)
		largest_cl = i

for i in largest_cl:
	check_cluster[i.x][i.y] = 1
plt.imshow(check_cluster)
plt.show()
