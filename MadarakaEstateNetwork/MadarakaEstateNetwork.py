import networkx as nx
import matplotlib.pyplot as plt
from classes.bfs import BfsTraverser

G = nx.Graph()

#put your own nodes here
nodes = ["SportsComplex", "Siwaka", "Ph.1A", "Ph.1B", "STC", "Phase2", "Phase3", "J1", "Mada", "ParkingLot"]
G.add_nodes_from(nodes)
#confirm nodes
G.nodes()

#Add Edges and their weights
#Change this section according to your specific maps information
G.add_edge("SportsComplex", "Siwaka",weight="450")
G.add_edge("Siwaka", "Ph.1A", weight="10")
G.add_edge("Siwaka", "Ph.1B", weight="230")
G.add_edge("Ph.1A", "Ph.1B",weight="100")
G.add_edge("Ph.1A", "Mada", weight="850")
G.add_edge("Ph.1B", "STC", weight="50")
G.add_edge("Ph.1B", "Phase2", weight="112")
G.add_edge("STC", "Phase2", weight="50")
G.add_edge("STC", "ParkingLot", weight="250")
G.add_edge("Phase2", "Phase3",weight="500")
G.add_edge("Phase2", "J1", weight="600")
G.add_edge("Phase3", "ParkingLot", weight="350")
G.add_edge("J1", "Mada", weight="200")
G.add_edge("Mada", "ParkingLot", weight="700")


# Position the nodes to resemble Nairobis map
# Also if you have a different map change this section
G.nodes["SportsComplex"]['pos'] = (-12, 12)
G.nodes["Siwaka"]['pos'] = (-2, 12)
G.nodes["Ph.1A"]['pos'] = (2, 12)
G.nodes["Ph.1B"]['pos'] = (2, 10)
G.nodes["STC"]['pos'] = (2, 8)
G.nodes["Phase2"]['pos'] = (6, 10)
G.nodes["Phase3"]['pos'] = (10, 8)
G.nodes["J1"]['pos'] = (10, 10)
G.nodes["Mada"]['pos'] = (14, 10)
G.nodes["ParkingLot"]['pos'] = (10, 4)  # Set the position of ParkingLot as the end goal

#store all positions in a variable
node_pos = nx.get_node_attributes(G,'pos')
#Call BFS to return set of all possible routes to the goal
#Change this section to call whichever search algorithm that you have coded in classes (DFS,UCS,G-BFS,A*)
route_bfs = BfsTraverser()

#Define source and destination
routes = route_bfs.BFS(G,"SportsComplex","ParkingLot") 
print(route_bfs.visited)
route_list = route_bfs.visited

#color the nodes in the route_bfs
node_col = ['darkturquoise' if not node in route_list else 'peru' for node in G.nodes()]
peru_colored_edges = list(zip(route_list,route_list[1:]))
#color the edges as well
#print(peru_colored_edges)

edge_col = ['darkturquoise' if not edge in peru_colored_edges else 'peru' for edge in G.edges()]
arc_weight=nx.get_edge_attributes(G,'weight')
nx.draw_networkx(G, node_pos,node_color= node_col, node_size=450)
nx.draw_networkx_edges(G, node_pos,width=2,edge_color= edge_col)
#nx.draw_networkx_edge_labels(G, node_pos,edge_color= edge_col, edge_labels=arc_weight)

nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)
plt.axis('off')
plt.show()
