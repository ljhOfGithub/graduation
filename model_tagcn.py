#224 97.69 200epoch
#su 99.51 200epoch
#all 99.08 200epoch
#label 72.74/95.80/82.69 200epoch

import os.path as osp

import torch
import torch.nn.functional as F
from torch_geometric.datasets import Planetoid
import torch_geometric.transforms as T
from torch_geometric.nn import TAGConv
import create_dataset as cd
import torch_geometric.utils as tu
import data_deal as dd
import numpy as np
epoch_list=[]
value_list=[]
type_list=[]
import pandas as pd
# dataset = 'Cora'
#path = osp.join(osp.dirname(osp.realpath(__file__)), '..', 'data', dataset)
dataset = cd.MyOwnDataset(transform=T.NormalizeFeatures())
data = dataset[0]
print(data)


class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = TAGConv(dataset.num_features, 16)
        self.conv2 = TAGConv(16, 2)

    def forward(self,data):
        x, edge_index = data.x, data.edge_index
        x = F.relu(self.conv1(x, edge_index))
        x = F.dropout(x, training=self.training)
        x = self.conv2(x, edge_index)
        return F.log_softmax(x, dim=1)




device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model, data = Net().to(device), data.to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=0.01, weight_decay=5e-4)


def train():
    model.train()
    optimizer.zero_grad()
    F.nll_loss(model(data)[data.train_mask], data.y[data.train_mask]).backward()
    optimizer.step()


def test():
    model.eval()
    logits, accs = model(data), []
    for _, mask in data('train_mask', 'val_mask', 'test_mask'):
        pred = logits[mask].max(1)[1]
        print(tu.precision(pred, data.y[mask], 2))
        print(tu.recall(pred, data.y[mask], 2))
        print(tu.f1_score(pred, data.y[mask], 2))
        print('\n')
        acc = pred.eq(data.y[mask]).sum().item() / mask.sum().item()
        accs.append(acc)
    value_list.append(tu.precision(pred, data.y[mask], 2)[1].item())
    value_list.append(tu.recall(pred, data.y[mask], 2)[1].item())
    value_list.append(tu.f1_score(pred, data.y[mask], 2)[1].item())
    type_list.append('precision')
    type_list.append('recall')
    type_list.append('f1')
    return accs

best_val_acc = test_acc = 0
for epoch in range(1, 1001):
    train()
    train_acc, val_acc, tmp_test_acc = test()
    epoch_list.append(epoch)
    epoch_list.append(epoch)
    epoch_list.append(epoch)
    if val_acc > best_val_acc:
        best_val_acc = val_acc
        test_acc = tmp_test_acc
    log = 'Epoch: {:03d}, Train: {:.4f}, Val: {:.4f}, Test: {:.4f}'
    print(log.format(epoch, train_acc, best_val_acc, test_acc))
#epoch 1000
torch.save(model.state_dict(),'test.pt')


# model = Net().to(device)
# model.load_state_dict(torch.load('test.pt'))
# model.eval()
# _, pred = model(data).max(dim=1)
# pred = list(pred)
# y = list(data.y)
# predict = pd.DataFrame({'pred':pred,'y':y})
# predict.to_csv('predict-gdc.csv')

#0是normal 1是scam 2是unknown
# dd.get_pred(pred,data.y)

dd.plot_solute(epoch_list,value_list,type_list)

# dd.print_solute(epoch_list,value_list,type_list,'tagcn list.txt')
# node_df=dd.read_csv(r'small/su_node.csv')
# edge_df=dd.read_csv(r'small/su_edge.csv')
# node_fea,type_list=dd.get_node_fea(node_df)
# train_mask,val_mask,test_mask=dd.split_data(type_list,[6,2,2])
# edge_list=dd.id_to_num(node_df,edge_df)
# edge_fea=dd.get_edge_fea(edge_df)
# data1=dd.make_torch_data1(node_fea,edge_list,type_list,train_mask,val_mask,test_mask,edge_fea)
# data1 = data1.to(device)
# model.eval()
# logits, accs = model(), []


# epoch 500
#1 pre0.9285 f10.8819 recall 0.8403
#2 pre0.9250 f10.8976 recall 0.8718
#3 pre0.9318 f10.8896 recall 0.8570




