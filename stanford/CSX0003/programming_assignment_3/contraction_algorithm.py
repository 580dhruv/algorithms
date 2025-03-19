#method to load the data from the given txt file
def load_data(file_name):
    file = open(file_name,'r')
    data = file.readlines()
    data = [[int(value) for value in row.strip().split('\t')] for row in data]
    return (data)
#method to separate the adjacency list
def create_list(data):
    print("data :",data)
    # initializing variables
    edges_list = []
    edge_vertice_dict = {}
    vertices_edge_dict = {}
    # adding vertices to vertices_list
    vertices_list = [row[0] for row in data]
    # adding edges to edges_list corresponding edge with its incident vertex-pair to the edge-vertice dict.
    count=1
    for vertice in vertices_list:
        for ver in data[vertice-1]:
            if vertice< ver:
                edges_list.append(count)
                edge_vertice_dict[count] = vertice,ver
                count+=1
    # adding the vertice with its corresponding edges both outgoing and incoming
    for edge in edge_vertice_dict:
        for vertice in edge_vertice_dict[edge]:
            if vertice not in vertices_edge_dict:
                vertices_edge_dict[vertice] = [edge]
            else:
                vertices_edge_dict[vertice].append(edge)
    print("Vertices list :", vertices_list)
    print("edges_list :",edges_list)
    print("edge_vertice_dict :", edge_vertice_dict)
    print("vertices_edge_dict :",vertices_edge_dict)
data = load_data('kargerMinCut.txt')
create_list(data)