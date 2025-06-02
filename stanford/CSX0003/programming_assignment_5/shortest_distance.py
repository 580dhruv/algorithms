import random
import math
import heapq
vertices_processed = []
vertex_short_dist = {}
vertex_path_dict = {}
# method that reads the filename that has been passed
def read_file(filename):
    file = open(filename,'r')    # opening the file using the reading mode
    raw_data = file.readlines()     #
    data = [[[int(element) for element in column.split(',')] for column in row.strip().split('\t')] for row in raw_data]
    # data = set_data_structures(data)
    return data
def set_data_structure(data):
    path_dict = {}
    edge_dict = {}
    max =0
    for row in data:
        vertex_weight_dict= {}
        for column_index in range(1,len(row)):
            vertex_weight_dict[row[column_index][0]] =row[column_index][1]
            if (not row[0][0] in edge_dict) :
               edge_dict[row[0][0]]= [row[column_index][0]]
            else:
                edge_dict[row[0][0]].append(row[column_index][0])
            if max<=row[column_index][0]:
                max = row[column_index][0]
        path_dict[row[0][0]] = vertex_weight_dict
    vertice_list = [row for row in range(1,max+1)]
    return path_dict,vertice_list,edge_dict
def compute_shortest_path(source_vertex,path_dict,edge_dict,vertice_list):
    for vertex in vertice_list:
        vertex_short_dist[vertex] = math.inf
        vertex_path_dict[vertex] = []
    # X=[S] (vertices processed so far)
    vertices_processed.append(source_vertex)
    # A[S] =0 (computed shortest path distances)
    vertex_short_dist[source_vertex] = 0
    # B[S] = empty path (computed shortest path)  [This array only to help ,explanation!]
    vertex_path_dict[source_vertex] = [source_vertex]
    # while not X = V:
    while not len(vertices_processed)==len(vertice_list):
    # - among all the edges (v,w)->E with v->X,not w->X, pick the one that minimizes
    #           A[v]+ l(v_w)   (Dijkstra's greedy criterion) [A[v] = (v*,w*) and already compared in previous iteration]
        for tail_vertex,head_vertices in edge_dict.items():
            l_v_w = 0
            for head_vertex in head_vertices:
                heap =[]
                print("tail :",tail_vertex,"head :",head_vertex)
                if ((tail_vertex in vertices_processed) and (not head_vertex in vertices_processed)):
                    l_v_w = vertex_short_dist[tail_vertex] + path_dict[tail_vertex][head_vertex]
                    print("l_v_w :", l_v_w, " vertex_short_dist[head_vertex] :", vertex_short_dist[head_vertex])
                    # if vertex_short_dist[head_vertex] >=l_v_w:
                    # #     - add w* to X
                     #         vertices_processed.append(w*)
                    vertices_processed.append(head_vertex)
                    # #     - set A[w*] = A[v*]+ l[v*_w*]
                    #         A[w*] = A[v*]+ l[v*_w*]
                    vertex_short_dist[head_vertex] = l_v_w
                    # #     - set B[w*] = B[v*]u(v*_w*)
                    #         B[w*] = B[v*]+v*_w*
                    vertex_path_dict[head_vertex] = vertex_path_dict[tail_vertex] + [head_vertex]
                    print("vertices_processed :", vertices_processed)
                    print("vertex_short_dist :", vertex_short_dist)
                    print("vertex_path_dict :", vertex_path_dict)
    return vertices_processed,vertex_short_dist,vertex_path_dict

data=read_file("test_case_2.txt")
path_dict,vertice_list,edge_dict  = set_data_structure(data)
print("path_dict :",path_dict)
print("edge_dict :",edge_dict)
print("vertice_list :",vertice_list)
source_vertex = random.randint(1,len(data))
source_vertex=1
print(source_vertex)
compute_shortest_path(source_vertex,path_dict,edge_dict,vertice_list)
