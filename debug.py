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
and the group with the longest living time is the group with
0x668172d39da7fd4c552f430fc0b694e357c157
as the root, involving a phishing fraud, and its living time is 
3.4 
years. Before the expansion, the group had only 
8 addresses, but after the expansion, they have 
$1,263$ 
addresses. 


After
expanding as a baseline, the scam group with root of 
% 0xd83605cf3aed2a56949c27f\-693c08aeda0e4d145
0xa6e71bdc40952eb1c083e5ae4940d70886296724
 is the most profitable group and its profit reaches 
%  $380,824 $ 
$223,615,694$
 ETH and the average profit is 
%  $513$ 
 $637.54$
 ETH per address. We also draw victim distribution graph which shown in Figure~\ref{fig:Scam group profit}(b). In total, 
%  $2,743,220$ 
 $105,762,720$
 victims have been cheated by these scam groups, and the scam group with 
%  0x3681828da105fc3c44e212f6\-c3dc51a0a5a6f5c6 
 0xc2d7cf95645d33006175b78989035c7c9061d3f9
 as root has the largest number of victims and the number is 
%  $627,332$. 
 $19,298,384$
"""


