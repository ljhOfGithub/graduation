import pickle
import numpy as np
import pandas as pd
import scipy.sparse as sp
import pdb
from deeprobust.graph.global_attack import NodeEmbeddingAttack
from deeprobust.graph.defense import DeepWalk
from deeprobust.graph.data import AmazonPyg
from deeprobust.graph.data import Dataset, Dpr2Pyg, Pyg2Dpr
from torch import optim
from torch.nn import functional as F
from torch.nn.parameter import Parameter
from tqdm import tqdm
from deeprobust.graph import utils
from deeprobust.graph.global_attack import BaseAttack
np.set_printoptions(threshold=np.inf)
pd.set_option('display.max_rows', None)
from deeprobust.graph.defense import GCN
from deeprobust.graph.global_attack import Metattack
from deeprobust.graph.global_attack import Random
from deeprobust.graph.global_attack import PGDAttack
from deeprobust.graph.global_attack import DICE
from deeprobust.graph.utils import preprocess

def Meta():
    with open('dprmodel.pkl', 'rb') as f:
        data = pickle.load(f)
    adj, features, labels = data.adj, data.features, data.labels
    idx_train, idx_val, idx_test = data.idx_train, data.idx_val, data.idx_test
    idx_unlabeled = np.union1d(idx_val, idx_test)
    labels = labels.astype(np.int32)
    surrogate = GCN(nfeat=features.shape[1], nclass=labels.max().item() + 1,
                    nhid=16, dropout=0, with_relu=False, with_bias=False, device='cpu').to('cpu')
    surrogate.fit(features, adj, labels, idx_train, idx_val, patience=30)
    model = Metattack(surrogate, nnodes=adj.shape[0], feature_shape=features.shape,
                      attack_structure=True, attack_features=False, device='cpu', lambda_=0).to('cpu')
    with open('Metattack.pkl', 'wb') as f:
        pickle.dump(model, f)
    # with open('Metattack.pkl', 'rb') as f:
    #     model = pickle.load(f)
    model.attack(features, adj, labels, idx_train, idx_unlabeled, n_perturbations=10, ll_constraint=False)
    modified_adj = model.modified_adj
    sp.save_npz('testmMeta.npz', modified_adj)
def Embed():
    with open('dprmodel.pkl', 'rb') as f:
        data = pickle.load(f)
    print(type(data.adj))
    return
    adj, features, labels = data.adj, data.features, data.labels
    model = NodeEmbeddingAttack()
    # with open('NodeEmbeddingAttack.pkl', 'wb') as f:
    #     pickle.dump(model,f)
    with open('NodeEmbeddingAttack.pkl', 'rb') as f:
        model = pickle.load(f)
    model.attack(adj, attack_type="remove")  # 只对adj进行攻击，没有使用features和labels其他的没有变
    modified_adj = model.modified_adj
    sp.save_npz('testmEmbed.npz', modified_adj)
def RandomAttack():
    with open('dprmodel.pkl', 'rb') as f:
        data = pickle.load(f)
    adj, features, labels = data.adj, data.features, data.labels
    model = Random()
    # with open('RandomAttack.pkl', 'wb') as f:
    #     pickle.dump(model,f)
    with open('RandomAttack.pkl', 'rb') as f:
        model = pickle.load(f)
    model.attack(adj, n_perturbations=10)
    modified_adj = sp.csr_matrix(model.modified_adj)
    print(modified_adj)
    print(type(modified_adj))
    # sp.save_npz('testmRandom.npz', modified_adj)
def Topo():
    with open('dprmodel.pkl', 'rb') as f:
        data = pickle.load(f)
    adj, features, labels = data.adj, data.features, data.labels
    adj, features, labels = preprocess(adj, features, labels, preprocess_adj=False)  # conver to tensor
    print(1)
    idx_train, idx_val, idx_test = data.idx_train, data.idx_val, data.idx_test
     # Setup Victim Model
    print(2)
    victim_model = GCN(nfeat=features.shape[1], nclass=labels.max().item() + 1,
                            nhid=16, dropout=0.5, weight_decay=5e-4, device='cpu').to('cpu')
    print(3)
    victim_model.fit(features, adj, labels, idx_train)
    print(4)
     # Setup Attack Model
    model = PGDAttack(model=victim_model, nnodes=adj.shape[0], loss_type='CE', device='cpu').to('cpu')
    print(5)
    with open('TopoAttack.pkl', 'wb') as f:
        pickle.dump(model,f)
    with open('TopoAttack.pkl', 'rb') as f:
        model = pickle.load(f)
    print(6)
    model.attack(features, adj, labels, idx_train, n_perturbations=10)
    print(7)
    modified_adj = model.modified_adj
    sp.save_npz('testmTopo.npz', modified_adj)
def Dice():
    with open('dprmodel.pkl', 'rb') as f:
        data = pickle.load(f)
    adj, features, labels = data.adj, data.features, data.labels
    model = DICE()
    with open('DiceAttack.pkl', 'wb') as f:
        pickle.dump(model,f)
    with open('DiceAttack.pkl', 'rb') as f:
        model = pickle.load(f)
    model.attack(adj, labels, n_perturbations=10)
    modified_adj = sp.csr_matrix(model.modified_adj)
    sp.save_npz('testmDice.npz', modified_adj)

def DeepwalkDefense():
    with open('dprmodel.pkl', 'rb') as f:
        data = pickle.load(f)
    with open('NodeEmbeddingAttack.pkl', 'rb') as f:
        attacker = pickle.load(f)
    adj, features, labels = data.adj, data.features, data.labels
    idx_train, idx_val, idx_test = data.idx_train, data.idx_val, data.idx_test
     # set up attack model
    # attacker = NodeEmbeddingAttack()
    print(0)
    attacker.attack(adj, attack_type="remove", n_perturbations=1000)
    print(1)
    modified_adj = attacker.modified_adj
    sp.save_npz('testmEmbed2.npz', modified_adj)
    print("Test DeepWalk on clean graph")
    model = DeepWalk()
    model.fit(adj)
    print(2)
    model.evaluate_node_classification(labels, idx_train, idx_test)#根据原图进行评估
    print("Test DeepWalk on attacked graph")
    model.fit(modified_adj)
    print(3)
    model.evaluate_node_classification(labels, idx_train, idx_test)#根据被攻击的图进行评估，svd是奇异值分解
    print("Test DeepWalk SVD")
    model = DeepWalk(type="svd")
    with open('svd.pkl', 'wb') as f:
        pickle.dump(model,f)
    model.fit(modified_adj)
    print(4)
    model.evaluate_node_classification(labels, idx_train, idx_test)
    print(5)
def main():
    # Meta()
    # RandomAttack()
    # Topo()
    # Embed()
    # Dice()
    # return
    # data = Dataset(root='D:\\ether\\tmp', name='test')  # 去除最大连通子图中的节点后的数据集
    # with open('dprmodel.pkl', 'wb') as f:
    #     pickle.dump(data, f)
    # with open('dprmodel.pkl', 'rb') as f:
    #     data = pickle.load(f)
    # sp.save_npz('testa.npz',data.adj)
    # sp.save_npz('testf.npz',data.features)
    DeepwalkDefense()
if __name__ == '__main__':
    main()