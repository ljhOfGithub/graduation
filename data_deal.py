import pandas as pd
import numpy as np
import torch
from torch_geometric.data import Data
from torch_geometric.utils import remove_self_loops
from torch_geometric.utils import negative_sampling
from torch_geometric.utils import dropout_adj
# import Graph_Sampling
import networkx as nx
from networkx.algorithms.bipartite.edgelist import parse_edgelist
from networkx.readwrite.gexf import write_gexf
import plotly.express as px
from scipy.sparse import csr_matrix
from scipy.sparse import coo_matrix
from scipy.sparse import lil_matrix
from sklearn.model_selection import KFold
import json
import ast
import numpy.ma as ma

def read_csv(path):
    return pd.read_csv(path)

def id_to_num(node_df,edge_df):
    node_list=[]
    edge_list=[]

    node_list=node_df['Id'].to_list()#节点的id列表
    node_index=range(len(node_list))#创建节点id的索引
    node_list_dict=dict(zip(node_list,node_index))#建立节点的


    # print(node_list)
    edge_from_list=edge_df['Source'].to_list()#边的起点列表
    edge_to_list = edge_df['Target'].to_list()#边的终点列表

    from_list=[]
    for each in edge_from_list:#遍历边的起点列表，将起点添加到from_list
        from_list.append(node_list_dict[each])#根据from节点的id添加节点的索引

    to_list=[]
    for each in edge_to_list:
        to_list.append(node_list_dict[each])

    edge_list=[from_list,to_list]#返回用节点的索引表示的边，即邻接矩阵
    # print(edge_from_list[0:5])
    # print(from_list[0:5])
    # print(edge_to_list[0:5])
    # print(to_list[0:5])
    return edge_list
#获取节点特征
def get_node_fea(node_df):
    fea_list=[]
    type_list = []
    for index, each in node_df.iterrows():
        temp_list=[]
        # temp_list.append(each['indegree'])
        # temp_list.append(each['outdegree'])
        # temp_list.append(each['degree'])
        temp_list.append(each['allIncome'])
        temp_list.append(each['allOutcome'])
        temp_list.append(each['avgIncome'])
        temp_list.append(each['avgOutcome'])
        temp_list.append(each['intxs'])
        temp_list.append(each['outtxs'])
        temp_list.append(each['degree'])
        temp_list.append(each['livingTime'])
        temp_list.append(each['front1/3in'])
        temp_list.append(each['middle1/3in'])
        temp_list.append(each['last1/3in'])
        temp_list.append(each['front1/3out'])
        temp_list.append(each['middle1/3out'])
        temp_list.append(each['last1/3out'])
        #temp_list.append(each['weighted indegree'])
        #temp_list.append(each['weighted outdegree'])
        #temp_list.append(each['weighted degree'])
        fea_list.append(temp_list)

        if(each['type']=='scam'):
            type_list.append(1)
        else:
            type_list.append(0)

    return fea_list,type_list
#获取节点的三个特征，传入node的dataframe
def get_node_fea_three(node_df):
    fea_list=[]
    type_list = []
    for index, each in node_df.iterrows():
        temp_list=[]
        temp_list.append(each['indegree'])
        temp_list.append(each['outdegree'])
        temp_list.append(each['degree'])
        #temp_list.append(each['weighted indegree'])
        #temp_list.append(each['weighted outdegree'])
        #temp_list.append(each['weighted degree'])
        fea_list.append(temp_list)

        if(each['type']=='scam'):#类别标签，第三种是其他
            type_list.append(1)
        elif(each['type']=='normal'):
            type_list.append(0)
        else:
            type_list.append(2)

    return fea_list,type_list#返回特征列表和类别列表
#获取边特征，权重
def get_edge_fea(edge_df):
    fea_list = []
    for index, each in edge_df.iterrows():
        temp_list = []
        temp_list.append(each['Weight'])
        fea_list.append(temp_list)
    return fea_list
