import pickle
import numpy as np
import pandas as pd
import scipy.sparse as sp
import pdb
from deeprobust.graph.global_attack import NodeEmbeddingAttack
from deeprobust.graph.defense import DeepWalk
from deeprobust.graph.data import AmazonPyg
from deeprobust.graph.data import Dataset, Dpr2Pyg, Pyg2Dpr

np.set_printoptions(threshold=np.inf)
pd.set_option('display.max_rows', None)

def main():
    # test = AmazonPyg(root='D:\\ether\\tmp', name='test',allow_pickle=True)
    # dpr_data = Pyg2Dpr(test)
    # print(type(dpr_data))
    # data=dpr_data
    # data = Dataset(root='D:\\ether\\tmp', name='test')
    # #
    # with open('dprmodel.txt', 'wb') as f:
    #     picklestring = pickle.dump(data,f)
    # return
    with open('dprmodel.txt', 'rb') as f:
        data = pickle.load(f)
    adj, features, labels = data.adj, data.features, data.labels
    print(adj)
    return
    # print(type(adj))
    # with open('D:\\ether\\testadj.txt', 'w') as f:
    #     print(adj, file=f)
    # print(adj)

    print(1)
    NodeEmbeddingAttackModel = NodeEmbeddingAttack()
    with open('NodeEmbeddingAttack.txt', 'wb') as f:
        picklestring = pickle.dump(NodeEmbeddingAttackModel,f)


    print(2)
    NodeEmbeddingAttackModel.attack(adj, attack_type="remove")  # 只对adj进行攻击，没有使用features和labels其他的没有变
    print(3)
    modified_adj = NodeEmbeddingAttackModel.modified_adj
    pdb.set_trace()
    print(modified_adj)
    NodeEmbeddingAttackModel.attack(adj, attack_type="remove", min_span_tree=True)
    modified_adj = NodeEmbeddingAttackModel.modified_adj
    print(modified_adj)

    idx_train, idx_val, idx_test = data.idx_train, data.idx_val, data.idx_test
    attacker = NodeEmbeddingAttack()
    attacker.attack(adj, attack_type="remove", n_perturbations=1000)
    modified_adj = attacker.modified_adj
    print("Test DeepWalk on clean graph")
    model = DeepWalk()
    model.fit(adj)
    model.evaluate_node_classification(labels, idx_train, idx_test)
    print("Test DeepWalk on attacked graph")
    model.fit(modified_adj)
    model.evaluate_node_classification(labels, idx_train, idx_test)
    print("Test DeepWalk SVD")
    model = DeepWalk(type="svd")
    model.fit(modified_adj)
    model.evaluate_node_classification(labels, idx_train, idx_test)
if __name__ == '__main__':
    main()