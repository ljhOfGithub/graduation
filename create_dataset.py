import os.path as osp

import torch
from torch_geometric.data import Dataset
import data_deal as dd
attacked = 3
class MyOwnDataset(Dataset):
    def __init__(self, root=r'dataset/', transform=None, pre_transform=None):#位于dataset/raw中的是原始csv文件，processed的是训练后的中间文件
        super(MyOwnDataset, self).__init__(root, transform, pre_transform)#Dataset类，cluster-gcn没有设置transform和pre_transform，继承初始值

    @property
    def raw_file_names(self):#文件名
        if attacked == 1:#测试被攻击后的网络
            return [r'node.csv', r'edgemD.csv']#可能产生的攻击是连接到原来的连通子图外的节点，所以不能用nodec.csv
        elif attacked == 2:
            return [r'node.csv', r'edgemR.csv']
        elif attacked == 3:
            return [r'node.csv', r'edgemE.csv']
        elif attacked == 4:
            return [r'node.csv', r'edgemE2.csv']
        elif attacked == 0:
            return [r'nodec.csv', r'edgec.csv']#三次跑模型分别是dataset2,dataset3

    @property
    def processed_file_names(self):#处理后的文件名，如果重新训练需要删除
        return ['data_0.pt']

    def process(self):#需要自己实现
        for raw_path in self.raw_paths:
            if 'node' in raw_path:#读入节点的dataframe
                node_df = dd.read_csv(raw_path)
                print(raw_path)
            elif 'edge' in raw_path:#读入边
                edge_df = dd.read_csv(raw_path)
                print(raw_path)
        node_fea, type_list = dd.get_node_fea(node_df)
        # node_fea, type_list = dd.get_node_fea_three(node_df)
        print('type comp')
        #train_mask, val_mask, test_mask = dd.split_data(type_list, [6, 2, 2])
        train_mask, val_mask, test_mask = dd.split_data_three(type_list, [6, 2, 2])
        print('mask comp')
        # train_mask, val_mask, test_mask = dd.fold_split_data(type_list, 8)
        edge_list = dd.id_to_num(node_df, edge_df)

        edge_fea=dd.get_edge_fea(edge_df)

        #data = dd.make_torch_data(node_fea, edge_list, type_list, train_mask, val_mask, test_mask)
        data = dd.make_torch_data1(node_fea, edge_list, type_list, train_mask, val_mask, test_mask,edge_fea)
        torch.save(data, osp.join(self.processed_dir, 'data_{}.pt'.format(0)))#保存至dataset/processed/data_0.pt



    def len(self):
        return len(self.processed_file_names)

    def get(self, idx):
        data = torch.load(osp.join(self.processed_dir, 'data_{}.pt'.format(idx)))
        return data