#
def split_data(type_list,ratio):
    train_lev=int(len(type_list)*ratio[0]/10)
    val_lev=int(len(type_list)*ratio[1]/10)
    test_lev=int(len(type_list)*ratio[2]/10)
    train_mask=[]
    val_mask=[]
    test_mask=[]

    test_index=np.random.choice(range(len(type_list)),size=test_lev,replace=False)
    remain_index=tuple(set(range(len(type_list)))-set(test_index))
    val_index=np.random.choice(range(len(remain_index)),size=val_lev,replace=False)
    train_index=tuple(set(range(len(type_list)))-set(test_index)-set(val_index))



    for i in range(0,len(type_list)):
        if i in train_index:
            train_mask.append(1)
            val_mask.append(0)
            test_mask.append(0)
        elif i in val_index:
            train_mask.append(0)
            val_mask.append(1)
            test_mask.append(0)
        else:
            train_mask.append(0)
            val_mask.append(0)
            test_mask.append(1)

    train_mask=torch.tensor(train_mask,dtype=torch.bool)
    val_mask = torch.tensor(val_mask, dtype=torch.bool)
    test_mask = torch.tensor(test_mask, dtype=torch.bool)
    return train_mask,val_mask,test_mask

def split_data_three(type_list,ratio):#ratio是占比数组
    ori_type_list=type_list
    type_list=[]
    i=0
    for each in ori_type_list:
        if(each==0 or each==1):#统计正常地址或欺诈地址数
            type_list.append(i)#type_list是有类型的地址的索引
        i=i+1
    print(type_list[0:10])

    train_lev=int(len(type_list)*ratio[0]/10)#训练集长度
    val_lev=int(len(type_list)*ratio[1]/10)#验证集长度
    test_lev=int(len(type_list)*ratio[2]/10)#测试集长度
    train_mask=[]
    val_mask=[]
    test_mask=[]

    test_index=np.random.choice(type_list,size=test_lev,replace=False)#挑选测试的类型列表索引，不可以重复挑选
    remain_index=tuple(set(type_list)-set(test_index))#剩余的类型列表
    val_index=np.random.choice(remain_index,size=val_lev,replace=False)#
    train_index=tuple(set(type_list)-set(test_index)-set(val_index))



    for i in range(0,len(ori_type_list)):
        if i in train_index:
            train_mask.append(1)
            val_mask.append(0)
            test_mask.append(0)
        elif i in val_index:
            train_mask.append(0)
            val_mask.append(1)
            test_mask.append(0)
        elif i in test_index:
            train_mask.append(0)
            val_mask.append(0)
            test_mask.append(1)
        else:
            train_mask.append(0)
            val_mask.append(0)
            test_mask.append(0)

    train_mask=torch.tensor(train_mask,dtype=torch.bool)
    val_mask = torch.tensor(val_mask, dtype=torch.bool)
    test_mask = torch.tensor(test_mask, dtype=torch.bool)
    return train_mask,val_mask,test_mask

def fold_split_data(type_list,ratio):
    # train_lev=int(len(type_list)*ratio[0]/10)
    # val_lev=int(len(type_list)*ratio[1]/10)
    # test_lev=int(len(type_list)*ratio[2]/10)
    train_mask=[]
    val_mask=[]
    test_mask=[]

    f=open(r'split.txt','r')
    index_list=f.readlines()
    f.close()

    train_index=json.loads(index_list[ratio])
    test_index=json.loads(index_list[ratio+1])

    i=0
    for i in range(0,len(type_list)):
        if i in train_index:
            train_mask.append(1)
            val_mask.append(0)
            test_mask.append(0)
        else:
            train_mask.append(0)
            val_mask.append(1)
            test_mask.append(1)

    train_mask=torch.tensor(train_mask,dtype=torch.bool)
    val_mask = torch.tensor(val_mask, dtype=torch.bool)
    test_mask = torch.tensor(test_mask, dtype=torch.bool)
    return train_mask,val_mask,test_mask

def make_torch_data(node_fea,edge_list,type_list,train_mask,val_mask,test_mask):
    x = torch.tensor(node_fea, dtype=torch.float)
    edge_index = torch.tensor(edge_list, dtype=torch.long)
    edge_index =remove_self_loops(edge_index)[0]
    y=torch.tensor(type_list,dtype=torch.long)

    return Data(x=x, edge_index=edge_index,y=y,train_mask=train_mask,val_mask=val_mask,test_mask=test_mask)


