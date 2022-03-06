#224 92.22 30epoch
#su 96.05 30epoch
#all 98.98 30epoch
#label 62.38/26.58/37.27 30epoch

import torch
import torch.nn.functional as F
from torch.nn import ModuleList
from tqdm import tqdm
from torch_geometric.datasets import Reddit
from torch_geometric.data import ClusterData, ClusterLoader, NeighborSampler
from torch_geometric.nn import SAGEConv
import torch_geometric.utils as tu
import create_dataset as cd
import data_deal as dd
import sys
epoch_list=[]
value_list=[]
type_list=[]

dataset=cd.MyOwnDataset()
data = dataset[0]
print(data)

cluster_data = ClusterData(data, num_parts=5, recursive=False,save_dir=dataset.processed_dir)#a graph data object into multiple subgraphs, as     motivated by the `"Cluster-GCN: An Efficient Algorithm for Training Deep     and Large Graph Convolutional Networks"
train_loader = ClusterLoader(cluster_data, batch_size=20, shuffle=True,num_workers=0)
#The data loader scheme from the `"Cluster-GCN: An Efficient Algorithm     for Training Deep and Large Graph Convolutional Networks"     <https:arxiv.org/abs/1905.07953>`_ paper which merges partioned subgraphs     and their between-cluster links from a large-scale graph data object to     form a mini-batch.

subgraph_loader = NeighborSampler(data.edge_index, sizes=[-1], batch_size=1024,
                                  shuffle=False, num_workers=0)
#Given a GNN with :math:`L` layers and a specific mini-batch of nodes     :obj:`node_idx` for which we want to compute embeddings, this module     iteratively samples neighbors and constructs bipartite graphs that simulate     the actual computation flow of GNNs.

class Net(torch.nn.Module):
    def __init__(self, in_channels, out_channels):
        super(Net, self).__init__()
        self.convs = ModuleList(
            [SAGEConv(in_channels, 128),
             SAGEConv(128, out_channels)])

    def forward(self, x, edge_index):
        for i, conv in enumerate(self.convs):
            x = conv(x, edge_index)
            if i != len(self.convs) - 1:
                x = F.relu(x)
                x = F.dropout(x, p=0.5, training=self.training)
        return F.log_softmax(x, dim=-1)

    def inference(self, x_all):
        # print(len(x_all))
        # print('xxx')
        # print(x_all.size(0))
        # print(self.convs)
        pbar = tqdm(total=x_all.size(0) * len(self.convs))
        pbar.set_description('Evaluating')
        # Compute representations of nodes layer by layer, using *all*
        # available edges. This leads to faster computation in contrast to
        # immediately computing the final representations of each batch.
        for i, conv in enumerate(self.convs):
            xs = []
            # print(self.convs)
            for batch_size, n_id, adj in subgraph_loader:
                edge_index, _, size = adj.to(device)
                # print(size[1])#1024 。。。 225
                x = x_all[n_id].to(device)
                # print(len(x))
                # print(len(x_all))
                x_target = x[:size[1]]
                # print(len(x_target))
                x = conv((x, x_target), edge_index)
                if i != len(self.convs) - 1:
                    x = F.relu(x)
                # print(len(x))#325时xs为225
                xs.append(x.cpu())#Returns a copy of this object in CPU memory.
                # print(len(x.cpu()))
                pbar.update(batch_size)

            x_all = torch.cat(xs, dim=0)
            # print(len(x_all))
        #333025 - 225 = 332800
        #332800 / 1024 = 325
        pbar.close()

        return x_all


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = Net(dataset.num_features, 2).to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=0.005)


def train():
    model.train()

    total_loss = total_nodes = 0
    for batch in train_loader:
        batch = batch.to(device)
        optimizer.zero_grad()
        out = model(batch.x, batch.edge_index)
        loss = F.nll_loss(out[batch.train_mask], batch.y[batch.train_mask])
        loss.backward()
        optimizer.step()
        nodes = batch.train_mask.sum().item()
        total_loss += loss.item() * nodes
        total_nodes += nodes
    return total_loss / total_nodes


@torch.no_grad()
def test():  # Inference should be performed on the full graph.
    model.eval()#测试模型
    # print('data.x')
    # print(data.x)
    # print(type(data.x))
    out = model.inference(data.x)
    added = torch.zeros((len(data.x) - len(out)), 2)
    out = torch.cat((out, added), 0)
    y_pred = out.argmax(dim=-1)
    # print('out')
    # print(out)
    # print(out.size())
    # print(len(out))
    # print(len(data.x))
    # print(len(y_pred))
    # print(len(data.y))
    # print(len(data.train_mask))
    # print(len(data.val_mask))
    # print(len(data.test_mask))
    # print(len(data.train_mask)+len(data.val_mask)+len(data.test_mask))
    accs = []
    for mask in [data.train_mask, data.val_mask, data.test_mask]:
        # print(y_pred[mask][0:500])
        # print(data.y[mask][0:500])
        # print(tu.precision(y_pred[mask], data.y[mask], 2))
        # print(tu.recall(y_pred[mask], data.y[mask], 2))
        # print(tu.f1_score(y_pred[mask], data.y[mask], 2))
        # print(len(mask))
        correct = y_pred[mask].eq(data.y[mask]).sum().item()
        accs.append(correct / mask.sum().item())

    value_list.append(tu.precision(y_pred[mask], data.y[mask], 2)[1].item())
    value_list.append(tu.recall(y_pred[mask], data.y[mask], 2)[1].item())
    value_list.append(tu.f1_score(y_pred[mask], data.y[mask], 2)[1].item())
    type_list.append('precision')
    type_list.append('recall')
    type_list.append('f1')
    return accs


for epoch in range(1,151):
    loss = train()
    if epoch % 5 == 0:
        train_acc, val_acc, test_acc = test()
        epoch_list.append(epoch)
        epoch_list.append(epoch)
        epoch_list.append(epoch)
        print(f'Epoch: {epoch:02d}, Loss: {loss:.4f}, Train: {train_acc:.4f}, '
              f'Val: {val_acc:.4f}, test: {test_acc:.4f}')
    else:
        print(f'Epoch: {epoch:02d}, Loss: {loss:.4f}')

# print(len(epoch_list))
# print(len(value_list))
# print(len(type_list))
dd.plot_solute(epoch_list,value_list,type_list)

# node_df=dd.read_csv(r'small/su_node.csv')
# edge_df=dd.read_csv(r'small/su_edge.csv')
# node_fea,type_list=dd.get_node_fea(node_df)
# train_mask,val_mask,test_mask=dd.split_data(type_list,[6,2,2])
# edge_list=dd.id_to_num(node_df,edge_df)
# edge_fea=dd.get_edge_fea(edge_df)
# data1=dd.make_torch_data1(node_fea,edge_list,type_list,train_mask,val_mask,test_mask,edge_fea)
# print(data1)
# data1 = data1.to(device)
# #model.eval()
# out = model.inference(data1.x)
# pred = out.argmax(dim=-1)
# print(len(pred))
# dd.get_pred(pred,data1.y)
#1pre0.7562 f1 0.6243  recall 0.5316
#2pre 0.7533 f1 0.7433 recall 0.7336
#3pre 0.7667 f1 0.7662 recall 0.7557