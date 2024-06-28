from GraphTools import GraphTolls, Read_Graph 
import matplotlib.pyplot as  plt 
import networkx as nx
import random
from collections import deque,Counter
import copy
import time 
import sys
import math
from sklearn.metrics.cluster import normalized_mutual_info_score





class louvain_prune(GraphTolls) :
    
    

    def modularity( self):
        result = 0
        for com in set( self.membership.values()):
            in_degree = self.internal.get( com, 0.)
            degree = self.DegCom.get( com, 0.)
            #print(self.m)
            result += in_degree / self.m - (( degree / ( 2. * self.m )) ** 2.)
            
        return result

    
    def flocalmove ( self , graph, resolution=1):
    
        Nodelist = deque(graph.nodes())
        random.shuffle(Nodelist)
        while Nodelist:
            node = Nodelist.popleft()
            com_node = self.membership[node]
            degc_totw = self.Degree.get(node, 0.) / (self.m * 2.)  # NOQA
            neigh_communities = super().neigh_comm( node, graph )
            super().delet_node(node, com_node, neigh_communities.get(com_node, 0.))
            best_com = com_node
            best_increase = 0
            for com, dnc in neigh_communities.items():
                Delat_Q = resolution * dnc - self.DegCom.get(com, 0.) * degc_totw
                    #print(incr)
                if Delat_Q > best_increase:
                    best_increase = Delat_Q
                    best_com = com
            super().insert_node(node, best_com, neigh_communities.get(best_com, 0.))
            if best_com != com_node:
                for veg in graph[node]:
                    if self.membership[veg] != best_com:    
                        Nodelist.append(veg)
           
        
        return  self.membership


    def LouvainPrune(self,  graph):
        start = time.time()
        super().modifie_status( graph, weight = 'weight')
        solution = self.flocalmove(graph)
        p_list = []
        n_mod = super().modularity()
        mod_graph = graph.copy()
        p = super().renumber()
        p_list.append(p)
        mod_graph = super().induced_graph( p, mod_graph, weight='weight')
        super().modifie_status( mod_graph, weight = 'weight')
        Q_val = n_mod
        while True :
            solution = self.flocalmove(mod_graph)
            #solution = self.FL_move(mod_graph)
            n_mod = super().modularity()
            if n_mod - Q_val < 0.0000001:
                break
            
            Q_val = n_mod
            p = super().renumber()
            p_list.append(p)
            mod_graph = super().induced_graph( p, mod_graph, weight='weight')
            super().modifie_status( mod_graph, weight='weight')
        
        #self.draw_communities( mod_graph, p)        
        P = super().best_sol( p_list, len(p_list)- 1)    
        super().init( graph, P, weight='weight')                                                                          
        end = time.time()
        t = end-start
        return  Q_val, P, t


def de_main():
    #path =  '/home/yacine/Desktop/LFR/network_mu_0.8.dat'
    path = sys.argv[1]
    #'/home/yacine/Desktop/real_network/louvain.txt'
    #Number_iter = int(sys.argv[2])
    graph = Read_Graph(path)
    #super() = super()( path, graph)
    louvain = louvain_prune(path, graph)   
    #graph = datasets.fetch_network_data(net_name="karate_club", net_type="igraph")
    NMI_list = []
    Time_list = [] 
    Q_list = []
    nb_run = 0
    while nb_run < int(sys.argv[2]):
        q,p , tim = louvain.LouvainPrune(graph)
        Q_list.append(q)
        Time_list.append(tim)
        #label = communities.lebel_node(community)  
        if sys.argv[3] != 'None':
            True_partition = GraphTolls.Read_GroundTruth(sys.argv[3])
            p = dict(sorted(p.items()))
            label = list(p.values())
            NMI = normalized_mutual_info_score( True_partition, label)
            NMI_list.append(NMI)

        nb_run = nb_run +1
    
    
    #data.writefile(Q_list)
    Q_avg = louvain.avg(Q_list)
    Q_max = louvain.max(Q_list)
    Q_std = louvain.stdev(Q_list)
    NMI_max = louvain.max(NMI_list)
    time_run = louvain.avg(Time_list)
    print("Q_avg",Q_avg,"Q_max",Q_max,"NMI",NMI_max,time_run,Q_std)
    
if __name__ == '__main__':
    
    de_main()










   