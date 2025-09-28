from graph import *

# Problem 1
# have the output list be a list and discovered be a set so that checking if an element is in discovered is constant

def DFS_component(G, node):
	edges = G.edges
	output_list = []
	discovered = set()
	process(edges, node, discovered, output_list)
	return output_list


def process(G, node, discovered, output_list):
	if node not in discovered:
		output_list.append(node)
		discovered.add(node)
	for neighbor in sorted(G[node]):
		if neighbor not in discovered:
			process(G, neighbor, discovered, output_list)

# Test graph with one component
G = Graph([('A', 'G'), ('A', 'C'), ('A', 'B'), ('C', 'D'), ('D', 'B'), ('B', 'E'), ('B', 'F')])
# print(DFS_component(G, 'A'))

def DFS_full(G):
	components = 0
	discovered = []
	for v in G.get_vertices():
		if v not in discovered:
			components += 1
			discovered = discovered + DFS_component(G, v)
	return (discovered, components)

# Test graph with 3 components
G_2 = Graph([('A', 'G'), ('A', 'C'), ('A', 'B'), ('C', 'D'), ('D', 'B'), ('B', 'E'), ('B', 'F'), ('H', 'I'), ('I', 'J'), ('M', 'N')])
# print(DFS_full(G_2))

# Problem 3
# store time as a list rather than an integer. this way, all the changes can be synced
def DFS_component_with_times(G, node):
	edges = G.edges
	discovered = {} # a dictionary that stores the key as the node and value as the time 
	time = [0]
	process_with_time(edges, node, discovered, time)

	# change discovered (a dictionary) into the format we want
	return [(key, discovered[key][0], discovered[key][1]) for key in discovered]

def process_with_time(G, node, discovered, time):
	if node not in discovered:
		discovered[node] = (time[0], float('-inf'))
		time[0] += 1

	for neighbor in sorted(G[node]):
		if neighbor not in discovered:
			process_with_time(G, neighbor, discovered, time)

	# add end time
	# (need to make tuple a list in order to update it)
	lst_of_tuple = list(discovered[node])
	lst_of_tuple[1] = time[0]
	discovered[node] = tuple(lst_of_tuple)
	time[0] += 1

# print(DFS_component_with_times(G, 'A'))

