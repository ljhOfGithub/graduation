from deeprobust.graph.data import Dataset
from deeprobust.graph.defense import SGC
from deeprobust.graph.data import Dataset, Dpr2Pyg, Pyg2Dpr
import numpy as np
def SGC():
    data = Dataset(root='D:\\ether\\tmp', name='test')
    adj, features, labels = data.adj, data.features, data.labels
    idx_train, idx_val, idx_test = data.idx_train, data.idx_val, data.idx_test
    labels = labels.astype(np.float16)
    sgc = SGC(nfeat=features.shape[1], K=3, lr=0.1,
              nclass=labels.max().item() + 1, device='cuda')
    sgc = sgc.to('cuda')
    pyg_data = Dpr2Pyg(data) # convert deeprobust dataset to pyg dataset
    sgc.fit(pyg_data, train_iters=200, patience=200, verbose=True) # train with earlystopping
from deeprobust.graph.data import PrePtbDataset, Dataset
from deeprobust.graph.defense import RGCN
import pickle
def rgcn():
     # load clean graph data
    with open('dprmodel.pkl', 'rb') as f:
         data = pickle.load(f)
    adj, features, labels = data.adj, data.features, data.labels
    idx_train, idx_val, idx_test = data.idx_train, data.idx_val, data.idx_test
     # load perturbed graph data
    perturbed_data = PrePtbDataset(root='D:\\ether\\tmp', name='testc')
    print(1)
    perturbed_adj = perturbed_data.adj
     # train defense model
    model = RGCN(nnodes=perturbed_adj.shape[0], nfeat=features.shape[1],
                      nclass=labels.max() + 1, nhid=32, device='cpu')
    print(2)
    model.fit(features, perturbed_adj, labels, idx_train, idx_val,
                   train_iters=200, verbose=True)
    print(3)
    model.test(idx_test)
    print(4)
    prediction_1 = model.predict()
    print(prediction_1)

def sgc():
    data = Dataset(root='D:\\ether\\tmp', name='test')
    adj, features, labels = data.adj, data.features, data.labels
    idx_train, idx_val, idx_test = data.idx_train, data.idx_val, data.idx_test
    labels = labels.astype(np.float16)
    sgc = SGC(nfeat=features.shape[1], K=3, lr=0.1,
              nclass=labels.max().item() + 1, device='cuda')
    sgc = sgc.to('cuda')
    pyg_data = Dpr2Pyg(data) # convert deeprobust dataset to pyg dataset
    sgc.fit(pyg_data, train_iters=200, patience=200, verbose=True) # train with earlystopping

def main():
    rgcn()
    # Dpr2Pyg()
if __name__ == '__main__':
    main()