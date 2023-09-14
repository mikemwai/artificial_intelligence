import networkx as nx
import matplotlib.pyplot as plt

# Import the GBFS class
from classes.gbfs import GBFSTraverser  

'''# Import the BFS class
from classes.bfs import BfsTraverser'''

G = nx.Graph()

# Add the nodes here
nodes = ["SportsComplex", "Siwaka", "Ph.1A", "Ph.1B", "STC", "Phase2", "Phase3", "J1", "Mada", "ParkingLot"]
G.add_nodes_from(nodes)
#confirm nodes
G.nodes()

# Add Edges and their weights
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


# Position the nodes to resemble Madaraka Estate map
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
G.nodes["ParkingLot"]['pos'] = (10, 4)  

# Store all positions in a variable
node_pos = nx.get_node_attributes(G,'pos')

# Define the heuristic values 
heuristic = {
    "SportsComplex": 730,
    "Siwaka": 405,
    "Ph.1A": 380,
    "Ph.1B": 280,
    "STC": 213,
    "Phase2": 210,
    "J1": 500,
    "Phase3": 160,
    "Mada": 630,
    "ParkingLot": 0
}

# Initialize the GBFSTraverser
gbfs_traverser = GBFSTraverser()

# Call GBFS to return the set of all possible routes to the goal
# Define source and destination
routes = gbfs_traverser.GBFS(G, "SportsComplex", "ParkingLot", heuristic)
print(gbfs_traverser.visited)
route_list = gbfs_traverser.visited

'''#Call BFS to return set of all possible routes to the goal
#Change this section to call whichever search algorithm that you have coded in classes (DFS,UCS,G-BFS,A*)
route_bfs = BfsTraverser()

#Define source and destination
routes = route_bfs.BFS(G,"SportsComplex","ParkingLot") 
print(route_bfs.visited)
route_list = route_bfs.visited'''

# Color the nodes in the route_bfs
node_col = ['darkturquoise' if not node in route_list else 'peru' for node in G.nodes()]
peru_colored_edges = list(zip(route_list,route_list[1:]))
# Color the edges as well
# print(peru_colored_edges)

edge_col = ['darkturquoise' if not edge in peru_colored_edges else 'peru' for edge in G.edges()]
arc_weight=nx.get_edge_attributes(G,'weight')
nx.draw_networkx(G, node_pos,node_color= node_col, node_size=450)
nx.draw_networkx_edges(G, node_pos,width=2,edge_color= edge_col)

nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)
plt.axis('off')
plt.show()
