def exist(board, word):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # 找board的i,j位置上的元素是否与word[k]一致
    def check(i, j, k):
        # 终止条件：
        # 先判断失败：若当前元素不一致，则不行
        if board[i][j] != word[k]:
            return False
        # 再判断成功:若k搜索到尽头，说明可以
        if k == len(word) - 1:
            return True
        # 加入path
        path.add((i, j))
        # 遍历所有路, 看是否能走通
        result = False  # 存放最终结果
        for di, dj in directions:
            # 处理节点
            newi, newj = i + di, j + dj
            # 走下去
            if 0 <= newi < h and 0 <= newj < w:
                # 如果当前路径还未走过
                if (newi, newj) not in path:
                    # 继续往下走
                    if check(newi, newj, k + 1):
                        # 走成功则结果为True
                        result = True
                        break
        # 回溯
        path.remove((i, j))
        # 返回回溯结果
        return result
    # 单词矩阵的长和宽
    h, w = len(board), len(board[0])
    # 结果路径的集合
    path = set()
    # 从任意起点出发
    for i in range(h):
        # 嵌套循环遍历所有节点
        for j in range(w):
            # 回溯查看是否有成功路径
            if check(i, j, 0):
                return True
    return False
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(exist(board,word))
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
print(exist(board,word))