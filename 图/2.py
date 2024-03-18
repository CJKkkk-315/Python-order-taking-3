
node_list = ['A','B','C','D','E','F','G','H']
edge_list = [['A', 'B', 3, 1],
             ['B', 'E', 2, 2],
             ['B', 'C', 4, 3],
             ['C', 'D', 4, 6],
             ['D', 'G', 6, 7],
             ['E', 'F', 4, 5],
             ['E', 'G', 5, 4],
             ['F', 'G', 2, 8],
             ['G', 'H', 4, 9],
             ]
# 计算入度
in_score = {i:0 for i in node_list}
for i in edge_list:
    in_score[i[1]] += 1
print('不同定点的入度：')
print(in_score)
# 拓扑排序
tp_sort = []
node_list_sort = node_list[::]
edge_list_sort = edge_list[::]
while len(tp_sort) != len(node_list):
    temp_start_list = []
    for edge in edge_list_sort:
        temp_start_list.append(edge[1])
    start_node = [x for x in node_list_sort if x not in temp_start_list][0]
    remove_list = []
    for edge in edge_list_sort:
        if edge[0] == start_node:
            remove_list.append(edge)
    for edge in remove_list:
        edge_list_sort.remove(edge)
    node_list_sort.remove(start_node)
    tp_sort.append(start_node)
print('拓扑排序：')
print(tp_sort)
# 计算最早开始时间
temp_start_list = []
for edge in edge_list:
    temp_start_list.append(edge[1])
start_node = [x for x in node_list if x not in temp_start_list]
Ve_node_dict = {}
Ve_node_dict[start_node[0]] = 0
for node in node_list:
    Ve_tempnode_list = []
    for edge in edge_list:
        if node == edge[1]:
            temp_Ve_node_value = Ve_node_dict[edge[0]] + edge[2]
            Ve_tempnode_list.append(temp_Ve_node_value)
    if len(Ve_tempnode_list) == 0:
        Ve_node_dict[node] = 0
    if len(Ve_tempnode_list) == 1:
        Ve_node_value = Ve_tempnode_list[0]
        Ve_node_dict[node] = Ve_node_value
    if len(Ve_tempnode_list) > 1:
        Ve_node_value = max(Ve_tempnode_list)
        Ve_node_dict[node] = Ve_node_value
print('子任务最早发生时间：')
print(Ve_node_dict)
# 计算最迟开始时间
temp_end_list = []
for edge in edge_list:
    temp_end_list.append(edge[0])
end_node = [x for x in node_list if x not in temp_end_list]
Vl_node_dict = {}
Vl_node_dict[end_node[0]] = Ve_node_dict[end_node[0]]
reverse_edge_list = []
for i in range(len(edge_list)-1,-1,-1):
    reverse_edge_list.append(edge_list[i])
for node in reversed(node_list):
    Vl_tempnode_list = []
    for edge in reverse_edge_list:
        if node == edge[0]:
            temp_Vl_node_value = Vl_node_dict[edge[1]] - edge[2]
            Vl_tempnode_list.append(temp_Vl_node_value)
    if len(Vl_tempnode_list) == 0:
        Vl_node_dict[node] = Ve_node_dict[end_node[0]]
    if len(Vl_tempnode_list) == 1:
        Vl_node_value = Vl_tempnode_list[0]
        Vl_node_dict[node] = Vl_node_value
    if len(Vl_tempnode_list) > 1:
        Vl_node_value = min(Vl_tempnode_list)
        Vl_node_dict[node] = Vl_node_value
print('子任务最迟发生时间：')
print(Vl_node_dict)
# 计算时间余量
Vle_node_dict = {}
for key in Vl_node_dict:
    Vle_node_dict[key] = Vl_node_dict[key] - Ve_node_dict[key]
print('子任务时间余量：')
print(Vle_node_dict)
# 计算关键路径
e_bian_dict = {}
for edge in edge_list:
    e_bian_dict['{}-{}'.format(edge[0],edge[1])] = Ve_node_dict[edge[0]]
l_bian_dict = {}
for edge in edge_list:
    l_bian_dict['{}-{}'.format(edge[0],edge[1])] = Vl_node_dict[edge[1]] - edge[2]
d_bian_dict = {}
for bian in e_bian_dict.keys():
    d_bian_dict[bian] = l_bian_dict[bian] - e_bian_dict[bian]
print("关键路径为：")
key_path = [x for x in d_bian_dict if d_bian_dict[x] == 0]
print(key_path)
# 计算活动持续总时间
all_time = 0
for path in key_path:
    for edge in edge_list:
        a,b = path.split('-')
        if a == edge[0] and b == edge[1]:
            all_time += edge[2]
print('活动持续总时间为：')
print(all_time)
print('关键活动：')
for path in key_path:
    print(path[0],end=' ')

