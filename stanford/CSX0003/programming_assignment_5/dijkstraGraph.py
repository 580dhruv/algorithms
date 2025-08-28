import networkx as nx
from pyvis.network import Network
import webbrowser

# Read the input file
def read_file(filename):
    with open("dijkstraData.txt", 'r') as file:
        raw_data = file.readlines()
    data = [[[int(e) for e in col.split(',')] for col in row.strip().split('\t')] for row in raw_data]
    return data

# Process into graph data
def set_data_structure(data):
    path_dict = {}
    vertice_distance_dict = {}
    max_vertex = 0

    for row in data:
        vertex_weight_dict = {}
        for i in range(1, len(row)):
            src = row[0][0]
            dest = row[i][0]
            weight = row[i][1]
            vertice_distance_dict[(src, dest)] = weight
            vertex_weight_dict[dest] = weight
            max_vertex = max(max_vertex, dest)
        path_dict[row[0][0]] = vertex_weight_dict

    vertice_list = list(range(1, max_vertex + 1))
    return path_dict, vertice_list, vertice_distance_dict

# Build the graph
data = read_file("dijkstraData.txt")
path_dict, vertice_list, vertice_distance_dict = set_data_structure(data)
G = nx.DiGraph()
for (u, v), w in vertice_distance_dict.items():
    G.add_edge(u, v, weight=w)

# Create the PyVis graph
net = Network(height="800px", width="100%", directed=True)

# Add nodes and edges
for node in G.nodes():
    net.add_node(node, label=str(node))
print("length of all the edges",len(G.edges))
for u, v, d in G.edges(data=True):
    weight = d.get('weight', '')
    net.add_edge(u, v, label=str(weight), title=f"Weight: {weight}")

# Better layout & style for readability
net.set_options("""
var options = {
  "physics": {
    "enabled": true,
    "stabilization": {
      "enabled": true,
      "iterations": 1000,
      "updateInterval": 25
    },
    "barnesHut": {
      "gravitationalConstant": -20000,
      "centralGravity": 0.3,
      "springLength": 150,
      "springConstant": 0.05,
      "damping": 0.09
    }
  },
  "nodes": {
    "shape": "dot",
    "size": 15,
    "font": { "size": 12 }
  },
  "edges": {
    "font": { "size": 10, "align": "middle" },
    "smooth": true
  }
}
""")

# Show the graph
net.write_html("interactive_graph.html", notebook=False)
webbrowser.open("interactive_graph.html")