def make_torch_data1(node_fea,edge_list,type_list,train_mask,val_mask,test_mask,edge_fea):
    x = torch.tensor(node_fea, dtype=torch.float)
    edge_index = torch.tensor(edge_list, dtype=torch.long)
    #edge_index =remove_self_loops(edge_index)[0]
    #edge_index=negative_sampling(edge_index)
    y=torch.tensor(type_list,dtype=torch.long)
    edge_attr=torch.tensor(edge_fea,dtype=torch.float)
    #dropout_adj(edge_index, edge_attr=edge_attr)

    return Data(x=x, edge_index=edge_index,y=y,train_mask=train_mask,val_mask=val_mask,test_mask=test_mask,edge_attr=edge_attr)

def change_data_format(oldData):


    adj=oldData.edge_index.numpy()
    adj_x,adj_y=adj[0],adj[1]
    # print(adj_x.shape)
    # print(adj_y.shape)
    data=np.ones(adj_x.shape[0])
    # print(data.shape)
    # adj=coo_matrix((data,(adj_x,adj_y)))
    adj=csr_matrix((data,(adj_x,adj_y)),shape=(156256,156256))
    # print(adj)
    features=oldData.x.numpy()
    # fea_x,fea_y=features[0],features[1]
    # data = np.ones(fea_x.shape[0])
    # features = coo_matrix((data, (fea_x, fea_y)))
    features=csr_matrix(features,shape=features.shape)

    labels=oldData.y.numpy()
    # features=csr_matrix(features)
    idx_train=oldData.train_mask.numpy()
    # print(idx_train[0:10])
    idx_val=oldData.val_mask.numpy()
    idx_test=oldData.test_mask.numpy()
    # print(type(bool(idx_train[0])))

    temp=[]
    a=0
    for i in range(0,len(idx_train)):
        if(bool(idx_train[i])):
            temp.append(i)
            a=a+1
    idx_train =np.array(temp)
    # print(a)

    temp = []
    a = 0
    for i in range(0, len(idx_val) ):
        if (bool(idx_val[i])):
            temp.append(i)
            a = a + 1
    idx_val = np.array(temp)
    # print(a)

    temp = []
    a = 0
    for i in range(0, len(idx_test)):
        if (bool(idx_test[i])):
            temp.append(i)
            a = a + 1
    idx_test = np.array(temp)
    # print(a)

    newData = Data(adj=adj,features=features,labels=labels,idx_train=idx_train,idx_val=idx_val,idx_test=idx_test)

    return newData

def change_data_format1(oldData):
    adj = oldData.edge_index.numpy()
    G=nx.from_edgelist(adj.T)
    graph=nx.to_dict_of_lists(G)

    new_train_mask=torch.tensor(oldData.train_mask.numpy(),dtype=torch.int).numpy()+torch.tensor(oldData.val_mask.numpy(),dtype=torch.int).numpy()
    new_test_mask=torch.tensor(oldData.test_mask.numpy(),dtype=torch.int).numpy()
    new_train_mask = np.array([new_train_mask, new_train_mask, new_train_mask]).T
    new_test_mask = np.array([new_test_mask, new_test_mask, new_test_mask]).T

    temp_x=oldData.x.numpy()
    allx=temp_x
    x=ma.array(temp_x,mask=new_train_mask).data
    tx=ma.array(temp_x,mask=new_test_mask).data

    temp_y=oldData.y.numpy()
    all_y=temp_y
    y=ma.array(temp_y,mask=new_train_mask).data
    ty=ma.array(temp_y,mask=new_test_mask).data


