import heapq

class GBFSTraverser:
    def __init__(self):
        self.visited = []  # List to store visited nodes
        self.end_search = False  # Flag to signal the end of the search

    def GBFS(self, graph, start_node, goal_node, heuristic):
        priority_queue = []  # Use a priority queue (heap) for GBFS
        heapq.heappush(priority_queue, (heuristic[start_node], start_node))  # Initialize the priority queue

        while priority_queue and not self.end_search:
            h, current_node = heapq.heappop(priority_queue)  # Get the node with the lowest heuristic value

            if current_node not in self.visited:
                print("Command: Drive to", current_node, "Estate/Junction")

                if current_node == goal_node:
                    print("We have reached", current_node, "the final destination")
                    self.visited.append(current_node)  # Mark the goal node as visited
                    self.end_search = True  # End the search
                else:
                    self.visited.append(current_node)  # Mark the current node as visited
                    for neighbor in graph[current_node]:
                        if neighbor not in self.visited:
                            heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))  # Add neighbors to the queue
