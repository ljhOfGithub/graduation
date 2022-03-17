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
















Traceback (most recent call last):
  File "D:/ether/model_defense.py", line 52, in <module>
    main()
  File "D:/ether/model_defense.py", line 49, in main
    sgc()
  File "D:/ether/model_defense.py", line 41, in sgc
    sgc = SGC(features.shape[1], K=3, lr=0.1,
  File "C:\Users\ljh\miniconda3\lib\site-packages\deeprobust\graph\defense\sgc.py", line 63, in __init__
    self.conv1 = SGConv(nfeat,
  File "C:\Users\ljh\miniconda3\lib\site-packages\torch_geometric\nn\conv\sg_conv.py", line 61, in __init__
    self.lin = Linear(in_channels, out_channels, bias=bias)
  File "C:\Users\ljh\miniconda3\lib\site-packages\torch_geometric\nn\dense\linear.py", line 50, in __init__
    self.weight = Parameter(torch.Tensor(out_channels, in_channels))
TypeError: new() received an invalid combination of arguments - got (float, int), but expected one of:
 * (*, torch.device device)
      didn't match because some of the arguments have invalid types: (!float!, !int!)
 * (torch.Storage storage)
 * (Tensor other)
 * (tuple of ints size, *, torch.device device)
 * (object data, *, torch.device device)

"""