def change_data_format2(oldData):


    adj=oldData.edge_index.numpy()
    adj_x,adj_y=adj[0],adj[1]
    # print(adj_x.shape)
    # print(adj_y.shape)
    data=np.ones(adj_x.shape[0])
    # print(data.shape)
    # adj=coo_matrix((data,(adj_x,adj_y)))
    #adj=csr_matrix((data,(adj_x,adj_y)),shape=(4937894,4937894))
    adj = csr_matrix((data, (adj_x, adj_y)), shape=(156256, 156256))
    # print(adj)
    features=oldData.x.numpy()
    # fea_x,fea_y=features[0],features[1]
    # data = np.ones(fea_x.shape[0])
    # features = coo_matrix((data, (fea_x, fea_y)))
    features=csr_matrix(features,shape=features.shape)

    labels=oldData.y.numpy()
    temp=[]
    for each in labels:
        if(each==1):
            temp.append([0,1])
        else:
            temp.append([1,0])
    labels=np.array(temp)
    # features=csr_matrix(features)
    idx_train=oldData.train_mask.numpy()
    # print(idx_train[0:10])
    idx_val=oldData.val_mask.numpy()
    idx_test=oldData.test_mask.numpy()
    # print(type(bool(idx_train[0])))

    # temp=[]
    # a=0
    # for i in range(0,len(idx_train)):
    #     if(bool(idx_train[i])):
    #         temp.append(i)
    #         a=a+1
    # idx_train =np.array(temp)
    # # print(a)
    #
    # temp = []
    # a = 0
    # for i in range(0, len(idx_val) ):
    #     if (bool(idx_val[i])):
    #         temp.append(i)
    #         a = a + 1
    # idx_val = np.array(temp)
    # # print(a)
    #
    # temp = []
    # a = 0
    # for i in range(0, len(idx_test)):
    #     if (bool(idx_test[i])):
    #         temp.append(i)
    #         a = a + 1
    # idx_test = np.array(temp)
    # print(a)

    newData = Data(adj=adj,features=features,labels=labels,idx_train=idx_train,idx_val=idx_val,idx_test=idx_test)

    return newData

def change_data_format3(oldData):
    adj=oldData.edge_index.numpy()
    adj_x,adj_y=adj[0],adj[1]
    # print(adj_x.shape)
    # print(adj_y.shape)
    data=np.ones(adj_x.shape[0])
    # print(data.shape)
    # adj=coo_matrix((data,(adj_x,adj_y)))
    #adj=csr_matrix((data,(adj_x,adj_y)),shape=(4937894,4937894))
    adj = csr_matrix((data, (adj_x, adj_y)), shape=(156256, 156256))
    # print(adj)
    features=oldData.x.numpy()
    # fea_x,fea_y=features[0],features[1]
    # data = np.ones(fea_x.shape[0])
    # features = coo_matrix((data, (fea_x, fea_y)))
    features=lil_matrix(features,shape=features.shape)

    labels=oldData.y.numpy()

    # features=csr_matrix(features)
    idx_train=oldData.train_mask.numpy()
    # print(idx_train[0:10])
    idx_val=oldData.val_mask.numpy()
    idx_test=oldData.test_mask.numpy()

    y_train=np.ma.array(labels,mask=idx_train).data
    y_val = np.ma.array(labels, mask=idx_val).data
    y_test = np.ma.array(labels, mask=idx_test).data
    # print(y_train.shape)
    # print(y_train[0:300])
    # print(y_val.shape)
    temp = []
    for each in y_train:
        if (each == 1):
            temp.append([0, 1])
        else:
            temp.append([1, 0])
    y_train = np.array(temp)

    temp = []
    for each in y_val:
        if (each == 1):
            temp.append([0, 1])
        else:
            temp.append([1, 0])
    y_val = np.array(temp)

    temp = []
    for each in y_test:
        if (each == 1):
            temp.append([0, 1])
        else:
            temp.append([1, 0])
    y_test = np.array(temp)

    # print(type(bool(idx_train[0])))

    # temp=[]
    # a=0
    # for i in range(0,len(idx_train)):
    #     if(bool(idx_train[i])):
    #         temp.append(i)
    #         a=a+1
    # idx_train =np.array(temp)
    # # print(a)
    #
    # temp = []
    # a = 0
    # for i in range(0, len(idx_val) ):
    #     if (bool(idx_val[i])):
    #         temp.append(i)
    #         a = a + 1
    # idx_val = np.array(temp)
    # # print(a)
    #
    # temp = []
    # a = 0
    # for i in range(0, len(idx_test)):
    #     if (bool(idx_test[i])):
    #         temp.append(i)
    #         a = a + 1
    # idx_test = np.array(temp)
    # print(a)

    newData = Data(adj=adj,features=features,labels=labels,idx_train=idx_train,idx_val=idx_val,idx_test=idx_test,
                   y_train=y_train,y_val=y_val,y_test=y_test)

    return newData


