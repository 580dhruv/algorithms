import random
import math
import heapq
vertices_processed = set()
vertex_short_dist = {}
vertex_path_dict = {}

# method that reads the filename that has been passed
def read_file(filename):
    file = open(filename,'r')    # opening the file using the reading mode
    raw_data = file.readlines()     #
    data = [[[int(element) for element in column.split(',')] for column in row.strip().split("\t")] for row in raw_data]
    # data = set_data_structures(data)
    return data
def set_data_structure(data):
    path_dict = {}
    vertice_distance_dict =  {}
    max =0
    for row in data:
        vertex_weight_dict= {}
        print(row)
        for column_index in range(1,len(row)):
            vertice_distance_dict[(row[0][0], row[column_index][0])] = abs(row[column_index][1])
            vertex_weight_dict[row[column_index][0]] = abs(row[column_index][1])
            if max<=row[column_index][0]:
                max = row[column_index][0]
        path_dict[row[0][0]] = vertex_weight_dict
    vertice_list = set([row for row in range(1,max+1)])
    return path_dict,vertice_list,vertice_distance_dict
def compute_shortest_path(source_vertex,path_dict,vertice_list,vertice_distance_dict):
    for vertex in vertice_list:
        vertex_short_dist[vertex] = math.inf
        vertex_path_dict[vertex] = []
    # X=[S] (vertices processed so far)
    vertices_processed.add(source_vertex)
    # A[S] =0 (computed shortest path distances)
    vertex_short_dist[source_vertex] = 0
    # B[S] = empty path (computed shortest path)  [This array only to help ,explanation!]
    # vertex_path_dict[source_vertex] = [source_vertex]
    # while not X = V:
    while not vertices_processed == vertice_list:           # change : len(X) = len(V)
        # print("vertice_processed :",vertices_processed)
        # print("vertice_list :",vertice_list)
        l_v_w = math.inf
        next_x = ''
        # - among all the edges (v,w)->E with v->X,not w->X, pick the one that minimizes
        #           A[v]+ l(v_w)   (Dijkstra's greedy criterion) [A[v] = (v*,w*) and already compared in previous iteration]
        for vertice_pair,distance in vertice_distance_dict.items():
            if ((vertice_pair[0] in vertices_processed) and (not vertice_pair[1] in vertices_processed)):
                print("vertice_pair[0] :", vertice_pair[0], "vertice_pair[1] :", vertice_pair[1])
                print("vertices_processed :", vertices_processed)
                if vertex_short_dist[vertice_pair[0]]+path_dict[vertice_pair[0]][vertice_pair[1]]<l_v_w:
                    print("1vertex_short_dist[vertice_pair[0]] :", vertex_short_dist[vertice_pair[0]],
                          "path_dict[vertice_pair[0]][vertice_pair[1]] :", path_dict[vertice_pair[0]][vertice_pair[1]],
                          "l_v_w :", l_v_w)
                    l_v_w = vertex_short_dist[vertice_pair[0]]+path_dict[vertice_pair[0]][vertice_pair[1]]
                    next_x = vertice_pair[1]
                    print("vertex_short_dist[vertice_pair[0]] :",vertex_short_dist[vertice_pair[0]],"path_dict[vertice_pair[0]][vertice_pair[1]] :",path_dict[vertice_pair[0]][vertice_pair[1]],"l_v_w :",l_v_w)
                print("vertex_short_dist[next_x] :", vertex_short_dist[next_x],"next_x :",next_x)
        vertices_processed.add(next_x)
        vertex_short_dist[next_x] = l_v_w
    return vertices_processed,vertex_short_dist,vertex_path_dict
data=read_file("dijkstraData.txt")
path_dict,vertice_list,vertice_distance_dict = set_data_structure(data)
print("path_dict :",path_dict)
print("vertice_list :",vertice_list)
print("vertice_distance_dict :",vertice_distance_dict)
# source_vertex = random.randint(1,len(data))
source_vertex=1
# print(source_vertex)
vertices_processed,vertex_short_dist,vertex_path_dict=compute_shortest_path(source_vertex,path_dict,vertice_list,vertice_distance_dict)
# print("vertices_processed :",vertices_processed)
print("vertex_short_dist :",vertex_short_dist)
print("vertex_path_dict :",vertex_path_dict)
print("vertices_processed :",vertices_processed)

