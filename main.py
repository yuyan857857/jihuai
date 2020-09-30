import time

from eight_puzzle.breadth_first import *
from eight_puzzle.depth_first import *
from eight_puzzle.A_star import *

if __name__ == '__main__':
    # 深度优先算法
    originate = [2, 8, 3, 1, 6, 4, 7, 0, 5]
    target = [1, 2, 3, 7, 8, 4, 0, 6, 5]
    node1 = Node(None, originate, 0)
    node2 = Node(None, target, 0)
    depth = degth_search(node1, node2, 10, 3)
    breadth = breadth_search(node1, node2, 10, 3)
    A_star = Astar_search(node1,node2,10,3)
    Now_d = time.time()
    flag_d = depth.search()
    end_d = time.time()
    Now_b = time.time()
    flag_b = breadth.search()
    end_b = time.time()
    Now_a = time.time()
    flag_a = A_star.search()
    end_a = time.time()
    cost_d = end_d - Now_d
    cost_b = end_b - Now_b
    cost_a = end_a - Now_a
    if (flag_d):
        print('深度优先算法:已经找到路径')
        depth.showLine()
        print('深度优先算法共用时%f秒\n\n' % (cost_d))
    else:
        print('未找到路径')

    if (flag_b):
        print('广度优先算法:已经找到路径')
        breadth.showLine()
        print('广度优先算法共用时%f秒' % (cost_b))
    else:
        print('未找到路径')

    if (flag_a):
        print('A星算法：已找到路径')
        A_star.showLine()
        print('A星算法共用时%f秒' % (cost_a))