def get_edge_from_csv(node_df,edge_df):#创建edge.csv
    node_list=node_df['Id'].to_list()
    edge_source=[]
    edge_to=[]
    for index, each in edge_df.iterrows():
        if each["Source"] in node_list or each['Target'] in node_list:
            edge_source.append(each['Source'])
            edge_to.append(each['Target'])
    edge_list=pd.DataFrame({'Source':edge_source,'Target':edge_to})
    edge_list.to_csv('edge.csv')
    return None

def get_pred(pred,y):
    pred=list(pred)
    y=list(y)
    print(len(pred))
    print(len(y))
    print(pred[0])
    print(y[0])
    predict=pd.DataFrame({'pred':pred,'y':y})
    predict.to_csv('predict-gdc.csv')
    return None

def get_graph(edge_df):
    edge_list=[]
    for index, each in edge_df.iterrows():
        temp_str=''
        temp_str=temp_str+each['Source']+' '
        temp_str = temp_str + each['Target']
        #print(temp_str)
        #temp_str = temp_str + str(each['Weight'])
        edge_list.append(temp_str)
    G=parse_edgelist(edge_list, create_using=nx.Graph(),nodetype=str)
    print(G.nodes())
    print(G.edges())

    return G


# def sample_graph_ISRW(G,node_num):
#     object1 = Graph_Sampling.SRW_RWF_ISRW()
#     sample1 = object1.random_walk_induced_graph_sampling(G,node_num)
#     write_gexf(sample1,'label_ISRW.gexf')
#     return None
# def sample_graph_SB(G,node_num):
#     object1 = Graph_Sampling.Snowball()
#     sample1 = object1.snowball(G,node_num,25)
#     write_gexf(sample1,'label_SB.gexf')
#     return None
# def sample_graph_FF(G,node_num):
#     object1 = Graph_Sampling.ForestFire()
#     sample1 = object1.forestfire(G,node_num)
#     write_gexf(sample1,'label_FF.gexf')
#     return None
# def sample_graph_MHRW(G,node_num):
#     object1 = Graph_Sampling.MHRW()
#     sample1 = object1.mhrw(G,node_num,30)
#     write_gexf(sample1,'label_MHRW.gexf')
#     return None
# def sample_graph_TIES(G,node_num):
#     object1 = Graph_Sampling.TIES()
#     sample1 = object1.ties(G,node_num,0.01)
#     write_gexf(sample1,'label_TIES.gexf')
#     return None
# def plot_solute(epoch_list,value_list,type_list):
#     df=pd.DataFrame({'Epoch':epoch_list,'Value':value_list,'Type':type_list})
#     fig=px.line(df,x='Epoch',y='Value',color='Type',template='simple_white')
#     fig.update_layout(title_font=dict(family='Calibri', size=12, color='black'))
#     fig.show()

    return None
def print_solute(epoch_list,value_list,type_list,path):
    f=open(path,'a')
    f.write(str(epoch_list))
    f.write('\n')
    f.write(str(value_list))
    f.write('\n')
    f.write(str(type_list))
    f.write('\n')
    f.close()
    return None


def dict_to_csv4():
    address = []
    types = []
    tx_type = []
    time_date = []

    froms = []
    tos = []
    values = []

    f = open('victim_trans.txt', 'r')
    str_list = f.readlines()
    f.close()

    print(len(str_list))
    i = 0
    for each_str in str_list:
        if (i == 20000):
            break
        else:
            i = i + 1
        each_dict = ast.literal_eval(each_str)
        # print(each_dict)
        for k, v in each_dict.items():
            # print(type(v))
            v = ast.literal_eval(v)
            if (v['message'] == 'OK'):
                for each in v['result']:
                    # print(type(each))
                    # each=ast.literal_eval(each)
                    address.append(k)
                    types.append('victim')
                    time_date.append(each['timeStamp'])
                    froms.append(each['from'])
                    tos.append(each['to'])
                    if (each['to'] == k):
                        tx_type.append('in')
                    else:
                        tx_type.append('out')
                    values.append(each['value'])
    df = pd.DataFrame({
        'address': address,
        'type': types,
        'date': time_date,
        'value': values,
        'from': froms,
        'to': tos,
        'tx type': tx_type
    })

    print(df.head())
    df.to_csv(r'final_type2_victim_trans.csv', encoding='utf-8')
    return None

