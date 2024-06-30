# Prune_louvain-algorithm
# Introduction 
This repository includes the implementation of the enhanced Louvain algorithm in Python. The main idea behind this improvement is to reduce computational time using the fast local move heuristic.
the Prune louvain algorithm consist of different setps:
```
1- Move the nodes locally using the fast local move 
2- Agreagate the network based on the obtained communities 
3 - Reapt step one and step 2 until no further improvement in the modularity value 
```
The picture represents how the algorithm works:


![Louvain-algorithm-overview-Fig-1-in-10](https://github.com/salahinfo/Prune_louvain-algorithm/assets/39995961/4a4a5740-8ca7-4989-bfd2-e6eed13be551)

