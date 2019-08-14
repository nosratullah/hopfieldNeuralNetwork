# Hopfield Neural Network
A simple Hopfield neural network for recalling memories.
A Hopfield network is a form of recurrent artificial neural network popularized by John Hopfield in 1982, but described earlier by Little in 1974.[1][2] Hopfield nets serve as content-addressable ("associative") memory systems with binary threshold nodes. They are guaranteed to converge to a local minimum and, therefore, may converge to a false pattern (wrong local minimum) rather than the stored pattern (expected local minimum). Hopfield networks also provide a model for understanding human memory.
![hofield](https://user-images.githubusercontent.com/13776994/61201384-94801400-a6f9-11e9-8db1-803f8229f868.png)

# Coefficient Matrix
![matrix1](https://user-images.githubusercontent.com/13776994/61285801-d3d06280-a7d6-11e9-8582-23f0a5a7ab3d.png)

This coefficient matrix belong to the tree bleow picture
![hopfield2](https://user-images.githubusercontent.com/13776994/61286506-3a09b500-a7d8-11e9-854c-a896818e5ae9.png)


# Capacity
The Network capacity of the Hopfield network model is determined by neuron amounts and connections within a given network. Therefore, the number of memories that are able to be stored is dependent on neurons and connections. Furthermore, it was shown that the recall accuracy between vectors and nodes was 0.138 (approximately 138 vectors can be recalled from storage for every 1000 nodes) (Hertz et al., 1991). Therefore, it is evident that many mistakes will occur if one tries to store a large number of vectors. When the Hopfield model does not recall the right pattern, it is possible that an intrusion has taken place, since semantically related items tend to confuse the individual, and recollection of the wrong pattern occurs. Therefore, the Hopfield network model is shown to confuse one stored item with that of another upon retrieval. Perfect recalls and high capacity, >0.14, can be loaded in the network by Storkey learning method.[3][4] Ulterior models inspired by the Hopfield network were later devised to raise the storage limit and reduce the retrieval error rate, with some being capable of one-shot learning.[5]

# Refrences
[1] Gurney, Kevin (2002). An Introduction to Neural Networks. Routledge. ISBN 978-1857285031.

[2] Sathasivam, Saratha (2008). "Logic Learning in Hopfield Networks". arXiv:0804.4075 [cs.LO].

[3] Liou, C.-Y.; Lin, S.-L. (2006). "Finite memory loading in hairy neurons" (PDF). Natural Computing. 5 (1): 15–42. doi:10.1007/s11047-004-5490-x.

[4] Liou, C.-Y.; Yuan, S.-K. (1999). "Error Tolerant Associative Memory" (PDF). Biological Cybernetics. 81 (4): 331–342. doi:10.1007/s004220050566. PMID 10541936.

[5] ABOUDIB, Ala; GRIPON, Vincent; JIANG, Xiaoran (2014). "A study of retrieval algorithms of sparse messages in networks of neural cliques". COGNITIVE 2014 : The 6th International Conference on Advanced Cognitive Technologies and Applications: 140–146.