def make_same_SU():
    scam_list=pd.read_csv(r'same SU/small4/small_scam100.csv')['id']

    edge_df=pd.read_csv(r'same SU/edge.csv')
    src_list=edge_df['Source']
    tar_list=edge_df['Target']

    edge_list=np.array([src_list,tar_list]).T
    print(edge_list.shape)
    G = nx.from_edgelist(edge_list)
    search_dict=nx.to_dict_of_lists(G)
    print(type(search_dict))

    edge_list = np.array([tar_list, src_list]).T
    print(edge_list.shape)
    G = nx.from_edgelist(edge_list)
    search_dict_rev = nx.to_dict_of_lists(G)
    print(type(search_dict_rev))

    # search_dict=dict(zip(src_list,tar_list))
    # print(len(search_dict))
    # search_dict_rev = dict(zip(tar_list, src_list))

    node_df=pd.read_csv(r'same SU/node.csv')
    id_list=node_df['Id']
    type_list=node_df['type']
    type_dict=dict(zip(id_list,type_list))

    un_list=[]
    new_src=[]
    new_tar=[]

    more_list=[]
    for each in scam_list:
        i=True
        if each in search_dict.keys():
            temp_list=search_dict[each]
            for each_node in temp_list:
                if i and type_dict[each_node]=='normal':
                    i=False
                    un_list.append(each_node)
                new_src.append(each)
                new_tar.append(each_node)

                more_list.append(each_node)
        else:
            temp_list = search_dict_rev[each]
            for each_node in temp_list:
                if i and type_dict[each_node] == 'normal':
                    i = False
                    un_list.append(each_node)
                new_src.append(each_node)
                new_tar.append(each)

                more_list.append(each_node)

    #un_list.append('0x20138ba64daf6f7cabc89d18a93243e77089a01a')
    print(len(scam_list))
    print(len(un_list))

    # i=0
    # for index,each in edge_df.iterrows():
    #     if(i%10==0):
    #         print(i)
    #     if each['Source'] in un_list or each['Target'] in un_list:
    #         new_src.append(each['Source'])
    #         new_tar.append(each['Target'])
    for each in un_list:
        if each in search_dict.keys():
            temp_list=search_dict[each]
            for each_node in temp_list:
                new_src.append(each)
                new_tar.append(each_node)

                more_list.append(each_node)
        else:
            temp_list = search_dict_rev[each]
            for each_node in temp_list:
                new_src.append(each_node)
                new_tar.append(each)

                more_list.append(each_node)

    for each in more_list:
        if each in search_dict.keys():
            temp_list=search_dict[each]
            for each_node in temp_list:
                new_src.append(each)
                new_tar.append(each_node)
        else:
            temp_list = search_dict_rev[each]
            for each_node in temp_list:
                new_src.append(each_node)
                new_tar.append(each)


    df=pd.DataFrame({'scam':scam_list})
    df.to_csv(r'same SU/small4/S_node.csv')
    df = pd.DataFrame({'normal': un_list})
    df.to_csv(r'same SU/small4/n_node.csv')
    df = pd.DataFrame({'Source': new_src, 'Target': new_tar})
    df.to_csv(r'same SU/small4/SU_edge.csv')

    return None

def make_same_SU1():
    scam_list = pd.read_csv(r'same SU/small7/scam.csv')['id']

    edge_df = pd.read_csv(r'same SU/edge.csv')
    src_list = edge_df['Source']
    tar_list = edge_df['Target']

    edge_list = np.array([src_list, tar_list]).T
    print(edge_list.shape)
    G = nx.from_edgelist(edge_list)
    search_dict = nx.to_dict_of_lists(G)
    print(type(search_dict))

    edge_list = np.array([tar_list, src_list]).T
    print(edge_list.shape)
    G = nx.from_edgelist(edge_list)
    search_dict_rev = nx.to_dict_of_lists(G)
    print(type(search_dict_rev))

    new_src = []
    new_tar = []
    for each in scam_list:
        if each in search_dict.keys():
            for i in search_dict[each]:
                new_src.append(each)
                new_tar.append(i)
        else:
            for i in search_dict_rev[each]:
                new_src.append(i)
                new_tar.append(each)
    df = pd.DataFrame({'Source': new_src, 'Target': new_tar})
    df.to_csv(r'same SU/small7/SU_edge.csv')