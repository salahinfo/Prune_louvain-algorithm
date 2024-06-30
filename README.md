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

We use tow metric to quantify the quality of detected communities :
- The Modularity function :
  
  ![Screenshot from 2024-06-30 16-17-30](https://github.com/salahinfo/Prune_louvain-algorithm/assets/39995961/0e90223b-48dd-4c61-ac7a-f84ad19a12c4)
- The normal mutual information (NMI), for the networks with ground-truth :
  
  ![Screenshot from 2024-06-30 16-10-15](https://github.com/salahinfo/Prune_louvain-algorithm/assets/39995961/0380e990-6f8b-4233-a774-74efa0a0574a)


# Usage :
 Note that the algorithm has been executed ten times to give you the metric value's maximum, average, and standard deviation. 
 Install all requirements packages mentioned in the file requirments.txt and download the datasets you want to apply the algorithm.
 Then, execute the below command line 
 if the networks have no ground truth. Execute this command.  
 ```
 python3 Plouvain.py "path of dataset"  10 None
 ```
if the networks have ground-truth excute this commmnad 
```
python3 Plouvain.py "path of dataset"  10 "path of ground-truth" 
```
# Refernce:
[1] : http://www.ijcee.org/vol8/927-A023.pdf 
