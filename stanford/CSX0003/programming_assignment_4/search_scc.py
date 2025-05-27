# importing necessary libraries
import random
import copy
import time
# initializing the variables
nodes_processed=0
current_source_vertex=None
leader = {}
finishing_time = {}
# method to reset the values of the vertex_dict to false
def reinitialize(vertex_dict):
    global leader,finishing_time,current_source_vertex,nodes_processed
    leader.clear()              # clearing leader
    nodes_processed=0           # setting the no of nodes processed to 0
    current_source_vertex=None  # setting the current source vertex to none
    # iterating over vertex_dict
    for vertex in vertex_dict:
        vertex_dict[vertex] = False     # setting the vertex to False
    return  vertex_dict                 # returning the updated vertex_dict
# method which reads the data from the given file
def read_data(filename):
    file = open(filename, 'r')      # opening the filename passed into read mode
    raw_data = file.readlines()     # reading all the lines from the opened file
    # structuring and typecasting data into int
    data = [[int(numb) for numb in (number.strip()).split(' ')] for number in raw_data]
    return data                     # returning the read data
# method which sets data into the data structure accordingly
def data_set(data):
    # initializing the variables
    edge_dict = {}
    reverse_edge_dict = {}
    vertex_dict = {}
    vertex_list = []
    max_vertex= 0
    count = 1
    min_vertex=0
    # iterating over the data
    for tail_vertex,head_vertex in data:
        if tail_vertex not in edge_dict:                        # checking the vertex at tail is not in edge dictionary
            edge_dict[tail_vertex]=[head_vertex]                    # adding it into the dictionary if true
        else :
            edge_dict[tail_vertex].append(head_vertex)              # else just appending into the existing tailed vertex
        if head_vertex not in reverse_edge_dict:                # checking if the head vertex is not in the reversed edge dictionary
            reverse_edge_dict[head_vertex]=[tail_vertex]            # adding it into the dictionary if true
        else :
            reverse_edge_dict[head_vertex].append(tail_vertex)      # else just appending into the existing head vertex
        if max(tail_vertex,head_vertex)>max_vertex:             # checking if max of the tail and head vertices is greater than max vertex
            max_vertex = max(tail_vertex,head_vertex)               # if true then setting the new value of max_vertex
        if min(tail_vertex,head_vertex)<min_vertex:             # checking if min of the tail and head vertices is greater than min vertex
            min_vertex=min(tail_vertex,head_vertex)                 # if true then setting the new value of min_vertex
        count+=1                                            # incrementing the count by 1
    # checking if the min_vertex is equaling to 0 and 0 not in the vertex_dict's values and
    if (min_vertex==0) and (0 not in vertex_dict.values()):
        min_vertex+=1   #  increating the min vertex var by 1
    # iterating over the min to max_Vertex+1
    for vertex in range(min_vertex,max_vertex+1):
        vertex_dict[vertex]=False   # updating the value at vertex in vertex_dictionary
        vertex_list.append(vertex)  # appending the updated vertex into the vertex_list
    return edge_dict,reverse_edge_dict,vertex_dict,vertex_list,max_vertex      # returning  all the data structures
# method to find the possible paths from the current source node and marking it as visited and calls the DFS on that active node.
# marking them  according to there finishing time.
def DFS(edge_dict,vertex_dict,vertex):
    # initializing the variables
    global current_source_vertex,nodes_processed,leader,finishing_time
    # mark i as explored (for the rest of DFS-loop)
    vertex_dict[vertex] = True
    # set leader(i):=node s
    if current_source_vertex not in leader :
        leader[current_source_vertex]= [vertex]         # adding new current_source_vertex to the leader dictionary
    else :
        leader[current_source_vertex].append(vertex)    # appending the vertex into the current_source_vertex in the leader dictionary
    if vertex in edge_dict:
        # for each arc (i,j)EG:
        for edge in edge_dict[vertex]:
            # if j not yet explored :
            if vertex_dict[edge]==False:
                # DFS(G,j)
                vertex_dict=DFS(edge_dict,vertex_dict,edge)
    # t++
    nodes_processed += 1
    # set f(i):=t  [f(i) => its the finishing time]
    finishing_time[nodes_processed] = vertex
    return vertex_dict      # returning the vertex_dictionary
# method which iterates over each vertex in the vertex_list and checks if they have been visited or not.
# And if they have not been visited yet calls DFS setting that node as current active node. returns the updated vertex_dict.
def DFS_loop(edge_dict,vertex_dict,vertex_list):    #DFS_loop(Graph G):
    # no of nodes processed so far
    global nodes_processed    # for finishing times in 1st pass
    # current source vertex
    global current_source_vertex    # for leaders  in 1st pass
    #Assume nodes labelled 1 to n
    #for i=n down to 1
    for vertex in vertex_list:
        # if i not yet explored
        if vertex_dict[vertex]==False :
            # s:=i
            current_source_vertex = vertex
            # DFS(Graph,i)
            vertex_dict = DFS(edge_dict,vertex_dict,vertex)
    return vertex_dict     # returning the updated vertex_dict
# method to reorder the given vertex_dictionary according to there finishing times
def reorder_vertice_dict(finishing_time,vertex_list):
    # iterating over the finishing time dictionary
    for position,vertex in finishing_time.items():
        vertex_list[position-1]=vertex      
    return vertex_list.reverse()    # returning the reversed the vertex dictionary
data = read_data("SCC.txt")     # reading the data from the file
# setting the data into necessary data structures
edge_dict,reverse_edge_dict,vertex_dict,vertex_list,max_vertex = data_set(data)
vertex_list.reverse()   # reversing the vertex list
# 1st DFS-loop: computing the "magical/finishing ordering" of the nodes
vertice_dict = DFS_loop(reverse_edge_dict,vertex_dict,vertex_list)
reinitialize(vertex_dict)   # reinitializing to False in vertex_dict
# reordering the vertices according to there magical/finishing ordering
vertice_list = reorder_vertice_dict(finishing_time, vertex_list)
# 2nd DFS-loop: to discover the SCCs one by one. (Processing nodes in decreasing order of there finishing time)
vertex_dict = DFS_loop(edge_dict,vertex_dict,vertex_list)
# Fetching the biggest 5 SCCs in terms of there size(# of nodes)
top_5_sizes = sorted([len(leader_vertex) for leader_vertex in leader.values()], reverse=True)[:5]
print("Top 5 SCC sizes:", top_5_sizes)      # printing the fetched biggest 5 SCCs
