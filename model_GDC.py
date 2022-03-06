#224 0.9301 200epoch
#su 91.88 200epoch
#all 99.08 200epoch
#label 70.77/94.48/80.92 200epoch

import os.path as osp
import argparse

import torch
import torch.nn.functional as F
from torch_geometric.datasets import Planetoid
import torch_geometric.transforms as T
from torch_geometric.nn import GCNConv, ChebConv  # noqa
import create_dataset as cd
import torch_geometric.utils as tu
import data_deal as dd
parser = argparse.ArgumentParser()
parser.add_argument('--use_gdc', action='store_true',
                    help='Use GDC preprocessing.')
args = parser.parse_args()

epoch_list=[]
value_list=[]
type_list=[]
dataset=cd.MyOwnDataset(transform=T.NormalizeFeatures())
data = dataset[0]
print(data)
data.edge_attr=data.edge_attr.flatten()

if args.use_gdc:
    gdc = T.GDC(self_loop_weight=1, normalization_in='sym',
                normalization_out='col',
                diffusion_kwargs=dict(method='ppr', alpha=0.05),
                sparsification_kwargs=dict(method='topk', k=128,
                                           dim=0), exact=True)
    data = gdc(data)


class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = GCNConv(dataset.num_features, 16, cached=True,
                             normalize=not args.use_gdc)
        self.conv2 = GCNConv(16, 2, cached=True,
                             normalize=not args.use_gdc)
        # self.conv1 = ChebConv(data.num_features, 16, K=2)
        # self.conv2 = ChebConv(16, data.num_features, K=2)

    def forward(self,data):
        x, edge_index, edge_weight = data.x, data.edge_index, data.edge_attr
        x = F.relu(self.conv1(x, edge_index, edge_weight))
        x = F.dropout(x, training=self.training)
        x = self.conv2(x, edge_index, edge_weight)
        return F.log_softmax(x, dim=1)


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model, data = Net().to(device), data.to(device)
optimizer = torch.optim.Adam([
    dict(params=model.conv1.parameters(), weight_decay=5e-4),
    dict(params=model.conv2.parameters(), weight_decay=0)
], lr=0.01)  # Only perform weight-decay on first convolution.


def train():
    model.train()
    optimizer.zero_grad()
    F.nll_loss(model(data)[data.train_mask], data.y[data.train_mask]).backward()
    optimizer.step()


@torch.no_grad()
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
for epoch in range(1, 501):
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
dd.plot_solute(epoch_list,value_list,type_list)

# node_df=dd.read_csv(r'small/su_node.csv')
# edge_df=dd.read_csv(r'small/su_edge.csv')
# node_fea,type_list=dd.get_node_fea(node_df)
# train_mask,val_mask,test_mask=dd.split_data(type_list,[6,2,2])
# edge_list=dd.id_to_num(node_df,edge_df)
# edge_fea=dd.get_edge_fea(edge_df)
# data1=dd.make_torch_data1(node_fea,edge_list,type_list,train_mask,val_mask,test_mask,edge_fea)
# data1 = data1.to(device)
# 500
# _, pred = model(data).max(1)
# dd.get_pred(pred,data.y)
#1 pre0.9280 f10.6217 recall 0.4673
#2 pre0.9219  f10.6541 recall 0.5085
#3 pre0.9366 f1 0.6786 recall 0.5321