"""
>>> from deeprobust.graph.data import AmazonPyg
>>> computers = AmazonPyg(root='D:\\ether\\tmp', name='computers')

>>> from deeprobust.graph.data import Dataset, Dpr2Pyg, Pyg2Dpr
>>> dpr_data = Pyg2Dpr(computers)
>>> data=dpr_data
>>> idx_train, idx_val, idx_test = data.idx_train, data.idx_val, data.idx_test

>>> import numpy as np
>>> idx_unlabeled = np.union1d(idx_val, idx_test)

>>> adj, features, labels = data.adj, data.features, data.labels
>>> from deeprobust.graph.global_attack import NodeEmbeddingAttack
>>> model = NodeEmbeddingAttack()
>>> model.attack(adj, attack_type="remove")

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\ljh\miniconda3\lib\site-packages\deeprobust\graph\global_attack\node_embedding_attack.py", line 73, in attack
    candidates = self.generate_candidates_removal(adj, seed)
  File "C:\Users\ljh\miniconda3\lib\site-packages\deeprobust\graph\global_attack\node_embedding_attack.py", line 129, in generate_candidates_removal
    (np.arange(n_nodes), np.fromiter(map(np.random.choice, adj.tolil().rows), dtype=np.int32)))
  File "mtrand.pyx", line 908, in numpy.random.mtrand.RandomState.choice
ValueError: 'a' cannot be empty unless no samples are taken

"""
