import networkx as nx # pip install networkx
import matplotlib.pyplot as plt


start_node = (0, 0, 5)
capacities = (2, 3, 5)

open_list = [start_node]
visited = [start_node]

G = nx.DiGraph() # Directed (irányított) gráf
G.add_node(start_node)

while len(open_list) > 0:
    current_node = open_list.pop(0) # Kivesszük az open lista 0. elemét
    for i in range(len(current_node)): # 0, 1, 2
        if current_node[i] != 0: # Üres kancsóból nem öntünk
            for j in range(len(current_node)):
                if i != j:
                    amount = min(current_node[i], capacities[j] - current_node[j])
                    new_node = list(current_node) # Tuple az nem módosítható!
                    new_node[i] -= amount
                    new_node[j] += amount
                    new_node = tuple(new_node)
                    
                    if new_node not in visited:
                        open_list.append(new_node)
                        visited.append(new_node)
                        G.add_node(new_node)
                    
                    if current_node != new_node:
                        G.add_edge(current_node, new_node)
                    
pos = nx.fruchterman_reingold_layout(G)
nx.draw(G, pos, with_labels=True, arrows=True)
plt.savefig("vizes_kancsok/allapotter.png")
plt.close()

end_nodes = []
for node in G.nodes:
    if node[0] == 1:
        end_nodes.append(node)

paths = list(nx.all_simple_paths(G, start_node, end_nodes))
paths.sort(key = lambda x: len(x))

fastest_path = paths[0]
print(fastest_path)