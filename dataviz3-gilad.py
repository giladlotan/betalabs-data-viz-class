# dataviz3-gilad.py
# 
# Exercise #3 / BetaLabs tutorial: given the followers list that we grabbed from the Twitter API, use the networkx library to do some graph calculations, and generate a graphml file

import networkx as nx
import pickle

# unpickle the friends info
f = open('friendships.pkl','rb')
friendships = pickle.load(f)
f.close()

print friendships

# create directed graph object
g = nx.DiGraph()

# add nodes to the graph (betaworks twitter users)
for betaworker in friendships.keys():
    g.add_node(betaworker)

# add edges based on who follows who
for betaworker,friendslist in friendships.items():
    for friend in friendslist:
	g.add_edge(betaworker,friend)

# print graph attributes
print "number of nodes:",g.nodes()
for n in g.in_degree_iter():
    print n

nx.write_graphml(g,'betagraph.graphml')
